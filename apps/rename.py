import os

data = os.listdir(f"{os.getcwd()}\\apps\\")

for file in data:
	print(file)
	os.rename(
		f"{os.getcwd()}\\apps\\{file}",
		f'{os.getcwd()}\\apps\\{file.replace(".exe - Shortcut", "")}'
	)