nums = 0
a = []
b = []
while nums <= 1:
    print("Список не должен быть единичным!")
    nums = int(input("Введите количество элементов: "))
else:
    print("Вводите числа по не убыванию!")
    a.append(int(input()))
    while len(a) != nums:
        num = int(input())
        if a[-1] <= num:
            a.append(num)
        else:
            print('Вы ввели число, меньшее предыдущего!')
    print(len(set(a)))

print('\n0(1)')