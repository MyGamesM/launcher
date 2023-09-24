import os, base64

class FileManager:
	def __init__(self, file: str) -> None:
		self.file = file

	def initFile(self) -> int | None:
		if not os.path.exists(self.file):
			with open(f"{os.getcwd()}\\{self.file}", "w") as f:
				f.write("{}")
			return 1

	def writeFile(self, data: str | dict) -> None:
		if type(data) == str and data != "":
			with open(f"{os.getcwd()}\\{self.file}", "w", encoding="UTF-8") as f:
				f.write(data)

		elif type(data) == dict and data != {}:
			from json import dump
			with open(f"{os.getcwd()}\\{self.file}", "w", encoding="UTF-8") as f:
				dump(data, f)

	def readFile(self) -> str | dict:
		if self.file.endswith(".txt"):
			with open(f"{os.getcwd()}\\{self.file}", "r", encoding="UTF-8") as f:
				return f.read()
			
		elif self.file.endswith(".json"):
			from json import load
			with open(f"{os.getcwd()}\\{self.file}", "r", encoding="UTF-8") as f:
				return load(f)

	def loadImage(self, file) -> bytes:
		with open(file, "rb") as f:
			return f.read()
		
	def encodeImage(self, data) -> str:
		return base64.b64encode(data).decode("ascii")

	def decodeImage(self, data) -> bytes:
		return base64.b64decode(data)