'''
Задание № 1:
правильная четырехугольная пирамида написать программу вычисления объема и площади геометрической фигуры,
исходя из заданных параметров. Результат выводить с точностью 3 знака после запятой.
'''

file_in = open("data_in.txt", "r", encoding="utf-8")
x = file_in.readlines()

a = float(x[0])  # сторона основания
h = float(x[1])  # высота
l = float(x[2])  # апофема

file_in.close()

v = (h * a ** 2) / 3
s = 2 * a * l

file_out = open("data_out.txt", "w", encoding="utf-8")
file_out.write(f"Объем равен - {'%.3f' % (v)}\n")
file_out.write(f"Площадь равна - {'%.3f' % (s)}")
file_out.close()


# print("{0:.3f}".format(v), "{0:.3f}".format(s), sep="\n")

print("Задание выполнил студент Конушкин Илья группы 2023-ФГиИБ-ПИ-1б ")