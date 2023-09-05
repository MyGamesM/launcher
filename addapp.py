from PyQt6.QtGui import QCloseEvent
from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit, QLabel

class AddApp(QWidget):
	def __init__(self, parent) -> None:
		super().__init__()

		self.parent = parent

		self.grid_layout = QGridLayout()
		self.setLayout(self.grid_layout)

		self.entry = QLineEdit()
		self.grid_layout.addWidget(self.entry)

		quit_button = QPushButton("Add")
		quit_button.clicked.connect(self.close)
		self.grid_layout.addWidget(quit_button)

	def closeEvent(self, a0: QCloseEvent | None) -> None:
		# make it so that you select an app and not just a name
		with open("apps.txt", "a", encoding="UTF-8") as f:
			f.write(f"\n{self.entry.text()}")
		self.parent.loadApps()

		self.parent.refreshUI()
		return super().closeEvent(a0)