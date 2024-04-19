'''
Задание № 1:
правильная четырехугольная пирамида написать программу вычисления объема и площади геометрической фигуры,
исходя из заданных параметров. Результат выводить с точностью 3 знака после запятой.
'''

try:
    a = int(input("Введите сторону основания: "))
    h = int(input("Введите высоту: "))
    l = int(input("Введите апофему: "))

except ValueError:
    print("Вы ввели не чgисло!")

else:
    v = (h * a ** 2) / 3
    s = 2 * a * l

    print("{0:.3f}".format(v), "{0:.3f}".format(s), sep="\n")
    print("Задание выполнил студент Конушкин Илья группы 2023-ФГиИБ-ПИ-1б ")

finally:
    print("the end")
