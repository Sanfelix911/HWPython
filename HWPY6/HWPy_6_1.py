# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def progression(a1,st,num):
    progress = []
    progress.append(a1)
    for i in range(1,num):
        progress.append(progress[i-1]+st)
    return progress 

first_element = int(input('Введите первый элемент прогресии :'))
step = int(input('Введите значение шага прогресии :'))
numb_elements = int(input('Введите количество элементов прогресии :'))
print(f'Первый элемент {first_element} / Шаг прогрессии {step} / Количество элементов {numb_elements}')

print(progression(first_element,step,numb_elements))


    
         