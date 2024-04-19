nums = 0
a = []
b = []
len_a = 0
c = 4  # присваивание х4
while nums <= 1:
    print("Список не должен быть единичным!")
    nums = int(input("Введите количество элементов: "))
    c += 2  # цикл + присваивание
else:
    print("Вводите числа по не убыванию!")
    a.append(int(input()))
    len_a += 1
    c += 2  # добавление + присваивание
    while len_a != nums:
        num = int(input())
        c += 3  # цикл + присваивание + условие
        if a[-1] <= num:
            a.append(num)
            len_a += 1
            c += 2  # добавление + присваивание
        else:
            print('Вы ввели число, меньшее предыдущего!')

    b.append(a[0])
    len_b = 0
    c += 2  # присваивание х2
    for i in range(0, len_a - 1):
        c += 2  # итерация + условие
        if a[i] != a[i + 1]:
            b.append(a[i + 1])
            len_b += 1
            c += 2  # добавление + присваивание
    print(len_b)

print(f'кол-во операций: {c}')
