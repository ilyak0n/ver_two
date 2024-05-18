'''Последовательность состоит из натуральных чисел. Определить значение второго по величине элемента в этой
последовательности. (Последовательность оканчивается нулем и ноль в нее не входит).'''

listik = []
len_arr = 0
c = 2  # массив + присваивание
while True:
    n = int(input())
    c += 3  # while + присваивание + условие в if
    if n != 0:
        listik.append(n)
        len_arr += 1
        c += 2  # добавление элемента + присвваивание
    else:
        break

max = 0
pre_max = 0
c += 2  # присваивание
for i in range(len_arr):
    if listik[i] > max:
        c += 1  # итерация
        pre_max = max
        max = listik[i]
        c += 2  # присваивание
    elif listik[i] < max and listik[i] > pre_max:
        pre_max = listik[i]
    c += 4  # два условия + присваивание

print(pre_max)

print(f'\nкол-во операций: {c}')
