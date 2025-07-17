from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
from database import *
from spoonacular_api import *
from utils import download_image
from PyQt6.QtCore import pyqtSignal, QThread

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
    
    def register(self,user_id):
        self.user_id = user_id
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
        gender = "Ofther"
        update_user_gender(self.user_id,gender)
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
    clicked = pyqtSignal(int)  # truyền id món ăn

    def __init__(self, id, name, img_url, healthScore, pricePerServing, cheap, veryHealthy, dairyFree, vegan, servings, tags):
        super().__init__()
        uic.loadUi("ui/item.ui", self)

        self.setFixedSize(355, 100)  # Set cố định cả chiều rộng và cao

        self.id = id
        self.name = name
        self.img_url = img_url
        self.healthScore = healthScore or 0
        self.pricePerServing = pricePerServing or 0
        self.cheap = cheap
        self.veryHealthy = veryHealthy
        self.vegan = vegan
        self.servings = servings
        self.dairyFree = dairyFree
        self.tags = tags or ""

        self.lb_img = self.findChild(QLabel, "lb_img")
        self.lb_name = self.findChild(QLabel, "lb_name")
        self.lb_pricePerServing = self.findChild(QLabel, "lb_pricePerServing")
        self.lb_healthScore = self.findChild(QLabel, "lb_healthScore")
        self.lb_tags = self.findChild(QLabel, "lb_tags")

        self.lb_name.setText(str(name))
        self.lb_healthScore.setText(f'🩺 {self.healthScore}')
        self.lb_pricePerServing.setText(f'💰 {self.pricePerServing}')
        
        # Chỉ hiển thị tag nếu có
        if self.tags and self.tags.strip():
            self.lb_tags.setText(self.tags)
            self.lb_tags.setStyleSheet("background:#e0f0ff; color:#0077b6; border-radius:8px; padding:2px 10px; margin-top:10px; font-weight:bold;")
        else:
            self.lb_tags.setText("")
            self.lb_tags.setStyleSheet("background:transparent; border:none;")

        # Load image
        pixmap = download_image(img_url)
        if pixmap:
            scaled_pixmap = pixmap.scaled(
                self.lb_img.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.lb_img.setPixmap(scaled_pixmap)
        else:
            self.lb_img.setText("No Image")
    
    def mousePressEvent(self, event):
        self.clicked.emit(self.id)
        super().mousePressEvent(event)

class IngredientItem(QWidget):
    def __init__(self, id, name, img, amount_info):
        super().__init__()
        uic.loadUi("ui/materials.ui", self)

        # Bỏ setFixedSize, chỉ set minimum/maximum để tránh bị giãn
        self.setMinimumWidth(200)
        self.setMaximumWidth(250)

        self.id = id
        self.name = name
        self.img = img
        self.amount_info = amount_info

        self.lb_ingredient_img = self.findChild(QLabel, "lb_ingredient_img")
        self.lb_ingredient_name = self.findChild(QLabel, "lb_ingredient_name")
        self.lb_ingredient_amount = self.findChild(QLabel, "lb_ingredient_amount")

        self.lb_ingredient_name.setText(name)
        self.lb_ingredient_amount.setText(amount_info)

        # Tạo URL đầy đủ từ tên file
        if img:
            if img.startswith('http'):
                # Đã là URL đầy đủ
                image_url = img
            else:
                # Tạo URL từ base URL của Spoonacular
                image_url = f"https://spoonacular.com/cdn/ingredients_100x100/{img}"
            
            # Load image từ URL
            pixmap = download_image(image_url)
            if pixmap:
                self.lb_ingredient_img.setPixmap(pixmap.scaled(
                    60, 60,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                ))
            else:
                self.lb_ingredient_img.setText("No Image")
        else:
            self.lb_ingredient_img.setText("No Image")
    
class FoodListLoader(QThread):
    result = pyqtSignal(dict)
    def run(self):
        food_list = get_random_recipes(number=10)
        self.result.emit(food_list)

class SearchRecipeWorker(QThread):
    result = pyqtSignal(dict)
    def __init__(self, query):
        super().__init__()
        self.query = query
    def run(self):
        food_list = search_recipe(self.query)
        print(f"SearchRecipeWorker result: {food_list}")  # Debug
        print(f"Keys in result: {list(food_list.keys())}")  # Debug
        if 'recipes' in food_list:
            print(f"Number of recipes: {len(food_list['recipes'])}")
        if 'results' in food_list:
            print(f"Number of results: {len(food_list['results'])}")
        self.result.emit(food_list)

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
        self.cb_gender.currentIndexChanged.connect(self.on_gender_changed)
        self.btn_search = self.findChild(QPushButton,"btn_search")
        self.txt_search = self.findChild(QLineEdit,"txt_search")
        self.btn_search.clicked.connect(self.search_recipe)

        self.main_widget = self.findChild(QStackedWidget,"main_widget")
        self.main_widget.setCurrentIndex(0)

        self.btn_del_account = self.findChild(QPushButton,"btn_del_account")
        self.btn_nav_home = self.findChild(QPushButton,"btn_nav_home")
        self.btn_nav_account = self.findChild(QPushButton,"btn_nav_account")
        self.btn_nav_menu = self.findChild(QPushButton,"btn_nav_menu")
        self.avatar = self.findChild(QLabel,"avatar")
        self.btn_avatar = self.findChild(QPushButton,"btn_avatar")
        self.btn_avatar.clicked.connect(self.update_avatar)

        self.btn_up_name = self.findChild(QPushButton,"btn_up_name")
        self.btn_up_name.clicked.connect(self.unlock_editing_name)

        self.btn_up_password = self.findChild(QPushButton,"btn_up_password")
        self.btn_up_password.clicked.connect(self.unlock_editing_password)
        
        # Lấy QWidget từ Designer để làm container cho danh sách món ăn
        self.food_container = self.findChild(QWidget, "food_list_container")
        self.food_layout = QVBoxLayout(self.food_container)
        self.food_layout.setSpacing(8)
        self.food_layout.setContentsMargins(0, 0, 0, 0)
        self.food_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.lw_food = self.findChild(QWidget, "lw_food")
        self.lw_food.setFixedSize(360, 340)
        self.lb_img_first_food = self.findChild(QLabel,"lb_img_first_food")
        self.lb_img_first_food.setFixedSize(320, 220)
        self.lb_img_first_food.setScaledContents(True)
        self.lb_name_first_food = self.findChild(QLabel,"lb_name_first_food")
        self.lb_name_first_food.setWordWrap(True)
        self.lb_name_first_food.setMaximumWidth(320)
        
        # Tìm các label khác cho first food
        self.lb_healthScore_first_food = self.findChild(QLabel,"lb_healthScore_first_food")
        self.lb_pricePerServing_first_food = self.findChild(QLabel,"lb_pricePerServing_first_food")
        self.lb_tags_first_food = self.findChild(QLabel,"lb_tags_first_food")
        self.lb_readyInMinutes_first_food = self.findChild(QLabel,"lb_readyInMinutes_first_food")
        self.lb_servings_first_food = self.findChild(QLabel,"lb_servings_first_food")
        self.lb_dishType_first_food = self.findChild(QLabel,"lb_dishType_first_food")

        if self.lw_food.layout():
            self.lw_food.layout().setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)

        self.btn_nav_home.clicked.connect(lambda: self.navMainScreen(0))
        self.btn_nav_account.clicked.connect(lambda: self.navMainScreen(1))
        self.btn_nav_menu.clicked.connect(lambda: self.navMainScreen(2))
        
        self.load_food_list()
        self.load_recipe_detail(1)

    def show_loading(self, message="Đang tải danh sách món ăn..."):
        """Hiển thị loading message"""
        # Clear existing items
        for i in reversed(range(self.food_layout.count())):
            widget = self.food_layout.itemAt(i).widget()
            if widget is not None:
                self.food_layout.removeWidget(widget)
                widget.setParent(None)
        
        loading_label = QLabel(message)
        loading_label.setStyleSheet("color: #888; font-size: 16px; padding: 20px;")
        self.food_layout.addWidget(loading_label)

    def clear_food_layout(self):
        """Xóa tất cả widget trong food_layout"""
        for i in reversed(range(self.food_layout.count())):
            widget = self.food_layout.itemAt(i).widget()
            if widget is not None:
                self.food_layout.removeWidget(widget)
                widget.setParent(None)

    def get_recipe_tags(self, recipe):
        """Lấy tags của recipe"""
        tags = []
        if recipe.get('cheap', False): tags.append('Cheap')
        if recipe.get('veryHealthy', False): tags.append('Very Healthy')
        if recipe.get('vegan', False): tags.append('Vegan')
        if recipe.get('vegetarian', False): tags.append('Vegetarian')
        if recipe.get('glutenFree', False): tags.append('Gluten Free')
        if recipe.get('dairyFree', False): tags.append('Dairy Free')
        return ', '.join(tags)

    def update_first_food_display(self, recipe):
        """Cập nhật hiển thị món ăn đầu tiên (ảnh lớn bên trái)"""
        # Lấy thông tin cơ bản
        title = recipe.get('title', '')
        image = recipe.get('image', '')
        healthScore = recipe.get('healthScore', '')
        pricePerServing = recipe.get('pricePerServing', '')
        readyInMinute = recipe.get('readyInMinutes', '')
        servings = recipe.get('servings', '')
        
        # Lấy tags
        tag_str = self.get_recipe_tags(recipe)
        
        # Lấy dish types
        dish_types = recipe.get('dishTypes', [])
        dish_type_str = ', '.join(dish_types) if dish_types else ''

        # Cập nhật ảnh
        pixmap = download_image(image)
        if pixmap:
            self.lb_img_first_food.setPixmap(pixmap.scaled(
                self.lb_img_first_food.size(), 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation
            ))
        else:
            self.lb_img_first_food.setText("No Image")

        # Cập nhật thông tin
        self.lb_name_first_food.setText(title)
        self.lb_healthScore_first_food.setText(f"🩺 {healthScore}")
        self.lb_pricePerServing_first_food.setText(f"💰 {pricePerServing}")
        
        # ⭐ FIX: Thêm word wrap cho tags
        self.lb_tags_first_food.setText(tag_str)
        self.lb_tags_first_food.setWordWrap(True)
        
        self.lb_readyInMinutes_first_food.setText(f"⏱ {readyInMinute} phút")
        self.lb_servings_first_food.setText(f"👤 {servings} khẩu phần")
        
        # ⭐ FIX: Thêm word wrap cho dish types
        if hasattr(self, 'lb_dishType_first_food') and self.lb_dishType_first_food:
            self.lb_dishType_first_food.setText(dish_type_str)
            self.lb_dishType_first_food.setWordWrap(True)

    def populate_food_list(self, recipes):
        """Điền danh sách món ăn vào layout"""
        for recipe in recipes:
            # Lấy tags
            tag_str = self.get_recipe_tags(recipe)
            
            # Tạo FoodItem widget
            food_widget = FoodItem(
                recipe['id'], 
                recipe['title'], 
                recipe['image'], 
                recipe.get("healthScore", 0), 
                recipe.get("pricePerServing", 0), 
                recipe.get("cheap", False), 
                recipe.get("veryHealthy", False), 
                recipe.get("dairyFree", False), 
                recipe.get("vegan", False), 
                recipe.get("servings", 0), 
                tag_str
            )
            food_widget.clicked.connect(self.on_food_item_clicked)
            self.food_layout.addWidget(food_widget)

    def handle_food_list_data(self, food_list):
        """Xử lý dữ liệu danh sách món ăn chung cho cả load và search"""
        print(f"Received data keys: {list(food_list.keys())}")  # Debug
        
        # Clear loading
        self.clear_food_layout()

        # ⭐ KEY FIX: Xử lý cả 'recipes' và 'results'
        recipes = []
        if 'recipes' in food_list and food_list['recipes']:
            recipes = food_list['recipes']
        elif 'results' in food_list and food_list['results']:  # Cho search_recipe
            recipes = food_list['results']
        
        print(f"Number of recipes to display: {len(recipes)}")  # Debug

        if recipes:
            # Cập nhật món ăn đầu tiên (ảnh lớn bên trái)
            self.update_first_food_display(recipes[0])

            # Điền danh sách món ăn (bên phải)
            self.populate_food_list(recipes)
        else:
            # Hiển thị thông báo không có kết quả
            no_result_label = QLabel("Không tìm thấy món ăn nào")
            no_result_label.setStyleSheet("color: #888; font-size: 16px; padding: 20px;")
            self.food_layout.addWidget(no_result_label)

    def load_food_list(self):
        """Load danh sách món ăn ngẫu nhiên"""
        self.show_loading("Đang tải danh sách món ăn...")
        
        self.loader = FoodListLoader()
        self.loader.result.connect(self.handle_food_list_data)
        self.loader.start()

    def search_recipe(self):
        """Tìm kiếm món ăn"""
        query = self.txt_search.text().strip()
        if not query:
            return
        
        self.show_loading("Đang tìm kiếm món ăn...")
        
        self.search_worker = SearchRecipeWorker(query)
        self.search_worker.result.connect(self.handle_food_list_data)
        self.search_worker.start()

    def unlock_editing_name(self):
        self.txt_name.setReadOnly(False)
        self.txt_name.setFocus()
        self.txt_name.selectAll()

    def finish_editing_name(self):
        new_name = self.txt_name.text()
        self.btn_nav_account.setText(new_name)
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

    def navMainScreen(self, index):
        self.main_widget.setCurrentIndex(index)

    def on_food_item_clicked(self, recipe_id):
        self.load_recipe_detail(recipe_id)
        self.main_widget.setCurrentIndex(3)

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
            
    def on_gender_changed(self, index):
        gender_text = self.cb_gender.currentText()
        if gender_text.strip() in ["", "---", "Chọn giới tính"]:
            return
        update_user_gender(self.user_id, gender_text)
        self.msg.success_box("Đã cập nhật giới tính")

    def load_recipe_detail(self, recipe_id):
        """Load thông tin chi tiết món ăn"""
        try:
            # Lấy thông tin chi tiết từ API
            recipe_detail = get_recipe_details(recipe_id)
            
            # Clear container
            detail_container = self.findChild(QWidget, "detail_container")
            detail_layout = detail_container.layout()
            
            # Xóa các widget cũ
            for i in reversed(range(detail_layout.count())):
                widget = detail_layout.itemAt(i).widget()
                if widget is not None:
                    detail_layout.removeWidget(widget)
                    widget.setParent(None)
            
            # 1. Phần thông tin cơ bản
            basic_info = self.create_basic_info_widget(recipe_detail)
            detail_layout.addWidget(basic_info)
            
            # 2. Phần nguyên liệu
            ingredients_widget = self.create_ingredients_widget(recipe_detail)
            detail_layout.addWidget(ingredients_widget)
            
            # 3. Phần mô tả
            description_widget = self.create_description_widget(recipe_detail)
            detail_layout.addWidget(description_widget)
            
        except Exception as e:
            print(f"Error loading recipe detail: {e}")
            import traceback
            traceback.print_exc()

    def create_basic_info_widget(self, recipe):
        """Tạo widget hiển thị thông tin cơ bản"""
        widget = QWidget()
        widget.setStyleSheet("background:#fff; border-radius:15px; padding:20px;")
        layout = QVBoxLayout(widget)
        
        # Ảnh món ăn
        img_label = QLabel()
        img_label.setMinimumSize(400, 250)
        img_label.setMaximumSize(400, 250)
        img_label.setScaledContents(True)
        img_label.setStyleSheet("border-radius:10px;")
        
        pixmap = download_image(recipe.get('image', ''))
        if pixmap:
            img_label.setPixmap(pixmap.scaled(
                400, 250, 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation
            ))
        else:
            img_label.setText("No Image")
        
        layout.addWidget(img_label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Tên món ăn
        title_label = QLabel(recipe.get('title', ''))
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title_label.setStyleSheet("color:#222; margin:10px 0;")
        title_label.setWordWrap(True)
        layout.addWidget(title_label)
        
        # Thông số (health score, price, tags)
        info_layout = QHBoxLayout()
        
        health_score = QLabel(f"🩺 {recipe.get('healthScore', 0)}")
        health_score.setStyleSheet("color:green; font-weight:bold; font-size:14px;")
        info_layout.addWidget(health_score)
        
        price = QLabel(f"💰 {recipe.get('pricePerServing', 0)}")
        price.setStyleSheet("color:orange; font-weight:bold; font-size:14px; margin-left:20px;")
        info_layout.addWidget(price)
        
        # Tags
        tags = self.get_recipe_tags(recipe)
        if tags:
            tags_label = QLabel(tags)
            tags_label.setStyleSheet("color:#0077b6; font-weight:bold; font-size:14px; margin-left:20px;")
            info_layout.addWidget(tags_label)
        
        info_layout.addStretch()
        layout.addLayout(info_layout)
        
        # Thời gian và khẩu phần
        time_servings = QHBoxLayout()
        ready_time = QLabel(f"⏱ {recipe.get('readyInMinutes', 0)} phút")
        ready_time.setStyleSheet("color:#555; font-size:12px;")
        time_servings.addWidget(ready_time)
        
        servings = QLabel(f"👤 {recipe.get('servings', 0)} khẩu phần")
        servings.setStyleSheet("color:#555; font-size:12px; margin-left:20px;")
        time_servings.addWidget(servings)
        
        # Thêm thông tin aggregateLikes và spoonacularScore
        likes = QLabel(f"👍 {recipe.get('aggregateLikes', 0)}")
        likes.setStyleSheet("color:#555; font-size:12px; margin-left:20px;")
        time_servings.addWidget(likes)
        
        score = QLabel(f"⭐ {recipe.get('spoonacularScore', 0):.1f}")
        score.setStyleSheet("color:#555; font-size:12px; margin-left:20px;")
        time_servings.addWidget(score)
        
        time_servings.addStretch()
        layout.addLayout(time_servings)
        
        # Thông tin cuisines và dishTypes
        if recipe.get('cuisines') or recipe.get('dishTypes'):
            cuisine_layout = QHBoxLayout()
            
            if recipe.get('cuisines'):
                cuisines_label = QLabel(f"🍽️ {', '.join(recipe['cuisines'])}")
                cuisines_label.setStyleSheet("color:#666; font-size:11px;")
                cuisine_layout.addWidget(cuisines_label)
            
            if recipe.get('dishTypes'):
                dish_types_label = QLabel(f"🍴 {', '.join(recipe['dishTypes'])}")
                dish_types_label.setStyleSheet("color:#666; font-size:11px; margin-left:20px;")
                cuisine_layout.addWidget(dish_types_label)
            
            cuisine_layout.addStretch()
            layout.addLayout(cuisine_layout)
        
        # Summary (mô tả ngắn)
        if recipe.get('summary'):
            summary_label = QLabel()
            summary_label.setText(recipe['summary'].replace('<b>', '').replace('</b>', '').replace('<a href=', '').replace('</a>', ''))
            summary_label.setWordWrap(True)
            summary_label.setStyleSheet("color:#333; font-size:12px; line-height:1.4; margin-top:10px; padding:10px; background:#f8f9fa; border-radius:8px;")
            layout.addWidget(summary_label)
        
        return widget

    def create_ingredients_widget(self, recipe):
        """Tạo widget hiển thị nguyên liệu"""
        widget = QWidget()
        widget.setStyleSheet("background:#fff; border-radius:15px; padding:20px;")
        layout = QVBoxLayout(widget)
        
        # Tiêu đề
        title = QLabel("Nguyên liệu")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setStyleSheet("color:#222; margin-bottom:15px;")
        layout.addWidget(title)
        
        # Danh sách nguyên liệu - 1 dòng 2 item, tự động dài ra
        ingredients_layout = QGridLayout()
        ingredients_layout.setSpacing(5)
        
        ingredients = recipe.get('extendedIngredients', [])
        
        for i, ingredient in enumerate(ingredients):
            # Lấy thông tin từ US measures
            us_measures = ingredient.get('measures', {}).get('us', {})
            amount = us_measures.get('amount', ingredient.get('amount', 0))
            unit_long = us_measures.get('unitLong', ingredient.get('unit', ''))
            
            # Tạo chuỗi hiển thị
            amount_display = f"{amount} {unit_long}".strip()
            if not amount_display:
                amount_display = ingredient.get('original', '')
            
            ingredient_widget = IngredientItem(
                ingredient.get('id', 0),
                ingredient.get('name', ''),
                ingredient.get('image', ''),
                amount_display
            )
            
            # Thêm vào grid: row = i//2, col = i%2
            row = i // 2
            col = i % 2
            ingredients_layout.addWidget(ingredient_widget, row, col)
        
        layout.addLayout(ingredients_layout)
        return widget

    def create_description_widget(self, recipe):
        """Tạo widget hiển thị mô tả"""
        widget = QWidget()
        widget.setStyleSheet("background:#fff; border-radius:15px; padding:20px;")
        layout = QVBoxLayout(widget)
        
        # Tiêu đề
        title = QLabel("Hướng dẫn")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setStyleSheet("color:#222; margin-bottom:15px;")
        layout.addWidget(title)
        
        # Mô tả
        description = QLabel(recipe.get('instructions', 'Không có hướng dẫn'))
        description.setWordWrap(True)
        description.setStyleSheet("color:#333; line-height:1.6; font-size:14px;")
        layout.addWidget(description)
        
        return widget

if __name__ == "__main__":
    app = QApplication([])
    login = Login()
    login = Home(10)
    login.show()
    app.exec()