try:
	from PySide6 import QtCore, QtGui, QtWidgets 
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets 
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui 

IMAGE_DIR = 'C:/Users/ICT68/Documents/maya/2025/scripts/styletool/image'

class StyleToolDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setWindowTitle('Style Tool')
		self.resize(300, 100)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet(
			'''
				font-family: Papyrus;
				color: white;
				background-color: #6699CC;
				}
			'''
		)

		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f'{IMAGE_DIR}/GingerBrave.png')
		scaledPixmap = self.imagePixmap.scaled(
			QtCore.QSize(300,300),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)
		self.imageLabel.setPixmap(scaledPixmap)
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.mainLayout.addWidget(self.imageLabel)

		self.nameLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)
		self.nameLabel = QtWidgets.QLabel('Name: ')
		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLineEdit.setStyleSheet(
			'''
				QLineEdit{
					background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #7C18FF, stop:1 #AF0CAF);
					color: white;
					border-radius: 8px;
					font-family: Arial;
					font-weight: bold;
				}
			'''
		)

		self.nameLayout.addWidget(self.nameLabel)
		self.nameLayout.addWidget(self.nameLineEdit)

		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)
		self.selectButton = QtWidgets.QPushButton('Select')
		self.selectButton.setStyleSheet(
			'''
				QPushButton{
					background-color: #78F075;
					border-radius: 12px;
					font-size: 16px;
					color: balck;
					font-family: Papyrus;
					font-weight: bold;
					padding: 4px;
				}
				QPushButton:hover{
					background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #50F0B0, stop:1 #F0E53F);
				}
				QPushButton:pressed{
					background-color: #F0EB63;
				}
			'''
		)

		self.cancelButton = QtWidgets.QPushButton('Cancel')
		self.cancelButton.setStyleSheet(
			'''
				QPushButton{
					background-color: #EF196B;
					border-radius: 12px;
					font-size: 16px;
					color: balck;
					font-family: Papyrus;
					font-weight: bold;
					padding: 4px;
				}
				QPushButton:hover{
					background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B13DEF, stop:1 #EF679F);
				}
				QPushButton:pressed{
					background-color: #982042;
				}
			'''
		)
		self.buttonLayout.addWidget(self.selectButton)
		self.buttonLayout.addWidget(self.cancelButton)

		self.mainLayout.addStretch()

def run():
	global ui 
	try:
		ui.close()
	except:
		pass
	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = StyleToolDialog(parent=ptr)
	ui.show()