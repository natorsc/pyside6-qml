# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QML Button."""

import sys
from pathlib import Path

from PySide6 import QtCore, QtGui, QtWidgets, QtQml

BASE_DIR = Path(__file__).resolve().parent
UI = BASE_DIR.joinpath('MainWindow.qml')
RESOURCES_RC_PY = BASE_DIR.joinpath('resources_rc.py')
_SCRIPTS = BASE_DIR.parent.parent.joinpath('_scripts')

sys.path.append(str(_SCRIPTS))

import _tools

_tools.compile_resources(output=RESOURCES_RC_PY)
_tools.format_qml_file(path=BASE_DIR)

import resources_rc

RESOURCES_RC = resources_rc


class MainWindow(QtCore.QObject):

    def __init__(self, parent=None, **kwargs):
        super().__init__(parent=parent)
        self.application = kwargs.get('application')

    @QtCore.Slot()
    def on_button_clicked(self):
        print(self.tr('Python: Botão pressionado.'))


if __name__ == "__main__":
    APPLICATION_NAME = 'br.com.justcode.QML'
    ORGANIZATION_NAME = APPLICATION_NAME.split('.')[2]
    ORGANIZATION_DOMAIN = '.'.join(APPLICATION_NAME.split('.')[0:3])

    application = QtWidgets.QApplication(sys.argv)
    application.setWindowIcon(QtGui.QIcon(':/window/icon'))
    application.setOrganizationName(ORGANIZATION_NAME)
    application.setOrganizationDomain(ORGANIZATION_DOMAIN)
    application.setApplicationName(APPLICATION_NAME)
    application.setDesktopFileName(APPLICATION_NAME)

    if QtCore.QSysInfo.productType() == 'windows':
        from ctypes import windll

        windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            APPLICATION_NAME,
        )

    mainwindow = MainWindow(application=application)

    engine = QtQml.QQmlApplicationEngine()
    engine.rootContext().setContextProperty('mainwindow', mainwindow)
    engine.load(QtCore.QUrl.fromLocalFile(UI))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(application.exec())
