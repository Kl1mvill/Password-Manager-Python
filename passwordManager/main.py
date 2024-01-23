from functions import *
from login import *

if __name__ == "__main__":
	# Проверка наличия необходимых для работы файлов. Подробнее в login.py
	if сhecking_files():
		register() # Регистрация пользователя

	clear_console()
	if login(): # Вход в приложение
		clear_console()
		while True: # Панель управления
			print("1. Добавить и редактировать профиль",
				  "2. Удалить профиль",
				  "3. Посмотреть пароль",
				  "4. Сгенерировать надежный пароль",
				  "5. Выход", sep="\n")

			command = input("Выберите действие >> ")
			match command:
				case "1": add_profile()
				case "2": del_profile()
				case "3": view_profiles()
				case "4": generate_password()
				case "5": raise SystemExit

				case _: print("Неизвестная команда"); clear_console()
