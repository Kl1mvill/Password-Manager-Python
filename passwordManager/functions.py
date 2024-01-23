from random import choice
from os import system

from pyperclip import copy

from encryption import encript, decrypt, read_file, write_file


def clear_console(): system("cls")


# Красивый вывод существующих профилей на экран
def print_profile(data):
	if len(data.keys()) != 0:
		print("Все профили - " + ", ".join(list(data.keys())))
	else:
		print("Вы не добавили профили\n\n")
		return True # Нужно для функций del_profile, view_profiles

# Добавление профилей в dataPasswords.json
def add_profile():
	clear_console()

	data = read_file("/passwordManager/data/dataPasswords.json")

	print_profile(data)
	print("Для редактирования профиля напишите имя уже существующего и заполните профиль заново.")
	print("Если хотите выйти нажмите Enter\n")
	name = input("Введите название приложения >> ")

	if name == "": print("\n\n"); return # Проверка на Enter см. 28 строчку

	data[name] = {
		"username": encript(input("Введите имя или почту >> ")),
		"password": encript(input("Введите пароль >> ")),
		"other": encript(input("Введите дополнительную информацию >> "))
	}

	write_file("/passwordManager/data/dataPasswords.json", data)

	print("\nРегистрация завершена!!!\n\n")


def del_profile():
	clear_console()

	data = read_file("/passwordManager/data/dataPasswords.json")

	if print_profile(data): return # Проверка на существование профилей

	try:
		print("\nЕсли хотите выйти нажмите Enter")
		name = input("Введите название профиля >> ")

		if name == "": print("\n\n"); return

		del data[name]
		write_file("/passwordManager/data/dataPasswords.json", data)

		print(f"Аккаунт {name} успешно удален!\n\n")

	except KeyError: # Проверка на неверно введеное имя
		del_profile()


def view_profiles():
	clear_console()

	data = read_file("/passwordManager/data/dataPasswords.json")

	if print_profile(data): return # Проверка на существование профилей

	try:
		print("\nЕсли хотите выйти нажмите Enter")
		name = input("Введите название профиля >> ")

		if name == "": print("\n\n"); return

		print(f"\nUsername - {decrypt(data[name]["username"])}",
			  f"Password - {decrypt(data[name]["password"])}",
			  f"Other - {decrypt(data[name]["other"])} \n\n",
			  sep="\n")
	except KeyError: # Проверка на неверно введеное имя
		view_profiles()


def generate_password():
	clear_console()
	password = ""

	print("\nЕсли хотите выйти нажмите Enter")

	count = input("Введите длину пароля >> ")

	if count == "": print("\n\n"); return
	if not count.isdigit(): generate_password(); return # Проверка, если пользователь ввел не число

	for _ in range(int(count)):
		password += choice("1234567890!~?><&*$@abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ")

	print(f"\nВаш пароль - {password}\n")

	if input("Скопировать (Y/n) >> ") == "Y": 
		copy(password)
	if input("\nСгенерировать другой? (Y/n) >> ") == "Y":
		generate_password()

	print("\n\n")
