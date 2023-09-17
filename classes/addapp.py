from os.path import expanduser

from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QFileDialog, QLabel

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
		self.grid_layout.addWidget(select_program_button, 1, 0)

		select_icon_button = QPushButton("Select\nicon")
		select_icon_button.clicked.connect(lambda: self.openFileDialog(1))
		self.grid_layout.addWidget(select_icon_button, 1, 1)

		add_button = QPushButton("Add")
		add_button.clicked.connect(self.processData)
		self.grid_layout.addWidget(add_button, 2, 0)

		close_button = QPushButton("Close")
		close_button.clicked.connect(self.close)
		self.grid_layout.addWidget(close_button, 2, 1)

	def showErrorLabel(self, msg: str) -> None:
		error_label = QLabel(msg)
		error_label.setStyleSheet("font-size: 14px;")
		self.grid_layout.addWidget(error_label, 0, 0, 1, 0)

	def processData(self) -> None:
		apps = self.parent.apps

		try:
			name = self.program_path.split("/")[-1][:-4]

			apps[name] = {
				"path" : self.program_path,
				"icon" : self.icon_path
			}
		except:
			self.showErrorLabel("Please select a file and icon")
			return

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
				if type == 0 and filename.endswith(".exe"): self.program_path = filename
				elif type == 1 and (filename.endswith(".png") or filename.endswith(".jpg")): self.icon_path = filename