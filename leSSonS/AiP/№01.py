n = int(input())
c = 1  # присваивание
for i in range(n):
    c += 1  # итерация
    a = i ** 2
    c += 1  # присваивание
    if a <= n and a != 0:
        print(i ** 2)
    c += 2  # два условия

print(f'\nкол-во операций: {c}')
