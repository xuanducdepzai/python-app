from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
from database import *
from spoonacular_api import *
from utils import download_image

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
        
        if len(password) < 6:
            msg.error_box("Mật khẩu phải có tối thiểu 6 ký tự")
            self.password.setFocus()
            return

        if len(password) > 14:
            msg.error_box("Mật khẩu chỉ có tối đa 14 ký tự")
            self.password.setFocus()
            return

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

# Updated FoodItem class
class FoodItem(QWidget):
    def __init__(self, id, name, img_url, rating):
        super().__init__()
        uic.loadUi("ui/item.ui", self)

        self.id = id
        self.name = name
        self.img_url = img_url
        self.rating = rating
        
        self.setMinimumSize(371, 121)

        self.lb_img = self.findChild(QLabel, "lb_img")
        self.lb_name = self.findChild(QLabel, "lb_name")

        self.lb_name.setText(name)
        
        # Load image
        pixmap = download_image(img_url)
        if pixmap:
            # Scale image to fit
            scaled_pixmap = pixmap.scaled(
                self.lb_img.size(), 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation
            )
            self.lb_img.setPixmap(scaled_pixmap)
        else:
            self.lb_img.setText("No Image")
        
class IngredientItem(QWidget):
    def __init__(self, id, name, img, description):
        super().__init__()
        uic.loadUi("ui/nguyen_lieu.ui",self)

        self.id = id
        self.name = name
        self.img = img
        self.description = description


        self.lb_img = self.findChild(QLabel,"lb_img")
        self.lb_name = self.findChild(QLabel,"lb_name")
        self.lb_description = self.findChild(QLabel,"lb_description")

        self.lb_name.setText(name)
        self.lb_description.setText(description)

        self.lb_img.setPixmap(QPixmap(img))
    
