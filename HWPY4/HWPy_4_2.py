# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод —
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь перед некоторым 
# кустом.

import random  # импортирую модуль random

# Входные данные
number_of_bushes = int(random.randint(4,11)) # случайное количество кустов от 4 до 10
number_of_berry_bushes = [] # пустой список для количества ягод на кустах
for i in range(number_of_bushes): # цикл заполнения списка с количеством ягод на куста
    number_of_berry_bushes.append(int(random.randint(1,11))) # заполняем список случайными числами количестов ягод от 1 до 10
print(f'Количество кустов : {number_of_bushes}') # выводим количество кустов
print(f'Количество ягод на каждом кусте : {number_of_berry_bushes}') 

# Поиск количества собираемыч ягод на позиции сборочного модуля
number_of_berries_per_position = [] # пустой список для количества ягод на позиции модуля
for i in range(len(number_of_berry_bushes)): # цикл заполнения количества ягод на каждой позиции
    if i == 0 :
        number_of_berries_per_position.append((number_of_berry_bushes[len(number_of_berry_bushes)-1]+number_of_berry_bushes[i]+number_of_berry_bushes[i+1]))
    elif (i == (len(number_of_berry_bushes)-1)):
        number_of_berries_per_position.append((number_of_berry_bushes[len(number_of_berry_bushes)-2]+number_of_berry_bushes[i]+number_of_berry_bushes[0]))
    elif (i > 0): 
        number_of_berries_per_position.append(number_of_berry_bushes[i-1]+number_of_berry_bushes[i]+number_of_berry_bushes[i+1])
print(f'Количество собираемых ягод на каждой позиции модуля : {number_of_berries_per_position}')

# Поиск и вывод максимального количества ягод на позиции модуля
print(f'Максимальное количество ягод с одной позици модуля : {max(number_of_berries_per_position)}')
    
    






