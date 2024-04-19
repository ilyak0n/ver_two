'''
Дан двумерный массив A размером 10*6 элементов, заполненный случайными целыми числами из диапазона (-10,10).
Сформировать   одномерный массив B, каждый элемент которого заполнить, разностью, между максимальным и средним
значением столбца двумерного массива A.
'''
import random

a = [0]*10
for i in range(10):
    a[i] = [random.randrange(-10,11)  for j in range(6)]

b = []
for i in range(len(a)):
    sr = 0
    summ = 0
    count = 0
    for j in range(len(a[i])):
        summ += a[i][j]
        count += 1
    b.append('{:.2f}'.format((max(a[i])) - (summ/count)))

print("A =", end="")
for i in range(len(a)):
    print(f"\t{a[i]}")
print(f"B = {b}")

print("Задание выполнил студент Конушкин Илья группы 2023-ФГиИБ-ПИ-1б ")