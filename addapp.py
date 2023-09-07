from os.path import expanduser

# from PyQt6.QtCore import QFileInfo
# from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QFileDialog

class AddApp(QWidget):
	def __init__(self, parent) -> None:
		super().__init__()

		self.parent = parent

		self.initUI()

	def initUI(self) -> None:
		self.grid_layout = QGridLayout()
		self.setLayout(self.grid_layout)

		select_program_button = QPushButton("Select\nprogram")
		select_program_button.clicked.connect(lambda: self.openFileDialog(0))
		self.grid_layout.addWidget(select_program_button, 0, 0)

		select_icon_button = QPushButton("Select\nicon")
		select_icon_button.clicked.connect(lambda: self.openFileDialog(1))
		self.grid_layout.addWidget(select_icon_button, 0, 1)

		add_button = QPushButton("Add")
		add_button.clicked.connect(self.processData)
		self.grid_layout.addWidget(add_button, 1, 0)

		close_button = QPushButton("Close")
		close_button.clicked.connect(self.close)
		self.grid_layout.addWidget(close_button, 1, 1)

	def processData(self) -> None:
		apps = self.parent.fm.readFile()
		name = self.program_path.split("/")[-1][:-4]

		apps[name] = {
			"path" : self.program_path,
			"icon" : self.icon_path
		}

		self.parent.fm.writeFile(apps)
		self.parent.buttonBuilder(self.program_path, self.icon_path)
		self.close()

	def openFileDialog(self, type: int):
		select_file = QFileDialog(self)
		select_file.setDirectory(f"{expanduser('~')}/Desktop")
		select_file.setFileMode(QFileDialog.FileMode.ExistingFile)

		if type == 0: select_file.setNameFilter("Programs (*.exe)")
		elif type == 1: select_file.setNameFilter("Images (*.png *.jpg)")
		else: return

		if select_file.exec():
			filename = select_file.selectedFiles()[0]
			if filename:
				if type == 0 and filename.endswith(".exe"): self.program_path = filename # self.parent.fm.loadImage(filename[0])
				elif type == 1 and (filename.endswith(".png") or filename.endswith(".jpg")): self.icon_path = filename # self.parent.fm.loadImage(filename[0])