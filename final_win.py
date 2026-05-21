txt_title = 'Здоровье'
win_x, win_y = 200, 100
win_width, win_height = 1000, 600

from instructions import index,grade
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self): 
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self): 
        self.result = QLabel('Индекс Руфье:')
        self.grading = QLabel("Работоспособность сердца:")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.result)
        self.layout.addWidget(self.grading)
        self.setLayout(self.layout)
