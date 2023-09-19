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

def main():
    print('1) Создать файл телефонной книги ',
          '2) Добавить запись в телефонную книгу',
          '3) Найти запись по имени',
          '4) Найти запись по фамилии',
          '5) Найти запись по телефону',
          '6) Выход' , sep='\n', end='\n')
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
            print("Good bye")

# create_file()
# add_person()
# add_person()
# add_person()
