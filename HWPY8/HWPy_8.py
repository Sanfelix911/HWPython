# Домашнее задание
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных

def add_person():
	name_first = input('Введите имя: ')
	name_last = input('Введите фамилию: ')
	phone_num = input('Введите телефон: ')
	with open('phone_book.txt', 'a', encoding='utf-8') as book:
		book.write(f'{name_first} {name_last} {phone_num}\n')

def create_file():
	with open('phone_book.txt', 'w', encoding='utf-8') as book:
		book.write('Имя   Фамилия   Телефон\n')

def search_name():
	name_search = input('Введите имя для поиска: ')
	with open('phone_book.txt', 'r', encoding='utf-8') as book:
		for line in book:
			if name_search.lower() == (note:=line.strip('\n').split())[0].lower():
				return note
		return "Запись не найдена"
	
def search_surname():
	surname_search = input('Введите фамилию для поиска: ')
	with open('phone_book.txt', 'r', encoding='utf-8') as book:
		for line in book:
			if surname_search.lower() == (note:=line.strip('\n').split())[1].lower():
				return note
		return "Запись не найдена"

def search_phone():
	phone_search = input('Введите телефон для поиска: ')
	with open('phone_book.txt', 'r', encoding='utf-8') as book:
		for line in book:
			if phone_search.lower() == (note:=line.strip('\n').split())[2].lower():
				return note
		return "Запись не найдена"

def suggest_user():
	print('Что ищем?',
		'1) Найти запись по имени',
		'2) Найти запись по фамилии',
		'3) Найти запись по телефону' , sep='\n', end='\n')
	attr = input('Введите вариант: ')
	match attr:
		case '1':
			user = search_name()
			return user
		case '2':
			user = search_surname()
			return user
		case '3':
			user = search_phone()
			return user
		case _:
			print("Такой команды не найдено попробуйте снова")
			return None
			
def delete_contact():
	user_1 = suggest_user()
	if user_1 is None:
		return
		
	book = open('phone_book.txt', 'r', encoding='utf-8')
	book_variable = book.readlines()
	book.close()

	book = open('phone_book.txt', 'w', encoding='utf-8')
	for line in book_variable:
		line_1 = line.replace('\n', '')
		if not (line_1.split(' ')[0] == user_1[0] and line_1.split(' ')[1] == user_1[1] and line_1.split(' ')[2] == user_1[2]):
			book.write(line)
	book.close()
	print(f"Абонент {' '.join(user_1)} удален")

def change_attribute(user, attr_num):
	attr = input('Введите замену: ')
	if user is None:
		return
		
	book = open('phone_book.txt', 'r', encoding='utf-8')
	book_variable = book.readlines()
	book.close()

	book = open('phone_book.txt', 'w', encoding='utf-8')
	for line in book_variable:
		line_1 = line.replace('\n', '')
		if not (line_1.split(' ')[0] == user[0] and line_1.split(' ')[1] == user[1] and line_1.split(' ')[2] == user[2]):
			book.write(line)
		else:
			user[int(attr_num) - 1] = attr
			book.write(' '.join(user) + '\n')
	book.close()
	print(f"Абонент {' '.join(user)} изменен")



def change_contact():
	user = suggest_user()
	print(*user)
	print('Что будем менять?',
		'1) Изменить имя',
		'2) Изменить фамилию',
		'3) Изменить телефон' , sep='\n', end='\n')
	attr = input('Введите вариант: ')
	change_attribute(user, attr)

def main():
	while 1==1:
		print('1) Создать файл телефонной книги ',
			'2) Добавить запись в телефонную книгу',
			'3) Найти запись по имени',
			'4) Найти запись по фамилии',
			'5) Найти запись по телефону',
			'6) Удалить запись',
			'7) Изменить запись',
			'8) Выход' , sep='\n', end='\n')
		match input():
			case '1':
				create_file()
			case '2':
				add_person()
			case '3':
				print(search_name())
			case '4':
				print(search_surname())
			case '5':
				print(search_phone())
			case '6':
				delete_contact()
			case '7':
				change_contact()
			case '8':
				print("Good bye")
				break
			case _:
				print("Такой команды не найдено попробуйте снова")
main()
