from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
from database import *

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

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/loggin.ui",self)

        self.email = self.findChild(QLineEdit,"txt_email_2")
        self.password = self.findChild(QLineEdit,"txt_password_3")
        self.btn_login = self.findChild(QPushButton,"btn_login_2")
        self.btn_register = self.findChild(QPushButton,"btn_register")
        self.btn_eye_p = self.findChild(QPushButton,"btn_eye_p")

        self.btn_login.clicked.connect(self.login)
        self.btn_register.clicked.connect(self.show_register)
        self.btn_eye_p.clicked.connect(lambda: self.hiddenOrShow(self.password,self.btn_eye_p))

    def hiddenOrShow(self, input:QLineEdit, button:QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            button.setIcon(QIcon("img/eye-solid.png"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            button.setIcon(QIcon("img/eye-slash-solid.png"))

    def login(self):
        msg = Messagebox()
        email = self.email.text().strip()
        password = self.password.text().strip()

        if email == "":
            msg.error_box("Email không được bỏ trống")
            self.email.setFocus()
            return

        if password == "":
            msg.error_box("Mật khẩu không được để trống")
            self.password.setFocus()
            return

        user = get_user_by_email_and_password(email, password)
        if user is not None:
            msg.success_box("Đăng nhập thành công")
            self.show_home(user['id'])
            return
        msg.error_box("Email hoặc mật khẩu không đúng")
        
    def show_register(self):
        self.register = Register()
        self.register.show()
        self.hide()
    
    def show_home(self,user_id):
        self.home = Home(user_id)
        self.home.show()
        self.close()

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/Sign_Up.ui",self)

        self.name = self.findChild(QLineEdit,"txt_name")
        self.email = self.findChild(QLineEdit,"txt_email")
        self.password = self.findChild(QLineEdit,"txt_password")
        self.confirm_password = self.findChild(QLineEdit,"txt_confirm_pwd")
        self.btn_login = self.findChild(QPushButton,"btn_login")
        self.btn_register = self.findChild(QPushButton,"btn_register")
        self.btn_eye_p = self.findChild(QPushButton,"btn_eye_p")
        self.btn_eye_cp = self.findChild(QPushButton,"btn_eye_cp")

        self.btn_register.clicked.connect(self.register)
        self.btn_login.clicked.connect(self.show_login)
        self.btn_eye_p.clicked.connect(lambda: self.hiddenOrShow(self.password,self.btn_eye_p))
        self.btn_eye_cp.clicked.connect(lambda: self.hiddenOrShow(self.confirm_password,self.btn_eye_cp))
    
    def hiddenOrShow(self, input:QLineEdit, button:QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            button.setIcon(QIcon("img/eye-solid.png"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            button.setIcon(QIcon("img/eye-slash-solid.png"))
    
    def register(self):
        msg = Messagebox()
        name = self.name.text().strip()
        email = self.email.text().strip()
        password = self.password.text().strip()
        confirm_password = self.confirm_password.text().strip()

        if email == "":
            msg.error_box("Email không được bỏ trống")
            self.email.setFocus()
            return
        
        if name == "":
            msg.error_box("Tên không được bỏ trống")
            self.name.setFocus()
            return
        
        if any(c in "@!#$%^&*()~><?/:'\"{}" for c in name):
            msg.error_box("Tên không được có các kí tự đặc biệt")
            self.name.setFocus()
            return
    
        if password == "":
            msg.error_box("Mật khẩu không được bỏ trống")
            self.password.setFocus()
            return
        
#        if len(password.split()) < 6:
#            msg.error_box("Mật khẩu phải có tối thiểu 6 ký tự")
#            self.password.setFocus()
#            return

#        if len(password.split()) > 14:
#            msg.error_box("Mật khẩu chỉ có tối đa 14 ký tự")
#            self.password.setFocus()
#            return

        if confirm_password == "":
            msg.error_box("Xác nhận mật khẩu không được để trống")
            self.confirm_password.setFocus()
            return
              
        if password != confirm_password:
            msg.error_box("Mật khẩu không trùng")
            self.password.setFocus()
            return

        if not self.validate_email(email):
            msg.error_box("Email không hợp lệ")
            self.email.setFocus()
            return
        
        check_email = get_user_by_email (email)
        if check_email is not None:
            msg.error_box("Email đã tồn tại")
            self.email.setFocus()
            return

        create_user(name,email,password)
        msg.error_box("Đăng ký thành công")
        self.show_login()

    def validate_email(self,s):
        idx_at = s.find("@")
        if idx_at == -1:
            return False
        return "." in s[idx_at+1:]
    
    def show_login(self):
        self.login = Login()
        self.login.show()
        self.close()
        
class Home(QMainWindow):
    def __init__(self,user_id):
        super().__init__()
        uic.loadUi("ui/Home.ui",self)

        self.user_id = user_id
        self.user = get_user_by_id(user_id)
        
        self.main_widget = self.findChild(QStackedWidget,"main_widget")
        self.main_widget.setCurrentIndex(0)

        self.btn_nav_home = self.findChild(QPushButton,"btn_nav_home")
        self.btn_nav_account = self.findChild(QPushButton,"btn_nav_account")
        self.btn_nav_menu = self.findChild(QPushButton,"btn_nav_menu")
        self.btn_detail = self.findChild(QPushButton,"btn_detail")
        self.avatar = self.findChild(QLabel,"avatar")
        self.btn_avatar = self.findChild(QPushButton,"btn_nav_avatar")
        self.btn_avatar.clicked.connect(self.update_avatar  )

        self.btn_nav_home.clicked.connect(lambda: self.navMainScreen(0))
        self.btn_nav_account.clicked.connect(lambda: self.navMainScreen(1))
        self.btn_nav_menu.clicked.connect(lambda: self.navMainScreen(2))
        self.btn_detail.clicked.connect(lambda: self.navMainScreen(3))
        
        self.loadAccountInfo()

    def navMainScreen(self,index):
        self.main_widget.setCurrentIndex(index)

    def loadAccountInfo(self):
        self.txt_name = self.findChild(QLineEdit,"txt_name")
        self.txt_email = self.findChild(QLineEdit,"txt_email")

        self.btn_nav_account.setText(self.user['name'])
        self.txt_name.setText(self.user['name'])
        self.txt_email.setText(self.user['email'])
        if not self.user_ == ["avatar"]:
            self.btn_avatar.setIcon(QIcon("avatar"))
            self.avatar.pixmap(QPixmap("avatar"))

    def update_avatar(self):
        file,_ = QFileDialog.getOpenFileName(self, "Select image", "", "Images Files(*.png *.jpg *.jpeg *.bmp)")
        if file:
            self.user["avatar"] = file
            self.btn_avatar.setIcon(QIcon(file))
            self.avatar.pixmap(QPixmap(file))    
            update_user_avatar(self.user_id, file)
            

if __name__ == "__main__":
    app = QApplication([])
    login = Login()
    login.show()
    app.exec()