count = 0
iter = 0
c = 2  # присваивание
while True:
    c += 1  # while
    a = int(input())
    c += 2  # присваивание + условие в if
    if a != 0:
        count += a
        iter += 1
        c += 2  # присваивание
    else:
        print(count)
        break

print(f'\nкол-во операций: {c}')