class Home(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        uic.loadUi("ui/Home.ui",self)

        self.user_id = user_id
        self.msg = Messagebox()
        
        self.user = get_user_by_id(user_id)
        self.loadAccountInfo()

        self.txt_name = self.findChild(QLineEdit,"txt_name")
        self.txt_name.returnPressed.connect(self.finish_editing_name)
        self.txt_email = self.findChild(QLineEdit,"txt_email")
        self.txt_password = self.findChild(QLineEdit,"txt_password")
        self.txt_password.returnPressed.connect(self.finish_editing_password)
        self.cb_gender = self.findChild(QComboBox,"cb_gender")

        self.main_widget = self.findChild(QStackedWidget,"main_widget")
        self.main_widget.setCurrentIndex(0)

        self.btn_del_account = self.findChild(QPushButton,"btn_del_account")
#        self.btn_del_account.clicked.connect(self.update_avatar )
        self.btn_nav_home = self.findChild(QPushButton,"btn_nav_home")
        self.btn_nav_account = self.findChild(QPushButton,"btn_nav_account")
        self.btn_nav_menu = self.findChild(QPushButton,"btn_nav_menu")
        self.avatar = self.findChild(QLabel,"avatar")
        self.btn_avatar = self.findChild(QPushButton,"btn_avatar")
        self.btn_avatar.clicked.connect(self.update_avatar )

        self.btn_up_name = self.findChild(QPushButton,"btn_up_name")
        self.btn_up_name.clicked.connect(self.unlock_editing_name)

        self.btn_up_password = self.findChild(QPushButton,"btn_up_password")
        self.btn_up_password.clicked.connect(self.unlock_editing_password)
        
        self.lw_food = self.findChild(QListWidget,"lw_food")
        self.lb_img_first_food = self.findChild(QLabel,"lb_img_first_food")
        self.lb_name_first_food = self.findChild(QLabel,"lb_name_first_food")

        self.btn_nav_home.clicked.connect(lambda: self.navMainScreen(0))
        self.btn_nav_account.clicked.connect(lambda: self.navMainScreen(1))
        self.btn_nav_menu.clicked.connect(lambda: self.navMainScreen(2))
        self.load_food_list()
    
#    def delete_account(self):
#        delete_account(self.user_id,id)
        
    def unlock_editing_name(self):
        self.txt_name.setReadOnly(False)
        self.txt_name.setFocus()
        self.txt_name.selectAll()

    def finish_editing_name(self):
        new_name = self.txt_name.text()
        self.txt_name.setReadOnly(True)
        self.msg.success_box("Đã sửa thành công tên")
        update_user_name(self.user_id,new_name)
    
    def unlock_editing_password(self):
        self.txt_password.setReadOnly(False)
        self.txt_password.setFocus()
        self.txt_password.selectAll()

    def finish_editing_password(self):
        new_password = self.txt_password.text()
        self.txt_password.setReadOnly(True)
        self.msg.success_box("Đã sửa thành công mật khẩu")
        update_user_password(self.user_id,new_password)

    def navMainScreen(self,index):
        self.main_widget.setCurrentIndex(index)

    def loadAccountInfo(self):
        self.txt_name = self.findChild(QLineEdit,"txt_name")
        self.txt_email = self.findChild(QLineEdit,"txt_email")
        self.txt_password = self.findChild(QLineEdit,"txt_password")
        self.btn_nav_account = self.findChild(QPushButton,"btn_nav_account")

        self.btn_nav_account.setText(self.user["name"])
        self.txt_name.setText(self.user['name'])
        self.txt_password.setText(self.user['password'])
        self.txt_email.setText(self.user['email'])
        
        if self.user["avatar"]:
            self.btn_avatar.setIcon(QIcon(self.user["avatar"]))
            self.btn_avatar.setIconSize(self.btn_avatar.size())
            self.avatar.setPixmap(QPixmap(self.user["avatar"]))
            self.avatar.setScaledContents(True)

        if not self.user["gender"]:
            self.cb_gender.setCurrentIndex(3)
        elif self.user["gender"] == "Male":
            self.cb_gender.setCurrentIndex(1)
        elif self.user["gender"] == "Female":
            self.cb_gender.setCurrentIndex(2)
        else:
            self.cb_gender.setCurrentIndex(3)
        
    def update_avatar(self):
        file,_ = QFileDialog.getOpenFileName(self, "Select image", "", "Images Files(*.png *.jpg *.jpeg *.bmp)")
        if file:
            self.user["avatar"] = file
            self.btn_avatar.setIcon(QIcon(file))
            self.avatar.setPixmap(QPixmap(file))    
            update_user_avatar(self.user_id, file)
            

    def load_food_list(self):
        # Load multiple recipes
        food_list = get_random_recipes(number=10)
        
        # Clear existing items
        self.lw_food.clear()
        
        # Enable scrolling explicitly
        self.lw_food.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.lw_food.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        if 'recipes' in food_list and food_list['recipes']:
            recipes = food_list['recipes']
            
            # Set FIRST recipe on the RIGHT side
            first_recipe = recipes[0]
            pixmap = download_image(first_recipe['image'])
            if pixmap:
                # Make sure the main image label has size
                if self.lb_img_first_food.width() == 0:
                    self.lb_img_first_food.setMinimumSize(300, 200)
                    
                scaled_pixmap = pixmap.scaled(
                    self.lb_img_first_food.size(), 
                    Qt.AspectRatioMode.KeepAspectRatio, 
                    Qt.TransformationMode.SmoothTransformation
                )
                self.lb_img_first_food.setPixmap(scaled_pixmap)
            self.lb_name_first_food.setText(first_recipe['title'])
            readyInMinute = first_recipe['readyInMinutes']
            
            # Add ALL recipes to LEFT list
            for recipe in recipes:
                # Create QListWidgetItem
                item = QListWidgetItem()
                
                # Create FoodItem widget
                food_widget = FoodItem(recipe['id'], recipe['title'], recipe['image'], "test")
                
                # Set the item size to match widget size
                item.setSizeHint(QSize(371, 121))  # Use QSize explicitly
                
                # Add to list
                self.lw_food.addItem(item)
                self.lw_food.setItemWidget(item, food_widget)
                readyInMinute = recipe['readyInMinutes']
            
            print(f"Added {len(recipes)} recipes to list")  # Debug print

if __name__ == "__main__":
    app = QApplication([])
    login = Login()
    login = Home(1)
    login.show()
    app.exec()