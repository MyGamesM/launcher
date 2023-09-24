import sys, subprocess, base64

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout

from classes.addapp import AddApp
from classes.filemanager import FileManager

class Window(QWidget):
	def __init__(self) -> None:
		super().__init__()
		self.setWindowTitle("TestApp")
		self.count = 0

		self.fm = FileManager("apps.json")
		if self.fm.initFile() == 1: print("Error: data file was not found, creating new one")
		self.apps = self.fm.readFile()

		self.initUI()

	def initUI(self) -> None:
		# self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
		self.grid_layout = QGridLayout()
		self.setLayout(self.grid_layout)
		self.refreshUI()

	def buttonBuilder(self, path: str, icon: str) -> QPushButton:
		# Create button
		button = QPushButton()
		button.setFixedSize(75, 75)
		button.clicked.connect(lambda: self.runProgram(path))
		# Set button icon
		qpixmap = QPixmap()
		qpixmap.loadFromData(self.fm.decodeImage(icon))
		button_icon = QIcon(qpixmap)
		button.setIcon(button_icon)
		button.setIconSize(QSize(70, 70))

		self.grid_layout.addWidget(button, 0, self.count)

	def refreshUI(self) -> None:
		for _, key in enumerate(self.apps):
			self.buttonBuilder(self.apps[key]["path"], self.apps[key]["icon"])
			self.count += 1

		add_app = QPushButton("Add app")
		add_app.clicked.connect(self.addApp)
		self.grid_layout.addWidget(add_app, 1, 0)

		quit_button = QPushButton("Quit")
		quit_button.clicked.connect(QApplication.instance().quit)
		self.grid_layout.addWidget(quit_button, 1, 1)

	def runProgram(self, f) -> None:
		subprocess.run(f, shell=True)

	def addApp(self) -> None:
		self.window = AddApp(self)
		self.window.show()

if __name__ == "__main__":
	app = QApplication([])

	app.setStyleSheet("""
		* { color: #eee; }
		QWidget { background-color: #3e3e3e; }
	""")

	window = Window()
	window.show()
	sys.exit(app.exec())