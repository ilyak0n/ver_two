'''
Дан двумерный массив A размером 10*6 элементов, заполненный случайными целыми числами из диапазона (-10,10).
Сформировать   одномерный массив B, каждый элемент которого заполнить, разностью, между максимальным и средним
значением столбца двумерного массива A.
'''
import random
def maxx(a: list) -> int:
    m = 0
    for i in range(1,len(a)):
        if a[i] > a[i-1] and a[i] > m:
            m = a[i]
        elif a[i-1] > a[i] and a[i-1] > m:
            m = a[i-1]
    return m
def sred(a: list):
    x = 0
    count = 0
    for i in range(len(a)):
        x += a[i]
        count += 1
    return x/count

def preobr(a: list) -> list:
    b = []
    for i in range(len(a)):
        b.append('{:.2f}'.format(maxx(a[i]) - sred(a[i])))
    return b

a = [0]*10
for i in range(10):
    a[i] = [random.randrange(-10,11)  for j in range(6)]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print('')
print(f'\nB = {preobr(a)}')

print("Задание выполнил студент Конушкин Илья группы 2023-ФГиИБ-ПИ-1б ")