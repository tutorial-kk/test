import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class=uic.loadUiType('test.ui')[0]

class MyWindow(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.btn_clicked)

	def btn_clicked(self):
		self.label.setText("clicked")
		QMessageBox.about(self, "message","clicked")
		Self.label.setText("")


if __name__=="__main__":
	app=QApplication(sys.argv)
	mywindow=MyWindow()
	mywindow.show()
	app.exec_()

'''
	def setupUI(self):
		self.setWindowTitle("Review")
		btn1=QPushButton("Click me", self)
		btn1.move(10,10)
		btn1.clicked.connect(self.btn1_clicked)
		self.show()
'''