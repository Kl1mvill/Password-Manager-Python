from functions import *
from login import *

if __name__ == "__main__":
	if сhecking_files():
		register()

	clear_console()
	if login():
		clear_console()
		while True:
			print("1. Добавить и редактировать профиль",
				  "2. Удалить профиль",
				  "3. Посмотреть пароль",
				  "4. Сгенерировать надежный пароль",
				  "5. Выход", sep="\n")

			command = input("Выберите действие >> ")
			match command:
				case "1":
					add_profile()
				case "2":
					del_profile()
				case "3":
					view_profiles()
				case "4":
					generate_password()
				case "5":
					raise SystemExit

				case _:
					print("Неизвестная команда"); clear_console()
