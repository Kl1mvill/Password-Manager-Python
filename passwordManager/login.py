from os import path, mkdir

from encryption import encryption_master_password, read_file


def сhecking_files() -> bool:
	"""
	Проверяет наличие файлов необходимых для работы программы
	Возвращает bool для проверки, есть ли зарегистрированный пользователь
	"""
	check = False

	print("Идет проверка файлов...")

	if not path.exists("/passwordManager/data"):
		mkdir("/passwordManager/data")
		print("Созданна папка data...")

	if not path.exists("/passwordManager/data/masterPasswords.txt"):
		with open("/passwordManager/data/masterPasswords.txt", 'w'): ...
		check = True
		print("Создан файл masterPasswords.txt...")

	if not path.exists("/passwordManager/data/dataPasswords.json"):
		with open("/passwordManager/data/dataPasswords.json", 'w') as file:
			file.write("{}")

		print("Создан файл dataPasswords.json...")

	if len(read_file("/passwordManager/data/masterPasswords.txt")) != 128:
		print(
			"\nВ файл masterPasswords.txt были внесенны изменения! К сожалению, все данные будут стёрты, зарегестрируйтесь ещё раз.")

		with open("/passwordManager/data/dataPasswords.json", 'w') as file:
			file.write("{}")

		with open("/passwordManager/data/masterPasswords.txt", 'w'): ...

		return True

	print("Проверка файлов прошла успешно!")
	return check


def register():
	print("\n\nЗапишите и проверьте на ошибки логин и пароль, а иначе потеряете доступ к своим данным!")

	username = input("Введите логин >> ")
	masterPassword = input("Введите пароль >> ")

	with open("/passwordManager/data/masterPasswords.txt", 'w') as file:
		file.write(encryption_master_password(username, masterPassword))

	print("\nРегистрация прошла успешно!")


def login() -> bool:
	print("Вход в систему:")
	username = input("\n\nВведите логин >> ")
	password = input("Введите пароль >> ")

	with open("/passwordManager/data/masterPasswords.txt", "r") as file:
		masterPassword = file.read()

	if encryption_master_password(username, password) == masterPassword:
		print("Вход прошел успешно!")
		return True
	else:
		print("Пароль введён не верно!")
