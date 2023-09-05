import os, sys, subprocess
from pathlib import Path
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QLabel
from addapp import AddApp

os.system("cls")

class Window(QWidget):
	def __init__(self) -> None:
		super().__init__()
		self.setWindowTitle("TestApp")
		self.count = 0

		self.loadApps()
		self.initUI()

	def initUI(self) -> None:
		# self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

		self.grid_layout = QGridLayout()
		self.setLayout(self.grid_layout)
		self.refreshUI()

	def refreshUI(self) -> None:
		for i, app in enumerate(self.apps):
			button = QPushButton(str(app))
			button.clicked.connect(lambda _, app=app: self.openFile(app))
			self.grid_layout.addWidget(button, 0, i)

		add_app = QPushButton("Add app")
		add_app.clicked.connect(self.addApp)
		self.grid_layout.addWidget(add_app, 1, 0)

		quit_button = QPushButton("Quit")
		quit_button.clicked.connect(QApplication.instance().quit)
		self.grid_layout.addWidget(quit_button, 1, 1)

	def openFile(self, f) -> None:
		cwd = f"{os.getcwd()}\\apps\\"
		apps = os.listdir(cwd)
		apps2 = [Path(app).stem for app in apps]
		f = apps[int([idx for idx, elem in enumerate(apps2) if f == elem][0])]
		subprocess.run(f"{cwd}{f}", shell=True)

	def loadApps(self) -> None:
		with open("apps.txt", "r", encoding="UTF-8") as f:
			self.apps = f.read().splitlines()

		# for i in range(len(self.apps)):
		# 	self.apps[i] = os.path.splitext(os.path.basename(self.apps[i]))[0]

	def addApp(self) -> None:
		self.window = AddApp(self)
		self.window.show()

if __name__ == "__main__":
	app = QApplication([])
	app.setStyleSheet("""
		* { color: #eee; }
		QWidget { background-color: #5d677a; }
	""")
	window = Window()
	window.show()
	sys.exit(app.exec())