# -*- coding: utf-8 -*-
from PyQt4 import (QtCore, QtGui)
from details import (ScenarioDetails, ProjectDetails, InputDetails, OutputDetails)
from gui_vm.model.project_tree import (Project, TreeNode, Scenario,
                                       InputNode, XMLParser, OutputNode)
from gui_vm.control.dialogs import (CopyFilesDialog, ExecDialog,
                                    NewScenarioDialog, RunOptionsDialog,
                                    InputDialog)
from gui_vm.config.config import Config
import os, subprocess
from shutil import rmtree

config = Config()
config.read()

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class ProjectTreeControl(QtCore.QAbstractItemModel):
    '''
    view on the project, holds the project itself and communicates with it,
    decides how to act on user input,
    also serves as an itemmodel to make the nodes showable in a qtreeview
    via indexing

    Parameter
    ---------
    parent: the window, where the dialogs will be shown in
    '''

    project_changed = QtCore.pyqtSignal()
    view_changed = QtCore.pyqtSignal()

    def __init__(self, view=None):
        super(ProjectTreeControl, self).__init__()
        self.tree_view = view
        self.model = None
        self.header = ('Projekt', 'Details')
        self.count = 0
        self.current_index = None

    @property
    def selected_item(self):
        if self.current_index is None:
            return None
        return self.nodeFromIndex(self.current_index)

    @property
    def project(self):
        return self.model.child_at_row(0)

    ##### overrides for viewing in qtreeview #####

    def headerData(self, section, orientation, role):
        if (orientation == QtCore.Qt.Horizontal and
            role == QtCore.Qt.DisplayRole):
            return QtCore.QVariant(self.header[section])
        return QtCore.QVariant()

    def index(self, row, column, parent_index):
        node = self.nodeFromIndex(parent_index)
        if row >= 0 and len(node.children) > row:
            return self.createIndex(row, column, node.child_at_row(row))
        else:
            return QtCore.QModelIndex()


    def data(self, index, role):
        '''
        return data to the tableview depending on the requested role
        '''
        node = self.nodeFromIndex(index)
        if node is None:
            return QtCore.QVariant()

        if role == QtCore.Qt.DecorationRole:
            return QtCore.QVariant()

        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.QVariant(
                int(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft))

        if role == QtCore.Qt.UserRole:
            return node

        #color the the 2nd column of a node depending on its status
        if role == QtCore.Qt.TextColorRole and index.column() == 1:
            #if hasattr(node, 'is_checked'):
            is_checked = node.is_checked
            if is_checked:
                #if hasattr(node, 'is_valid'):
                is_valid = node.is_valid
                if is_valid:
                    return QtCore.QVariant(QtGui.QColor(QtCore.Qt.darkGreen))
                else:
                    return QtCore.QVariant(QtGui.QColor(QtCore.Qt.red))
            else:
                return QtCore.QVariant(QtGui.QColor(QtCore.Qt.black))

        if role == QtCore.Qt.FontRole:
            #if  (index.column() == 0 and
            if (isinstance(node, Scenario) or isinstance(node, Project)):
                return QtCore.QVariant(
                    QtGui.QFont("Arial", 9, QtGui.QFont.Bold))
            else:
                return QtCore.QVariant(QtGui.QFont("Arial", 9))

        #all other roles (except display role)
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        #Display Role (text)
        if index.column() == 0:
            return QtCore.QVariant(node.name)

        elif index.column() == 1:
            return QtCore.QVariant(node.note)

        else:
            return QtCore.QVariant()

    def columnCount(self, parent):
        return len(self.header)

    def rowCount(self, parent):
        node = self.nodeFromIndex(parent)
        if node is None:
            return 0
        return node.child_count

    def parent(self, child_idx):
        if not child_idx.isValid():
            return QtCore.QModelIndex()

        node = self.nodeFromIndex(child_idx)

        if node is None or not isinstance(node, TreeNode):
            return QtCore.QModelIndex()

        parent = node.parent

        if parent is None:
            return QtCore.QModelIndex()

        grandparent = parent.parent
        if grandparent is None:
            row = 0
        else:
            row = grandparent.row_of_child(parent)

        assert row != - 1
        return self.createIndex(row, 0, parent)

    def nodeFromIndex(self, index):
        return index.internalPointer() if index.isValid() else self.model

    def insertRow(self, row, parent):
        return self.insertRows(row, 1, parent)

    def insertRows(self, row, count, parent):
        self.beginInsertRows(parent, row, (row + (count - 1)))
        self.endInsertRows()
        return True

    def remove_row(self, row, parentIndex):
        return self.removeRows(row, 1, parentIndex)

    def removeRows(self, row, count, parentIndex):
        self.beginRemoveRows(parentIndex, row, row)
        node = self.nodeFromIndex(parentIndex)
        if len(node.children) > row:
            node.remove_child_at(row)
        self.endRemoveRows()

        return True

    def pop_context_menu(self, pos):
        pass


