count = 0
iter = 0
с = 2  # присваивание
while True:
    с += 1  # while
    a = int(input())
    с += 2  # присваивание + условие в if
    if a != 0:
        count += a
        iter += 1
        с += 2  # присваивание
    else:
        print(count)
        break

print(f'\nкол-во операций: {c}')
