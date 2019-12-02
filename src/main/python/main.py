from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton

import sys

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked it!')
    alert.exec_()

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = QMainWindow()
    window.resize(250, 150)

    button = QPushButton('Click me')
    button.clicked.connect(on_button_clicked)

    layout = QVBoxLayout()
    layout.addWidget(button)

    window.setLayout(layout)
    window.show()

    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
