from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic


class Messagebox ():
    def success_box(self, message):
        box = QMessageBox()
        box.setWindowTitle("Success")
        box.setText(message)
        box.setIcon(QMessageBox.Icon.Information)
        box.exec()

    def error_box(self, message):
        box = QMessageBox()
        box.setWindowTitle("Error")
        box.setText(message)
        box.setIcon(QMessageBox.Icon.Critical)
        box.exec()

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Các bài qt/Home.ui",self)

        self.btn_jujuce = self.findChild(QPushButton,"btn1")
        self.btn_jujuceclicked.connect(self.show_dish)

    def show_dish(self,user_id):
        self.dish = Dish(user_id)
        self.dish.show()
        self.close()

class Dish(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Các bài qt/dish.ui",self)

      
      
        