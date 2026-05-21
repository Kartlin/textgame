from final_win import *
from time import time
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QLineEdit

app = QApplication([])
class TestWin(QWidget):
    def __init__(self):
      super().__init__()
      self.set_appear()
      self.initUI() 
      self.connects() 
      self.show()
    def set_appear(self):
        self.setWindowTitle('Тест Руфье')
        self.move(900, 70)
        self.resize(1000, 600)
    def initUI(self):
        self.v_line = QHBoxLayout()
        self.l1 = QLabel('Введите Ф.И.О.:')
        self.name = QLineEdit()
        self.l2 = QLabel('Полных лет:')
        self.age = QLineEdit()
        self.guide1 = QLabel('''Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.
        Результат запишите в соответствующее поле.''')
        self.test1 = QPushButton('Начать первый тест')
        self.result1 = QLineEdit()
        self.guide2 = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания", чтобы запустить счетчик приседаний.')
        self.test2 = QPushButton('Начать делать приседания')
        self.guide3 = QLabel('''Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.
        Нажмите кнопку "Начать финальный тест", чтобы запустить таймер.
        Зеленым обозначены секунды, в течение которых необходимо
        проводить измерения, черным - минуты без замера пульсаций. Результаты запишите в соответствующие поля.''')
        self.test3 = QPushButton('Начать финальный тест')
        self.enter_res1 = QLineEdit()
        self.enter_res2 = QLineEdit()
        self.timer = QLabel('00:00:00')
        self.show_results = QPushButton('Отправить результаты')
        self.layout1 = QVBoxLayout()
        self.layout2 = QVBoxLayout()
        self.layout1.addWidget(self.l1)
        self.layout1.addWidget(self.name)
        self.layout1.addWidget(self.l2)
        self.layout1.addWidget(self.age)
        self.layout1.addWidget(self.guide1)
        self.layout1.addWidget(self.test1)
        self.layout1.addWidget(self.result1)
        self.layout1.addWidget(self.guide2)
        self.layout1.addWidget(self.test2)
        self.layout1.addWidget(self.guide3)
        self.layout1.addWidget(self.test3)
        self.layout1.addWidget(self.enter_res1)
        self.layout1.addWidget(self.enter_res2)
        self.layout2.addWidget(self.timer)
        self.v_line.addLayout(self.layout1)
        self.v_line.addWidget(self.show_results)
        self.v_line.addLayout(self.layout2)
        self.setLayout(self.v_line)
    def connects(self): 
        self.show_results.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = FinalWin()
