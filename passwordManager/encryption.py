from json import load, dump
from hashlib import pbkdf2_hmac

import cryptocode


def read_file(file_name: str):
	with open(file_name, "r") as file:
		if ".json" in file_name: return load(file)
		elif ".txt" in file_name: return file.read()
		else: print(f"Введен неверный путь! Проверь - {file_name}")


def write_file(file_name: str, data):
	with open(file_name, "w") as file:
		if ".json" in file_name: dump(data, file)
		elif ".txt" in file_name: file.write(data)
		else: print(f"Введен неверный путь! Проверь - {file_name}")


def encryption_master_password(username: str, password: str) -> str:
	# Используем хеш-функцию sha256. В качестве основного текста передаем пароль. 
	# В качестве соли передаем имя пользователя. Ограничиваем длину хеша dklen=64, что равно 128 символам.
	return pbkdf2_hmac("sha256", password.encode("utf-8"), username.encode("utf-8"), 564389, dklen=64).hex()


def encript(text: str):
	# Шифруем текст хешом "гланого" пароля
	return cryptocode.encrypt(text, read_file("/passwordManager/data/masterPasswords.txt"))


def decrypt(encryptedText):
	return cryptocode.decrypt(encryptedText, read_file("/passwordManager/data/masterPasswords.txt"))
