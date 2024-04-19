spisok = []
len_spisok = 0
c = 2  # присваивание + массив

while True:
    n = int(input())
    c += 3  # while + присваивание + условие в if
    if n == 0:
        break
    else:
        spisok.append(n)
        len_spisok += 1
        c += 2  # добавлене элемента + присваивание

current = 0
next = 0
count = 1
answer = 0
c += 4  # 4 присваивания
for i in range(len_spisok):
    next = spisok[i]
    c += 2  # итерация + присваивание
    if next == current:
        count += 1
        c += 1  # присваивание
    else:
        current, next = 0, 0
        c += 2  # присваивания
        if count > answer:
            answer = count
            c += 1  # присваивание
        count = 1
        c += 2  # присваивание + условие
    current = spisok[i]
    c += 2  # условие + присваивание

print(answer)

print(f'\nкол-во операций: {c}')
