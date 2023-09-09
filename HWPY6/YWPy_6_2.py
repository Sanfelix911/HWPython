# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random  

def list_start(): # функция заполнения рандомного списка
    list1=[]
    numb_elem = int(random.randint(10,20)) # рандомное количество элементов в списке от 10 до 20 
    for i in range(numb_elem) :
        list1.append(int(random.randint(-20,20))) # заполняем список случайными числами 
    return list1

def max_min() : # функция нахождения рандомного диапазона
    range_list = []
    range_list.append(int(random.randint(-20,-1))) # минимальное значение диапазона
    range_list.append(int(random.randint(0,20))) # максимальное значение диапазона
    return range_list

def numb_index(l_rand,l_range): # функция выборки индексов значений в диапазоне
    list_index =[]
    for i in range(len(l_rand)):
        if l_rand[i] >= l_range[0] and l_rand[i] <= l_range[1]:
            list_index.append(i)
    return list_index         

print(f'Список со случайными значениями :')
list_start1 = list_start()
print(list_start1)
print(f'Диапазон значений :')
range_max_min = max_min()
print(range_max_min)
print(f'Индексы элементов значения которых входят в диапазон ({range_max_min[0]}) - ({range_max_min[1]}) :')
print(numb_index(list_start1,range_max_min))