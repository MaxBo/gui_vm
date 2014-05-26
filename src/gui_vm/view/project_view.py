# -*- coding: utf-8 -*-
from PyQt4 import (QtCore, QtGui)
from details import (SimRunDetails, ProjectDetails, ResourceDetails)
from gui_vm.model.project_tree import (Project, ProjectTreeNode, SimRun,
                                       ResourceNode, XMLParser)
from gui_vm.view.qt_designed.progress_ui import Ui_ProgressDialog
from gui_vm.model.backend import hard_copy
import sys
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class CopyFilesDialog(QtGui.QDialog, Ui_ProgressDialog):
    '''

    Parameter
    ---------
    filenames: list of Strings,
           filenames of the files to be copied
    destinations: list of Strings,
                  folders where the files shall be copied
    '''

    def __init__(self, filenames, destinations, parent=None):
        super(CopyFilesDialog, self).__init__(parent=parent)
        self.parent = parent
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setMaximumHeight(420)
        self.buttonBox.clicked.connect(self.close)
        self.show()
        self.copy(filenames, destinations)

    def copy(self, filenames, destinations):

        #todo: store changed filenames in this dict
        self.changed_filenames = {}

        if not hasattr(filenames, '__iter__'):
            filenames = [filenames]
        if not hasattr(destinations, '__iter__'):
            destinations = [destinations]
        for i in xrange(len(filenames)):
            d, filename = os.path.split(filenames[i])
            dest_filename = os.path.join(destinations[i], filename)
            do_copy = True
            if os.path.exists(dest_filename):
                reply = QtGui.QMessageBox.question(
                    self, _fromUtf8("Überschreiben"),
                    _fromUtf8("Die Datei {} existiert bereits."
                              .format(filename) +
                              "\nWollen Sie sie überschreiben?"),
                    QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                do_copy = reply == QtGui.QMessageBox.Yes
            if do_copy:
                status_txt = 'Kopiere <b>{}</b> nach <b>{}</b> ...<br>'.format(
                    filename, destinations[i])
                self.log_edit.insertHtml(status_txt)
                success = hard_copy(filenames[i], dest_filename,
                                    callback=self.progress_bar.setValue)
                if success:
                    status_txt = '{} erfolgreich kopiert<br>'.format(filename)
                else:
                    status_txt = ('<b>Fehler</b> beim Kopieren von {}<br>'
                                  .format(filename))
                self.log_edit.insertHtml(status_txt)
            else:
                status_txt = '<b>{}</b> nicht kopiert<br>'.format(
                    filename, destinations[i])
                self.log_edit.insertHtml(status_txt)
        self.progress_bar.setValue(100)

    def __del__(self):
        print 'messagebox geloescht'




class ProjectTreeView(QtCore.QAbstractItemModel):
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
    editable = QtCore.pyqtSignal(bool)
    addable = QtCore.pyqtSignal(bool)
    removable = QtCore.pyqtSignal(bool)
    resetable = QtCore.pyqtSignal(bool)
    refreshable = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None):
        super(ProjectTreeView, self).__init__()
        self.parent = parent
        self.root = ProjectTreeNode('root')
        self.header = ('Projektbrowser', 'Details')
        self.count = 0
        self.details = None
        self.current_index = None

    @property
    def selected_item(self):
        return self.nodeFromIndex(self.current_index)

    @property
    def project(self):
        return self.root.child_at_row(0)

    def add(self):
        node = self.selected_item
        if isinstance(node, Project):
            self.add_run()
        elif isinstance(node, SimRun):
            self.add_run()

    def remove(self):
        node = self.selected_item
        if isinstance(node, SimRun):
            self.remove_run()
        elif isinstance(node, ResourceNode):
            self.remove_resource()

    def edit(self):
        node = self.selected_item
        if node.rename:
            text, ok = QtGui.QInputDialog.getText(
                None, 'Umbenennen', 'Neuen Namen eingeben:',
                QtGui.QLineEdit.Normal, node.name)
            if ok:
                node.name = str(text)
                self.project_changed.emit()

    def reset(self):
        node = self.selected_item
        if isinstance(node, SimRun):
            self.reset_simrun()
        elif isinstance(node, ResourceNode):
            self.reset_resource()

    def add_run(self):
        project = self.project
        text, ok = QtGui.QInputDialog.getText(
            None, 'Neues Szenario', 'Name des neuen Szenarios:',
            QtGui.QLineEdit.Normal,
            'Szenario {}'.format(project.child_count))
        if ok:
            name = str(text)
            if name in project.children_names:
                QtGui.QMessageBox.about(
                    None, "Fehler",
                    _fromUtf8("Der Szenarioname '{}' ist bereits vergeben."
                              .format(name)))
            else:
                project.add_run(model='Maxem', name=name)
                self.project_changed.emit()

    def remove_run(self):
        node = self.selected_item
        parent = node.parent
        self.project.remove_run(node.name)
        #select parent
        parent_idx = self.createIndex(
            0, 0, parent)
        self.item_clicked(parent_idx)

    def remove_resource(self):
        '''
        remove the source of the resource node and optionally remove it from
        the disk
        '''
        node = self.selected_item
        if os.path.exists(node.full_source):
            reply = QtGui.QMessageBox.question(
                None, _fromUtf8("Löschen"),
                _fromUtf8("Soll die Datei {} \nin {}\n".format(
                    node.resource.file_name, node.full_path) +
                          "ebenfalls entfernt werden?"),
                QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            do_delete = reply == QtGui.QMessageBox.Yes
            if do_delete:
                os.remove(node.full_source)
        node.set_source(None)
        node.update()
        self.project_changed.emit()

    def reset_simrun(self):
        '''
        set the simrun to default, copy all files from the default folder
        to the project/scenario folder and link the project tree to those
        files
        '''
        #self.project_tree_view.reset(self.row_index)
        simrun_node = self.selected_item
        simrun_node = simrun_node.reset_to_default()
        filenames = []
        destinations = []
        for res_node in simrun_node.get_resources():
            filenames.append(res_node.original_source)
            destinations.append(os.path.join(res_node.full_path))

        #bad workaround (as it has to know the parents qtreeview)
        #but the view crashes otherwise, maybe make update signal
        self.parent.qtreeview.setUpdatesEnabled(False)
        dialog = CopyFilesDialog(filenames, destinations, parent=self.parent)
        self.parent.qtreeview.setUpdatesEnabled(True)
        #dialog.deleteLater()
        simrun_node.update()
        self.project_changed.emit()

    def reset_resource(self):
        res_node = self.selected_item
        res_node.reset_to_default()
        filename = res_node.original_source
        destination = res_node.full_path
        dialog = CopyFilesDialog(filename, destination, parent=self.parent)
        res_node.update()
        self.project_changed.emit()

    def write_project(self, filename):
        XMLParser.write_xml(self.project, filename)

    def create_project(self, name, folder):
        if name is None:
            name = 'Neues Projekt'
        if self.project:
            self.project.remove()
        self.root.add_child(Project(name))
        #select first row
        index = self.createIndex(
            0, 0, self.project)
        self.item_clicked(index)
        self.project.project_folder = folder

    def read_project(self, filename):
        if self.project:
            self.project.remove()
        self.root = XMLParser.read_xml('root', filename)
        self.project.update()
        self.view_changed.emit()

    def item_clicked(self, index):
        '''
        show details when row of project tree is clicked
        details shown depend on type of node that is behind the clicked row
        '''
        self.current_index = index
        node = self.selected_item
        #def do_nothing(*args): pass

        #clear the old details
        if self.details:
            self.details.close()
            self.details = None

        if node.rename:
            self.editable.emit(True)
        else:
            self.editable.emit(False)

        if isinstance(node, Project):
            self.addable.emit(True)
            #self.add = self.add_run
            self.removable.emit(False)
            #self.remove = do_nothing
            self.resetable.emit(False)
            #self.reset = do_nothing
            self.refreshable.emit(True)
            #self.refresh = do_nothing
            self.details = ProjectDetails(node)

        elif isinstance(node, SimRun):
            self.addable.emit(True)
            self.removable.emit(True)
            self.resetable.emit(True)
            self.refreshable.emit(True)
            self.details = SimRunDetails(node)

        elif isinstance(node, ResourceNode):
            self.addable.emit(False)
            self.removable.emit(True)
            self.resetable.emit(True)
            self.refreshable.emit(True)
            self.details = ResourceDetails(node)

        else:
            self.addable.emit(False)
            self.removable.emit(False)
            self.resetable.emit(False)
            self.refreshable.emit(False)

        if self.details:
            self.details.value_changed.connect(self.project_changed)
        self.dataChanged.emit(index, index)

    def replace(self, index, new_node):
        pass

    ##### overrides for viewing in qtreeview #####

    def headerData(self, section, orientation, role):
        if (orientation == QtCore.Qt.Horizontal and
            role == QtCore.Qt.DisplayRole):
            return QtCore.QVariant(self.header[section])
        return QtCore.QVariant()

    def index(self, row, column, parent_index):
        node = self.nodeFromIndex(parent_index)
        return self.createIndex(row, column, node.child_at_row(row))


    def data(self, index, role):
        '''
        return data to the tableview depending on the requested role
        '''
        node = self.nodeFromIndex(index)
        if node is None:
            return QtCore.QVariant()
        #print '{} - {}'.format(node.name, sys.getrefcount(node))
        is_valid = True
        is_checked = False
        if hasattr(node, 'resource'):
            is_valid = node.resource.is_valid
            is_checked = node.resource.is_checked

        if role == QtCore.Qt.DecorationRole:
            return QtCore.QVariant()

        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.QVariant(
                int(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft))

        if role == QtCore.Qt.UserRole:
            return node

        #color the the 2nd column of a node depending on its status
        if role == QtCore.Qt.TextColorRole and index.column() == 1:
            if is_checked:
                if is_valid:
                    return QtCore.QVariant(QtGui.QColor(QtCore.Qt.darkGreen))
                else:
                    return QtCore.QVariant(QtGui.QColor(QtCore.Qt.red))
            else:
                return QtCore.QVariant(QtGui.QColor(QtCore.Qt.black))

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

    def parent(self, child):
        print self.count
        self.count += 1
        if not child.isValid():
            return QModelIndex()

        node = self.nodeFromIndex(child)

        if node is None or not isinstance(node, ProjectTreeNode):
            return QtCore.QModelIndex()

        parent = node.parent

        if parent is None:
            return QtCore.QModelIndex()

        grandparent = parent.parent
        if grandparent is None:
            return QtCore.QModelIndex()
        row = grandparent.row_of_child(parent)

        assert row != - 1
        return self.createIndex(row, 0, parent)

    def nodeFromIndex(self, index):
        return index.internalPointer() if index.isValid() else self.root

    #def flags(self, index):
        #defaultFlags = QAbstractItemModel.flags(self, index)

        #if index.isValid():
            #return Qt.ItemIsEditable | Qt.ItemIsDragEnabled | \
                    #Qt.ItemIsDropEnabled | defaultFlags

        #else:
            #return Qt.ItemIsDropEnabled | defaultFlags


    #def mimeTypes(self):
        #types = QStringList()
        #types.append('application/x-ets-qt4-instance')
        #return types

    #def mimeData(self, index):
        #node = self.nodeFromIndex(index[0])
        #mimeData = PyMimeData(node)
        #return mimeData


    #def dropMimeData(self, mimedata, action, row, column, parentIndex):
        #if action == Qt.IgnoreAction:
            #return True

        #dragNode = mimedata.instance()
        #parentNode = self.nodeFromIndex(parentIndex)

        ## make an copy of the node being moved
        #newNode = deepcopy(dragNode)
        #newNode.setParent(parentNode)
        #self.insertRow(len(parentNode)-1, parentIndex)
        #self.emit(SIGNAL("dataChanged(QModelIndex,QModelIndex)"),
#parentIndex, parentIndex)
        #return True


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
        node.remove_child_at(row)
        self.endRemoveRows()

        return True
