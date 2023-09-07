import os
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
			from json import loads
			with open(f"{os.getcwd()}\\{self.file}", "r", encoding="UTF-8") as f:
				return loads(f.read())

	def loadImage(self, file) -> None:
		with open(file, "rb") as f:
			return f.read()