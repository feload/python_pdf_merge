from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
button = QPushButton('Click me')


def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked it!')
    alert.exec_()


button.clicked.connect(on_button_clicked)

layout.addWidget(button)

window.setLayout(layout)
window.show()

app.exec_()