class VMProjectControl(ProjectTreeControl):
    def __init__(self, view=None, details_view=None, button_group=None):
        super(VMProjectControl, self).__init__(view)
        self.model = TreeNode('root')
        self.details_view = details_view
        self.button_group = button_group
        self.plus_button = self.button_group.findChild(
            QtGui.QAbstractButton, 'plus_button')
        self.minus_button = self.button_group.findChild(
            QtGui.QAbstractButton, 'minus_button')
        self.edit_button = self.button_group.findChild(
            QtGui.QAbstractButton, 'edit_button')
        self.reset_button = self.button_group.findChild(
            QtGui.QAbstractButton, 'reset_button')
        self.lock_button = self.button_group.findChild(
            QtGui.QAbstractButton, 'lock_button')
        self.copy_button = self.button_group.findChild(
            QtGui.QAbstractButton, 'copy_button')
        self.clean_button = self.button_group.findChild(
            QtGui.QAbstractButton, 'clean_button')

        self.view_changed.connect(self.update_view)
        self.dataChanged.connect(self.update_view)

        # connect the context buttons with the defined actions
        self.plus_button.clicked.connect(lambda: self.start_function('add'))
        self.minus_button.clicked.connect(lambda: self.start_function('remove'))
        self.edit_button.clicked.connect(lambda: self.start_function('edit'))
        self.reset_button.clicked.connect(lambda: self.start_function('reset'))
        #self.start_button.clicked.connect(self.project_control.execute)
        self.lock_button.clicked.connect(lambda:
                                         self.start_function('switch_lock'))
        self.copy_button.clicked.connect(lambda: self.start_function('copy'))

        self.project_changed.connect(self.item_clicked)

        for button in self.button_group.children():
            button.setEnabled(False)

        self.context_map = {
            'add': {
                Project: [self.add_scenario, 'Szenario hinzufügen'],
                Scenario: [self.add_scenario, 'Szenario hinzufügen'],
                OutputNode: [self.add_special_run, 'spezifischen Lauf hinzufügen']
            },
            'remove': {
                Scenario: [self._remove_scenario, 'Szenario entfernen'],
                InputNode: [self.remove_resource, 'Eingabedaten entfernen'],
                OutputNode: [self._remove_output, 'Ausgabedaten entfernen']
            },
            'reset': {
                Scenario: [self._reset_scenario, 'Szenario zurücksetzen'],
                InputNode: [self._reset_resource, 'Eingabedaten zurücksetzen']
            },
            'edit': {
                Scenario: [self._rename, 'Szenario umbenennen'],
                Project: [self._rename, 'Projekt umbenennen'],
                InputNode: [self.edit_resource, 'Eingabedaten editieren'],
                OutputNode: [self.edit_resource, 'Ausgabedaten editieren']
            },
            'execute': {
                Scenario: [self.run_complete, 'Szenario starten']
            },
            'switch_lock': {
                Scenario: [self._switch_lock, 'Szenario sperren'],
            },
            'copy': {
                Scenario: [self._clone_scenario, 'Szenario klonen'],
                OutputNode: [self._copy_special_run, 'spezifischen Lauf kopieren']
            },
            'clean': {

            },
        }

    def item_clicked(self, index=None):
        '''
        show details when row of project tree is clicked
        details shown depend on type of node that is behind the clicked row
        '''
        if index is not None:
            self.current_index = index
        self.dataChanged.emit(self.current_index, self.current_index)

    def start_function(self, function_name):
        node = self.selected_item
        cls = node.__class__
        if cls in self.context_map[function_name]:
            self.context_map[function_name][cls][0]()
        self.project_changed.emit()

    def _map_buttons(self, node):

        # emit signal flags for context
        locked = node.locked
        cls = node.__class__

        def map_button(button, map_name, depends_on_lock=False):
            enabled = is_in_map = cls in self.context_map[map_name]
            if depends_on_lock:
                enabled = is_in_map and not locked
            button.setEnabled(enabled)
            if is_in_map:
                tooltip = _fromUtf8(self.context_map[map_name][cls][1])
            else:
                tooltip = ''
            button.setToolTip(tooltip)

        map_button(self.plus_button,'add')
        map_button(self.minus_button, 'remove', True)
        if(len(config.settings['trafficmodels'][node.model.name]['default_folder']) > 0):
            map_button(self.reset_button, 'reset', True)
        map_button(self.edit_button, 'edit', True)
        #self.start_button.setEnabled(cls in self.context_map['execute'])
        map_button(self.lock_button, 'switch_lock')
        if node.locked:
            self.lock_button.setChecked(True)
        else:
            self.lock_button.setChecked(False)
        map_button(self.copy_button, 'copy')
        map_button(self.clean_button, 'clean')

    def pop_context_menu(self, pos):
        node = self.selected_item
        if node.locked:
            return
        cls = node.__class__
        context_menu = QtGui.QMenu()
        action_map = {}
        for key, value in self.context_map.iteritems():
            if cls in value:
                action_map[context_menu.addAction(_fromUtf8(value[cls][1]))] = \
                    value[cls][0]
        action = context_menu.exec_(self.tree_view.mapToGlobal(pos))
        context_menu.close()
        if action:
            action_map[action]()

    def update_view(self):
        self.tree_view.expandAll()
        for column in range(self.tree_view.model()
                            .columnCount(QtCore.QModelIndex())):
            self.tree_view.resizeColumnToContents(column)

        #clear the old details
        for i in reversed(range(self.details_view.count())):
            widget = self.details_view.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        #get new details depending on type of node
        node = self.selected_item
        if node is None:
            return

        details = None

        if isinstance(node, Project):
            details = ProjectDetails(node)
        elif isinstance(node, Scenario):
            details = ScenarioDetails(node, self)
        elif isinstance(node, InputNode):
            details = InputDetails(node, self)
        elif isinstance(node, OutputNode):
            model = node.get_parent_by_class(Scenario).model
            details = OutputDetails(node, model.evaluate)

        #track changes made in details
        if details:
            details.value_changed.connect(self.view_changed)
            details.value_changed.connect(self.project_changed.emit)
            self.details_view.addWidget(details)
            details.update()

        self._map_buttons(node)

    def _remove_node(self, node):
        if not node:
            node = self.selected_item
        parent_idx = self.parent(self.current_index)
        cur_tmp = self.current_index
        self.item_clicked(parent_idx)
        self.remove_row(cur_tmp.row(),
                        parent_idx)
        node.remove_all_children()

    def _remove_scenario(self, scenario_node=None):
        if not scenario_node:
            scenario_node = self.selected_item
        path = scenario_node.path
        reply = QtGui.QMessageBox.question(
            None, _fromUtf8("Löschen"),
            _fromUtf8("Soll das gesamte Szenario-Verzeichnis {}\n".format(
                path) + "von der Festplatte entfernt werden?"),
            QtGui.QMessageBox.Yes, QtGui.QMessageBox.No, QtGui.QMessageBox.Cancel)
        if reply == QtGui.QMessageBox.Cancel:
            return
        if reply == QtGui.QMessageBox.Yes:
            try:
                rmtree(scenario_node.path)
            except Exception, e:
                QtGui.QMessageBox.about(
                None, "Fehler", str(e))
        self._remove_node(scenario_node)


    def remove_resource(self, resource_node=None, remove_node=False,
                        confirmation=True, remove_outputs=True):
        '''
        remove the source of the resource node and optionally remove it from
        the disk
        '''
        if not resource_node:
            resource_node = self.selected_item
        if resource_node.locked:
            QtGui.QMessageBox.about(
                None, "Fehler",
                _fromUtf8("Die Ressource ist gesperrt und kann nicht " +
                          "gelöscht werden."))
            return
        file_absolute = resource_node.file_absolute
        if file_absolute and os.path.exists(file_absolute):
            do_delete = True
            if confirmation:
                reply = QtGui.QMessageBox.question(
                    None, _fromUtf8("Löschen"),
                    _fromUtf8("Soll die Datei {} \n".format(file_absolute) +
                              "ebenfalls entfernt werden?"),
                    QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                do_delete = reply == QtGui.QMessageBox.Yes
            if do_delete:
                os.remove(resource_node.file_absolute)
        resource_node.file_relative = None
        if remove_node:
            self._remove_node(resource_node)
        else:
            resource_node.update()

        if remove_outputs:
            scenario = resource_node.scenario
            self.remove_outputs(scenario)
        self.project_changed.emit()

    def _remove_output(self, resource_node=None):
        if not resource_node:
            resource_node = self.selected_item

        scenario = resource_node.scenario
        if resource_node.is_primary:
            msg = "Soll der Gesamtlauf wirklich entfernt werden?"
            if len(scenario.get_output_files()) > 1:
                msg += "\nAlle spezifischen Läufe werden ebenfalls gelöscht!"
            reply = QtGui.QMessageBox.question(
                None, _fromUtf8("Löschen"), _fromUtf8(msg),
                QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
            if reply == QtGui.QMessageBox.Ok:
                cur_tmp = self.current_index
                parent_idx = self.current_index.parent()
                self.item_clicked(parent_idx.parent())
                self.remove_row(parent_idx.row(), parent_idx.parent())
                self.remove_outputs(scenario)
        else:
            self.remove_resource(remove_node=True, remove_outputs=False,
                                 confirmation=False)

    def run_complete(self, scenario_node=None):
        if not scenario_node:
            scenario_node = self.selected_item

        options, ok = RunOptionsDialog.getValues(scenario_node, is_primary=True)
        dialog = ExecDialog(scenario_node, 'Gesamtlauf',
                            parent=self.tree_view, options=options)

    def run(self, scenario_name):
        scenario_node = self.project.get_child(scenario_name)
        if scenario_node:
            self.run_complete(scenario_node)
        else:
            QtGui.QMessageBox.about(
                self, 'Szenario {} nicht gefunden!'.format(scenario_name))

    def _switch_lock(self, resource_node=None):
        if not resource_node:
            resource_node = self.selected_item
        resource_node.locked = not resource_node.locked
        self.project_changed.emit()

    def _rename(self):
        node = self.selected_item
        text, ok = QtGui.QInputDialog.getText(
            None, 'Umbenennen', 'Neuen Namen eingeben:',
            QtGui.QLineEdit.Normal, node.name)
        if ok:
            node.name = str(text)
            self.project_changed.emit()

    def _copy_special_run(self, output_node=None):
        #ToDo: Dropdown with every scenario with same model
        #if exists with name -> rename '<name>-2' '<name>-3' etc. (loop)
        pass

    def _clone_scenario(self, scenario_node=None):
        if not scenario_node:
            scenario_node = self.selected_item
        text, ok = QtGui.QInputDialog.getText(
                    None, 'Szenario kopieren', 'Name des neuen Szenarios:',
                    QtGui.QLineEdit.Normal, scenario_node.name + ' - Kopie')
        if ok:
            new_scen_name = str(text)
            if new_scen_name in self.project.children_names:
                QtGui.QMessageBox.about(
                    None, "Fehler",
                    _fromUtf8("Der Szenarioname '{}' ist bereits vergeben."
                              .format(new_scen_name)))
                return
            new_scenario_node = scenario_node.clone(new_scen_name)
            scenario_node.parent.add_child(new_scenario_node)
            path = new_scenario_node.path
            if os.path.exists(new_scenario_node.path):
                reply = QtGui.QMessageBox.question(
                    None, _fromUtf8("Fehler"),
                    _fromUtf8("Der Pfad '{}' existiert bereits. Fortsetzen?"
                                  .format(path)),
                    QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                if reply == QtGui.QMessageBox.No:
                    return
            filenames = []
            destinations = []
            for i, nodes in enumerate([scenario_node.get_input_files(),
                                       scenario_node.get_output_files()]):
                is_input = i == 0
                for res_node in nodes:
                    if is_input:
                        new_res_node = new_scenario_node.get_input(res_node.name)
                    else:
                        new_res_node = new_scenario_node.get_output(res_node.name)
                    if new_res_node and os.path.exists(res_node.file_absolute):
                        filenames.append(res_node.file_absolute)
                        destinations.append(os.path.split(new_res_node.file_absolute)[0])

            #bad workaround (as it has to know the parents qtreeview)
            #but the view crashes otherwise, maybe make update signal
            self.tree_view.setUpdatesEnabled(False)
            dialog = CopyFilesDialog(filenames, destinations,
                                     parent=self.tree_view)
            self.tree_view.setUpdatesEnabled(True)
            scenario_node.update()
            self.project_changed.emit()

    def edit_resource(self, resource_node=None):
        if not resource_node:
            resource_node = self.selected_item
        node = self.selected_item
        hdf5_viewer = config.settings['environment']['hdf5_viewer']
        if hdf5_viewer:
            subprocess.Popen('"{0}" "{1}"'.format(hdf5_viewer,
                                                  node.file_absolute))
        else:
            QtGui.QMessageBox.about(
                None, "Fehler",
                _fromUtf8("In den Einstellungen ist kein HDF5-Editor angegeben."))

    def add_scenario(self):
        project = self.project
        if (not project):
            return
        default_name = 'Szenario {}'.format(project.child_count)
        scenario_name, model_name, ok = NewScenarioDialog.getValues(default_name)
        if ok:
            if scenario_name in project.children_names:
                QtGui.QMessageBox.about(
                    None, "Fehler",
                    _fromUtf8("Der Szenarioname '{}' ist bereits vergeben."
                              .format(scenario_name)))
            else:
                project.add_scenario(model=model_name, name=scenario_name)
                if(len(config.settings['trafficmodels'][model_name]['default_folder']) > 0):
                    reply = QtGui.QMessageBox.question(
                        None, _fromUtf8("Neues Szenario erstellen"),
                        _fromUtf8("Möchten Sie die Standarddateien " +
                                  "für das neue Szenario verwenden?"),
                        QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                    do_copy = reply == QtGui.QMessageBox.Yes
                    if do_copy:
                        self._reset_scenario(
                            scenario_node=project.get_child(scenario_name))
                    self.project_changed.emit()

    def add_special_run(self, node=None):
        if not node:
            node = self.selected_item
        scenario = node.scenario
        options, ok = RunOptionsDialog.getValues(scenario, is_primary = False)
        if ok:
            default = 'spezifischer Lauf {}'.format(
                len(scenario.get_output_files()) - 1)
            run_name, ok = InputDialog.getValues(_fromUtf8(
                'Name für den spezifischen Lauf'), default)
            if ok:
                scenario.add_run(run_name, options=options)

    def _reset_scenario(self, scenario_node=None):
        '''
        set the simrun to default, copy all files from the default folder
        to the project/scenario folder and link the project tree to those
        files
        '''
        #self.project_tree_view.reset(self.row_index)
        if not scenario_node:
            scenario_node = self.selected_item
        scenario_node = scenario_node.reset_to_default()

        if not scenario_node:
            QtGui.QMessageBox.about(
                None, "Fehler",
                _fromUtf8("Die Defaults des Modells " +
                          "konnten nicht geladen werden."))
        else:
            filenames = []
            destinations = []
            for res_node in scenario_node.get_input_files():
                filenames.append(res_node.original_source)
                destinations.append(os.path.split(res_node.file_absolute)[0])

            #bad workaround (as it has to know the parents qtreeview)
            #but the view crashes otherwise, maybe make update signal
            self.tree_view.setUpdatesEnabled(False)
            dialog = CopyFilesDialog(filenames, destinations,
                                     parent=self.tree_view)
            self.tree_view.setUpdatesEnabled(True)
            #dialog.deleteLater()
            scenario_node.update()
            self.remove_outputs(scenario_node)

        self.project_changed.emit()

    def validate_project(self):
        scenarios = self.project.find_all_by_class(Scenario)
        for scen in scenarios:
            scen.validate()
        self.view_changed.emit()

    def _reset_resource(self):
        res_node = self.selected_item
        res_node.reset_to_default()
        filename = res_node.original_source
        destination = os.path.split(res_node.file_absolute)[0]
        dialog = CopyFilesDialog(filename, destination,
                                 parent=self.tree_view)
        res_node.update()
        scenario = res_node.scenario
        self.remove_outputs(scenario)
        self.project_changed.emit()

    def write_project(self, filename):
        XMLParser.write_xml(self.project, filename)

    def new_project(self, name, project_folder):
        if name is None:
            name = 'Neues Projekt'
        if self.project:
            self.remove(self.project)
            self.remove_row(self.current_index.row(),
                            self.parent(self.current_index))
        self.model.add_child(Project(name, project_folder=project_folder))
        self.project.on_change(self.project_changed.emit)
        self.item_clicked(self.createIndex(0, 0, self.project))

    def read_project(self, filename):
        self.current_index = self.createIndex(0, 0, self.project)
        if self.project:
            self.remove(self.project)
            self.remove_row(self.current_index.row(),
                            self.parent(self.current_index))
        self.model = XMLParser.read_xml(self.model, filename)
        self.project.on_change(self.project_changed.emit)
        self.project.project_folder = os.path.split(filename)[0]
        self.project.update()
        self.project_changed.emit()
        self.view_changed.emit()

    def remove_outputs(self, scenario):
        for output in scenario.get_output_files():
            try:
                rmtree(os.path.split(output.file_absolute)[0])
            except:
                pass
        output = scenario.get_child(scenario.OUTPUT_NODES)
        if output:
            output.remove_all_children()