import sys
import os
import BNS

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import *
from PySide6.QtCore import QFile, QIODevice

def resource_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath("."), relative_path)

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = QUiLoader().load(resource_path('UI/Qt.ui'))
		
		#시그널 등록
		self.ui.btn_predict.clicked.connect(self.predict)
		
	def predict(self):
		len = self.ui.lineEdit_length.text()
		weight = self.ui.lineEdit_weight.text()
		self.ui.label_result.setText(BNS.predict(len, weight))
			
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.ui.show()
	sys.exit(app.exec())