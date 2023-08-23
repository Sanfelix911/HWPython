# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени k),
# не превосходящие числа N.

import random  # импортирую модуль random

n = random.randint(1, 100)  # генерирую число n от 1 до 100
print(f"Число N = {n}")
two_to_degree = int(1)
while two_to_degree <= n:
    print(two_to_degree, end=" ")
    two_to_degree *= 2
