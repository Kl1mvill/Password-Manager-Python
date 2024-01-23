from os import path, mkdir

from encryption import encryption_master_password, read_file, write_file


def сhecking_files() -> bool:
	"""
	Проверяет наличие файлов необходимых для работы программы.
	Возвращает bool для проверки, есть ли зарегистрированный пользователь.
	"""
	check = False

	print("Идет проверка файлов...")

	# Проверяет созданна ли папка data
	if not path.exists("/passwordManager/data"):
		mkdir("/passwordManager/data")
		print("Созданна папка data...")

	# Проверяет создан ли в папке data файл masterPasswords.txt
	if not path.exists("/passwordManager/data/masterPasswords.txt"):
		with open("/passwordManager/data/masterPasswords.txt", 'w'): ...
		check = True
		print("Создан файл masterPasswords.txt...")

	# Проверяет создан ли в папке data файл dataPasswords.json
	if not path.exists("/passwordManager/data/dataPasswords.json"):
		with open("/passwordManager/data/dataPasswords.json", 'w') as file:
			file.write("{}")

		print("Создан файл dataPasswords.json...")

	# Проверяет изменял ли кто-нибудь файл masterPasswords.txt. Если изменял то все данные стираются.
	# Также помогает избежать бага при регистрации.
	if len(read_file("/passwordManager/data/masterPasswords.txt")) != 128 and not check:
		print("\nВ файл masterPasswords.txt были внесенны изменения! К сожалению, все данные будут стёрты, зарегестрируйтесь ещё раз.")

		with open("/passwordManager/data/dataPasswords.json", 'w') as file:
			file.write("{}")

		with open("/passwordManager/data/masterPasswords.txt", 'w'): ...

		return True

	print("Проверка файлов прошла успешно!")
	return check


def register():
	"Регистрация нового 'гланого' пользователя"
	
	print("\n\nЗапишите логин и пароль, а иначе потеряете доступ к своим данным!")

	username = input("Введите логин >> ")
	masterPassword = input("Введите пароль >> ")

	write_file("/passwordManager/data/masterPasswords.txt", encryption_master_password(username, masterPassword))

	print("\nРегистрация прошла успешно!")


def login() -> bool: # Возвращает результат входа
	print("Вход в систему:")
	
	username = input("\n\nВведите логин >> ")
	password = input("Введите пароль >> ")

	masterPassword = read_file("/passwordManager/data/masterPasswords.txt")
	
	# Хэширование пароля введеного пользователем и сравнение полученного хэша с уже существующим.
	# Подробнее в encryption.py
	if encryption_master_password(username, password) == masterPassword:
		print("Вход прошел успешно!")
		return True
	else:
		print("Пароль введён не верно!")
