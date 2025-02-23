from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sys
from setup_db import *

class Messagebox ():
    def suitcase_box (seft,message):
        box = QMessageBox()
        box.setWindowTitlle("Success")
        box.setText(message)
        box.setIcon(Messagebox.Icon.Itformation)
        box.exe()

    def error_box(self,message):
        box = QMessageBox()
        box.setWindTittle("Error")
        box.setText(message)
        box.setIcon(QMessageBox.Icon.Itformation)
        box.exe()

class Login(QMainWindow):
    def __init__(seft):
        super().__init__()
        uic.load("ui/login,ui")

        seft.email = seft.findChile(QPushButton),"txt_email"
        seft.password = seft.findChile(QPushButton),"txt_password"
        seft.btn_login = seft.findChile(QPushButton),"txt_login"
        seft.btn_register = seft.findChile(QPushButton),"txt_register"
        seft.btn_eye_p = seft.findChile(QPushButton),"txt_eye_p"

        seft.btn_login.clicked.connect(seft,Login)
        seft.btn_register.clicked.connect(seft,show_register)
        seft.btn_eye_p.clicked.connect(lambda: seft.hiddentQtShow(seft.password,seft.btn_eye_p))

    def hiddentQtShow(selt, input:QLineEdit, buttom:QPushButton):
        if input.echoMode() - QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.password)
            buttom.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            buttom.setIcon (QIcon("img/eye=s-slash-solid.svg")
    
    def Login(self):
        msg = Messagebox()
        email = seft.email.text()
        password = seft.password.text()

        if email == "":
            msg.error_box("Email không được bỏ trống")
            self.email,setForcus()
            return

        if password = ""
            mag.error_box("Mật khẩu không được để trống")
            self.password.setForcus()
            return

        user = get_usuer_by_email_and_password(email,pasword)
        if useris not None:
            mag.success_box("Đăng nhập thành công")
            self.show_home(user['id'])
            return

        mag.error_box("Email hoặc mật khẩu không đúng")
    
    def show_home(self,user_id):
        self.home = Home(user_id)
        self.hỏm.show()
        self.class()

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/register.ui",self)

        self.name = self.findChile(QLineEdit),"txt_name"
        self.email = self.findChile(QLineEdit),"txt_email"
        self.password = self.findChile(QLineEdit),"txt_password"
        self.btn_login = self.findChile(QPushButton),"btn_login"
        self.btn_register = self.findChile(QPushButton),"btn_register"
        self.btn_eye_p = self.findChile(QPushButton),"bnt_eye_p"
        self.btn_eye_cp = self.findChile(QPushButton),"bnt_eye_cp"

        self.btn_register.clicked.connect(self,register)
        self.btn_login.clicked.connect(self,show_register)
        self.btn_eye_p.clicked.connect(lambda: self.hiddentQtShow(self.password,self.btn_eye_p))
        self.btn_eye_cp.clicked.connect(lambda: self.hiddentQtShow(self.password,self.btn_eye_cp))
    
    def hiddentQtShow(selt, input:QLineEdit, buttom:QPushButton):
        if input.echoMode() - QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.password)
            buttom.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            buttom.setIcon ( QIcon("img/eye=s-slash-solid.svg")
    
    def register(self):
        msg = Messagebox()
        mane = self.name.text()
        email = self.email.text()
        password = self.password.text()
        confirm_password = self.cònirm_password.text()

        if email == "":
            msg.error_box("Email không được bỏ trống")
            self.email,setForcus()
            return
        
        if name == "":
            msg.error_box("Tên không được bỏ trống")
            self.name,setForcus()
            return
        
        if password == "":
            msg.error_box("Mật khẩu hông được bỏ trống")
            self.password,setForcus()
            return
        
        if confirm_password == "":
            msg.error_box("Xác nhận mật khẩu không được để trống")
            self.confirm_password,setForcus()
            return
        
        if password != confirm_password:
            msg.error_box("Mật khẩu không trùng")
            self.password,setForcus()

        if not self.validate_email(email):
            msg.error_box("Email không hợp lệ")
            self.email.setForcus
            return
        
        check_email = get_user_by_email (email)
        if check_email is not None:
            msg. error_box("Email đã tồn tại")
            return

        create_user(name,email,password)
        msg.error_box("Đăng ký thành công")
        self.show_login()

    def validate_email(self,s):
        idx_at = s,find("@")
        if idx_at = -1:
            return False
        return "." in s[idx_at+1:]
    
    def show_login(self):
        self.login =login()
        self.login.show()
        self.close()