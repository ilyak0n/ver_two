import math

x = -10
a = 10
h = 0.05

while x <= a+h:
    if x <= -3:
        y = -x - 3
        print('{:.3f}'.format(x), "\t", '{:.3f}'.format(y))
    elif -3 < x <= -1:
        y = math.sqrt(4 - (x + 1)**2)
        print('{:.3f}'.format(x), "\t", '{:.3f}'.format(y))
    elif -1 < x <= 1:
        y = 2
        print('{:.3f}'.format(x), "\t", '{:.3f}'.format(y))
    elif 1 < x <= 3:
        y = math.sqrt(4 - (x - 1)**2)
        print('{:.3f}'.format(x), "\t", '{:.3f}'.format(y))
    elif 3 < x:
        y = 1.5 * x - 4.5
        print('{:.3f}'.format(x), "\t", '{:.3f}'.format(y))
    x += h

print("Задание выполнил студент Конушкин Илья группы 2023-ФГиИБ-ПИ-1б ")