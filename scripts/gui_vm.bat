SET PYTHON_BACKUP=%PYTHON%
SET PATH_BACKUP=%PATH%
SET PYTHON=%~dp0..
SET PATH=%PYTHON%;%PYTHON%\Scripts\;%PATH%
python -m gui_vm.main
SET PATH=%PATH_BACKUP%
SET PYTHON=%PYTHON_BACKUP%