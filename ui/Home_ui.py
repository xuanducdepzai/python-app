# Form implementation generated from reading ui file '/Users/pinxun/Documents/MindX/PTA/PTA08/XuanDuc/python-app/ui/Home.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 505)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_widget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.main_widget.setGeometry(QtCore.QRect(-20, 70, 811, 461))
        self.main_widget.setMaximumSize(QtCore.QSize(1080, 760))
        self.main_widget.setObjectName("main_widget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.btn_nav_menu = QtWidgets.QPushButton(parent=self.home)
        self.btn_nav_menu.setGeometry(QtCore.QRect(360, 260, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.btn_nav_menu.setFont(font)
        self.btn_nav_menu.setStyleSheet("border: 2px solid white;\n"
"border-radius:15px;\n"
"color:rgb(255, 255, 255);\n"
"")
        self.btn_nav_menu.setObjectName("btn_nav_menu")
        self.label_4 = QtWidgets.QLabel(parent=self.home)
        self.label_4.setGeometry(QtCore.QRect(20, 0, 781, 451))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/XuanDuc/python-app/ui/../img/3.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(parent=self.home)
        self.label_3.setGeometry(QtCore.QRect(250, 220, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(19)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 600 19pt \"Segoe UI\";")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(parent=self.home)
        self.label_2.setGeometry(QtCore.QRect(270, 180, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(34)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 900 34pt \"Segoe UI\";")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=self.home)
        self.label.setGeometry(QtCore.QRect(290, 130, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 900 32pt \"Segoe UI\";")
        self.label.setObjectName("label")
        self.lb_servings_first_food = QtWidgets.QLabel(parent=self.home)
        self.lb_servings_first_food.setGeometry(QtCore.QRect(40, 360, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lb_servings_first_food.setFont(font)
        self.lb_servings_first_food.setStyleSheet("color:#555; font-size:11px;")
        self.lb_servings_first_food.setText("")
        self.lb_servings_first_food.setObjectName("lb_servings_first_food")
        self.lb_servings_first_food.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.btn_nav_menu.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.main_widget.addWidget(self.home)
        self.account = QtWidgets.QWidget()
        self.account.setObjectName("account")
        self.label_10 = QtWidgets.QLabel(parent=self.account)
        self.label_10.setGeometry(QtCore.QRect(10, 0, 791, 461))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background:rgb(212, 229, 236)")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.account)
        self.label_11.setGeometry(QtCore.QRect(250, 10, 581, 401))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(32)
        sizePolicy.setVerticalStretch(31)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setStyleSheet("background:rgb(133, 167, 212);\n"
"border-radius:15px;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.btn_up_name = QtWidgets.QPushButton(parent=self.account)
        self.btn_up_name.setGeometry(QtCore.QRect(740, 70, 51, 51))
        self.btn_up_name.setStyleSheet("background: none;\n"
"border:none")
        self.btn_up_name.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/XuanDuc/python-app/ui/../img/56.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_up_name.setIcon(icon)
        self.btn_up_name.setIconSize(QtCore.QSize(38, 48))
        self.btn_up_name.setObjectName("btn_up_name")
        self.btn_avatar = QtWidgets.QPushButton(parent=self.account)
        self.btn_avatar.setGeometry(QtCore.QRect(250, 10, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_avatar.setFont(font)
        self.btn_avatar.setStyleSheet("color:rgb(0, 0, 0);\n"
"background: none;\n"
"border: none;")
        self.btn_avatar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/XuanDuc/python-app/ui/../img/38.webp"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_avatar.setIcon(icon1)
        self.btn_avatar.setIconSize(QtCore.QSize(190, 190))
        self.btn_avatar.setObjectName("btn_avatar")
        self.txt_name = QtWidgets.QLineEdit(parent=self.account)
        self.txt_name.setGeometry(QtCore.QRect(410, 70, 381, 52))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.txt_name.setFont(font)
        self.txt_name.setStyleSheet("border-color : rgb(0, 0, 0);\n"
"border: 2px solid back;\n"
"    border-radius: 10px; /* Rounded corners */\n"
"   background-color: rgb(165, 185, 218);\n"
"    padding: 10px\n"
"")
        self.txt_name.setReadOnly(True)
        self.txt_name.setObjectName("txt_name")
        self.txt_email = QtWidgets.QLineEdit(parent=self.account)
        self.txt_email.setGeometry(QtCore.QRect(290, 350, 501, 52))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        self.txt_email.setFont(font)
        self.txt_email.setStyleSheet("border-color : rgb(0, 0, 0);\n"
"border: 2px solid back;\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    background-color: rgb(165, 185, 218);\n"
"    padding: 10px\n"
"")
        self.txt_email.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.txt_email.setReadOnly(True)
        self.txt_email.setObjectName("txt_email")
        self.label_12 = QtWidgets.QLabel(parent=self.account)
        self.label_12.setGeometry(QtCore.QRect(420, 40, 49, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_22 = QtWidgets.QLabel(parent=self.account)
        self.label_22.setGeometry(QtCore.QRect(540, 450, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_35 = QtWidgets.QLabel(parent=self.account)
        self.label_35.setGeometry(QtCore.QRect(300, 320, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.txt_password = QtWidgets.QLineEdit(parent=self.account)
        self.txt_password.setGeometry(QtCore.QRect(290, 260, 501, 52))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        self.txt_password.setFont(font)
        self.txt_password.setStyleSheet("border-color : rgb(0, 0, 0);\n"
"border: 2px solid back;\n"
"    border-radius: 10px; /* Rounded corners */\n"
"   background-color: rgb(165, 185, 218);\n"
"    padding: 10px\n"
"")
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.txt_password.setReadOnly(True)
        self.txt_password.setObjectName("txt_password")
        self.label_36 = QtWidgets.QLabel(parent=self.account)
        self.label_36.setGeometry(QtCore.QRect(300, 230, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.btn_up_password = QtWidgets.QPushButton(parent=self.account)
        self.btn_up_password.setGeometry(QtCore.QRect(740, 260, 51, 51))
        self.btn_up_password.setStyleSheet("background: none;\n"
"border:none")
        self.btn_up_password.setText("")
        self.btn_up_password.setIcon(icon)
        self.btn_up_password.setIconSize(QtCore.QSize(38, 48))
        self.btn_up_password.setObjectName("btn_up_password")
        self.label_38 = QtWidgets.QLabel(parent=self.account)
        self.label_38.setGeometry(QtCore.QRect(10, 10, 161, 401))
        self.label_38.setStyleSheet("background:rgb(133, 167, 212);\n"
"border-radius:15px;")
        self.label_38.setText("")
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(parent=self.account)
        self.label_39.setGeometry(QtCore.QRect(300, 150, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.cb_gender = QtWidgets.QComboBox(parent=self.account)
        self.cb_gender.setGeometry(QtCore.QRect(290, 180, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.cb_gender.setFont(font)
        self.cb_gender.setStyleSheet("border-color : rgb(0, 0, 0);\n"
"border: 2px solid back;\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    background-color: rgb(165, 185, 218);\n"
"    padding: 10px\n"
"")
        self.cb_gender.setObjectName("cb_gender")
        self.cb_gender.addItem("")
        self.cb_gender.addItem("")
        self.cb_gender.addItem("")
        self.pushButton = QtWidgets.QPushButton(parent=self.account)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 151, 71))
        self.pushButton.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.pushButton.setStyleSheet("background: none;\n"
"font: 900 18pt \"Segoe UI\";\n"
"border: none")
        self.pushButton.setObjectName("pushButton")
        self.label_10.raise_()
        self.label_38.raise_()
        self.label_11.raise_()
        self.txt_name.raise_()
        self.btn_up_name.raise_()
        self.btn_avatar.raise_()
        self.txt_email.raise_()
        self.label_12.raise_()
        self.label_22.raise_()
        self.label_35.raise_()
        self.txt_password.raise_()
        self.label_36.raise_()
        self.btn_up_password.raise_()
        self.label_39.raise_()
        self.cb_gender.raise_()
        self.pushButton.raise_()
        self.main_widget.addWidget(self.account)
        self.menu = QtWidgets.QWidget()
        self.menu.setStyleSheet("background:rgb(212, 229, 236); border:none;")
        self.menu.setObjectName("menu")
        self.menuMainLayout = QtWidgets.QHBoxLayout(self.menu)
        self.menuMainLayout.setProperty("margin", 18)
        self.menuMainLayout.setContentsMargins(18, 18, 18, 18)
        self.menuMainLayout.setSpacing(18)
        self.menuMainLayout.setObjectName("menuMainLayout")
        self.lw_food = QtWidgets.QWidget(parent=self.menu)
        self.lw_food.setObjectName("lw_food")
        self.menuLeftLayout = QtWidgets.QVBoxLayout(self.lw_food)
        self.menuLeftLayout.setProperty("margin", 12)
        self.menuLeftLayout.setContentsMargins(12, 12, 12, 12)
        self.menuLeftLayout.setSpacing(10)
        self.menuLeftLayout.setObjectName("menuLeftLayout")
        self.lb_img_first_food = QtWidgets.QLabel(parent=self.lw_food)
        self.lb_img_first_food.setMinimumSize(QtCore.QSize(320, 220))
        self.lb_img_first_food.setStyleSheet("border-radius:18px; background:#fff; padding:12px;")
        self.lb_img_first_food.setScaledContents(True)
        self.lb_img_first_food.setObjectName("lb_img_first_food")
        self.menuLeftLayout.addWidget(self.lb_img_first_food)
        self.lb_name_first_food = QtWidgets.QLabel(parent=self.lw_food)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.lb_name_first_food.setFont(font)
        self.lb_name_first_food.setStyleSheet("color:#222; margin-top:12px; margin-bottom:8px; padding-left:4px;")
        self.lb_name_first_food.setObjectName("lb_name_first_food")
        self.menuLeftLayout.addWidget(self.lb_name_first_food)
        self.menuInfoRow1 = QtWidgets.QHBoxLayout()
        self.menuInfoRow1.setObjectName("menuInfoRow1")
        self.lb_healthScore_first_food = QtWidgets.QLabel(parent=self.lw_food)
        self.lb_healthScore_first_food.setStyleSheet("color:green; font-weight:bold; padding-left:4px;")
        self.lb_healthScore_first_food.setObjectName("lb_healthScore_first_food")
        self.menuInfoRow1.addWidget(self.lb_healthScore_first_food)
        self.lb_pricePerServing_first_food = QtWidgets.QLabel(parent=self.lw_food)
        self.lb_pricePerServing_first_food.setStyleSheet("color:orange; font-weight:bold; padding-left:4px;")
        self.lb_pricePerServing_first_food.setObjectName("lb_pricePerServing_first_food")
        self.menuInfoRow1.addWidget(self.lb_pricePerServing_first_food)
        self.lb_tags_first_food = QtWidgets.QLabel(parent=self.lw_food)
        self.lb_tags_first_food.setStyleSheet("background:#e0f0ff; color:#0077b6; border-radius:8px; padding:2px 10px; margin-left:8px; font-weight:bold;")
        self.lb_tags_first_food.setObjectName("lb_tags_first_food")
        self.menuInfoRow1.addWidget(self.lb_tags_first_food)
        self.menuLeftLayout.addLayout(self.menuInfoRow1)
        self.menuInfoRow2 = QtWidgets.QHBoxLayout()
        self.menuInfoRow2.setObjectName("menuInfoRow2")
        self.lb_readyInMinutes_first_food = QtWidgets.QLabel(parent=self.lw_food)
        self.lb_readyInMinutes_first_food.setStyleSheet("color:#555; font-size:11px; padding-left:4px;")
        self.lb_readyInMinutes_first_food.setObjectName("lb_readyInMinutes_first_food")
        self.menuInfoRow2.addWidget(self.lb_readyInMinutes_first_food)
        self.lb_dishType_first_food = QtWidgets.QLabel(parent=self.lw_food)
        self.lb_dishType_first_food.setStyleSheet("color:#555; font-size:11px; font-style:italic; padding-left:4px;")
        self.lb_dishType_first_food.setObjectName("lb_dishType_first_food")
        self.menuInfoRow2.addWidget(self.lb_dishType_first_food)
        self.menuLeftLayout.addLayout(self.menuInfoRow2)
        self.menuMainLayout.addWidget(self.lw_food)
        self.food_scroll_area = QtWidgets.QScrollArea(parent=self.menu)
        self.food_scroll_area.setWidgetResizable(True)
        self.food_scroll_area.setObjectName("food_scroll_area")
        self.food_list_container = QtWidgets.QWidget()
        self.food_list_container.setGeometry(QtCore.QRect(0, 0, 413, 425))
        self.food_list_container.setMinimumSize(QtCore.QSize(250, 400))
        self.food_list_container.setStyleSheet("background:transparent;")
        self.food_list_container.setObjectName("food_list_container")
        self.food_scroll_area.setWidget(self.food_list_container)
        self.menuMainLayout.addWidget(self.food_scroll_area)
        self.main_widget.addWidget(self.menu)
        self.detail = QtWidgets.QWidget()
        self.detail.setStyleSheet("background:rgb(212, 229, 236);")
        self.detail.setObjectName("detail")
        self.detailLayout = QtWidgets.QVBoxLayout(self.detail)
        self.detailLayout.setProperty("margin", 18)
        self.detailLayout.setContentsMargins(18, 18, 18, 18)
        self.detailLayout.setSpacing(18)
        self.detailLayout.setObjectName("detailLayout")
        self.detail_scroll_area = QtWidgets.QScrollArea(parent=self.detail)
        self.detail_scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.detail_scroll_area.setWidgetResizable(True)
        self.detail_scroll_area.setObjectName("detail_scroll_area")
        self.detail_container = QtWidgets.QWidget()
        self.detail_container.setGeometry(QtCore.QRect(0, 0, 773, 423))
        self.detail_container.setStyleSheet("background:transparent;")
        self.detail_container.setObjectName("detail_container")
        self.detail_container_layout = QtWidgets.QVBoxLayout(self.detail_container)
        self.detail_container_layout.setSpacing(20)
        self.detail_container_layout.setObjectName("detail_container_layout")
        self.detail_scroll_area.setWidget(self.detail_container)
        self.detailLayout.addWidget(self.detail_scroll_area)
        self.main_widget.addWidget(self.detail)
        self.btn_nav_account = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_nav_account.setGeometry(QtCore.QRect(530, 10, 191, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_nav_account.sizePolicy().hasHeightForWidth())
        self.btn_nav_account.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.btn_nav_account.setFont(font)
        self.btn_nav_account.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btn_nav_account.setStyleSheet("color:rgb(0, 0, 0);\n"
"background: none;\n"
"border: none;")
        self.btn_nav_account.setIconSize(QtCore.QSize(40, 40))
        self.btn_nav_account.setObjectName("btn_nav_account")
        self.btn_search = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(390, 20, 41, 41))
        self.btn_search.setStyleSheet("background:orange;\n"
"border: 2px solid back;\n"
"  border-radius: 10px; \n"
"")
        self.btn_search.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/XuanDuc/python-app/ui/../img/30.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_search.setIcon(icon2)
        self.btn_search.setIconSize(QtCore.QSize(32, 32))
        self.btn_search.setObjectName("btn_search")
        self.txt_search = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_search.setGeometry(QtCore.QRect(130, 20, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        self.txt_search.setFont(font)
        self.txt_search.setStyleSheet("border-color : rgb(0, 0, 0);\n"
"border: 2px solid back;\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    background-color: rgba(255, 255, 255, 0.1); /* Transparent-like background */\n"
"    padding: 10px\n"
"")
        self.txt_search.setText("")
        self.txt_search.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.txt_search.setObjectName("txt_search")
        self.btn_nav_home = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_nav_home.setGeometry(QtCore.QRect(70, 20, 41, 41))
        self.btn_nav_home.setStyleSheet("background:rgb(255, 255, 255);\n"
"border-radius:10px")
        self.btn_nav_home.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/XuanDuc/python-app/ui/../img/46.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_nav_home.setIcon(icon3)
        self.btn_nav_home.setIconSize(QtCore.QSize(32, 32))
        self.btn_nav_home.setObjectName("btn_nav_home")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(-90, -10, 991, 81))
        self.label_8.setMaximumSize(QtCore.QSize(1080, 700))
        self.label_8.setStyleSheet("background:rgb(255, 255, 255)")
        self.label_8.setText("")
        self.label_8.setScaledContents(False)
        self.label_8.setObjectName("label_8")
        self.label_63 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_63.setGeometry(QtCore.QRect(60, -20, 671, 91))
        self.label_63.setStyleSheet("background:rgb(184, 217, 232);\n"
"border-radius:15px;")
        self.label_63.setText("")
        self.label_63.setObjectName("label_63")
        self.avatar = QtWidgets.QLabel(parent=self.centralwidget)
        self.avatar.setGeometry(QtCore.QRect(430, 10, 101, 61))
        self.avatar.setText("")
        self.avatar.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/XuanDuc/python-app/ui/../img/38.webp"))
        self.avatar.setScaledContents(True)
        self.avatar.setObjectName("avatar")
        self.label_37 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(-42, -45, 921, 161))
        self.label_37.setStyleSheet("background:rgb(212, 229, 236);")
        self.label_37.setText("")
        self.label_37.setObjectName("label_37")
        self.label_8.raise_()
        self.label_37.raise_()
        self.label_63.raise_()
        self.main_widget.raise_()
        self.btn_nav_account.raise_()
        self.txt_search.raise_()
        self.btn_nav_home.raise_()
        self.btn_search.raise_()
        self.avatar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.main_widget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_nav_menu.setText(_translate("MainWindow", "Menu"))
        self.label_3.setText(_translate("MainWindow", "Recipes are ready to learn now!"))
        self.label_2.setText(_translate("MainWindow", "on Asian Food"))
        self.label.setText(_translate("MainWindow", "The Red Deal"))
        self.txt_name.setText(_translate("MainWindow", "Name: Xuân Đức"))
        self.txt_email.setText(_translate("MainWindow", "Email: xuanduy.nhathong@gmail.com"))
        self.txt_email.setPlaceholderText(_translate("MainWindow", "Usename"))
        self.label_12.setText(_translate("MainWindow", "Tên:"))
        self.label_22.setText(_translate("MainWindow", "Tên:"))
        self.label_35.setText(_translate("MainWindow", "Email:"))
        self.txt_password.setText(_translate("MainWindow", "password: 123456"))
        self.txt_password.setPlaceholderText(_translate("MainWindow", "Usename"))
        self.label_36.setText(_translate("MainWindow", "Password:"))
        self.label_39.setText(_translate("MainWindow", "Gender:"))
        self.cb_gender.setItemText(0, _translate("MainWindow", "Famale"))
        self.cb_gender.setItemText(1, _translate("MainWindow", "Male"))
        self.cb_gender.setItemText(2, _translate("MainWindow", "Ofther"))
        self.pushButton.setText(_translate("MainWindow", "Profile        "))
        self.btn_nav_account.setText(_translate("MainWindow", "Xuân Đức"))
        self.txt_search.setPlaceholderText(_translate("MainWindow", "Enter the formula you want to find"))
