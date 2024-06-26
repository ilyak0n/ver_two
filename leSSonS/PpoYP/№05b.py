'''
разработать аналогичную программу №5b табулирования, но с использованием пользовательских функций
(точно также с учетом области ее определения при изменении аргумента значения х от начального x_0
до конечного значения x_n постоянным шагом h_x, где значения функции выводить с точностью 3 знака после запятой)
'''
import math

def f(x_0: int, x_n: int, h):
    while x_0 <= x_n + h:
        if x_0 <= -3:
            y = -x_0 - 3
            print('{:.3f}'.format(x_0), "\t", '{:.3f}'.format(y))
        elif -3 < x_0 <= -1:
            y = math.sqrt(4 - (x_0 + 1) ** 2)
            print('{:.3f}'.format(x_0), "\t", '{:.3f}'.format(y))
        elif -1 < x_0 <= 1:
            y = 2
            print('{:.3f}'.format(x_0), "\t", '{:.3f}'.format(y))
        elif 1 < x_0 <= 3:
            y = math.sqrt(4 - (x_0 - 1) ** 2)
            print('{:.3f}'.format(x_0), "\t", '{:.3f}'.format(y))
        elif 3 < x_0:
            y = 1.5 * x_0 - 4.5
            print('{:.3f}'.format(x_0), "\t", '{:.3f}'.format(y))
        x_0 += h

f(-10,10,0.05)

print("Задание выполнил студент Конушкин Илья группы 2023-ФГиИБ-ПИ-1б ")