# Form implementation generated from reading ui file '/Users/pinxun/Documents/MindX/PTA/PTA08/XuanDuc/python-app/ui/materials.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setMinimumSize(QtCore.QSize(400, 80))
        Form.setMaximumSize(QtCore.QSize(400, 80))
        Form.setStyleSheet("background:#f8f9fa; border-radius:8px; padding:5px; border: none;")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_ingredient_img = QtWidgets.QLabel(parent=Form)
        self.lb_ingredient_img.setMinimumSize(QtCore.QSize(60, 60))
        self.lb_ingredient_img.setMaximumSize(QtCore.QSize(60, 60))
        self.lb_ingredient_img.setScaledContents(True)
        self.lb_ingredient_img.setStyleSheet("border-radius:8px; background:#fff; border:none;")
        self.lb_ingredient_img.setObjectName("lb_ingredient_img")
        self.horizontalLayout.addWidget(self.lb_ingredient_img)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_ingredient_name = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.lb_ingredient_name.setFont(font)
        self.lb_ingredient_name.setStyleSheet("color:#111; border:none; background:transparent;")
        self.lb_ingredient_name.setObjectName("lb_ingredient_name")
        self.verticalLayout.addWidget(self.lb_ingredient_name)
        self.lb_ingredient_amount = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_ingredient_amount.setFont(font)
        self.lb_ingredient_amount.setStyleSheet("color:#444; border:none; background:transparent;")
        self.lb_ingredient_amount.setObjectName("lb_ingredient_amount")
        self.verticalLayout.addWidget(self.lb_ingredient_amount)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass
