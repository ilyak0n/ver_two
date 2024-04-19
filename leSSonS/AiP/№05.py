spisok = []
len_spisok = 0
c = 2  # присваивание х2
while True:
    n = int(input())
    c += 3  # пока + присваивание + условие
    if n != 0:
        spisok.append(n)
        len_spisok += 1
        c += 2  # добавление + присваивание
    else:
        break

new_sp = []
len_new_sp = 0
c += 2  # присваивание х2
for i in range(1, len_spisok - 1):
    c += 3  # итерация + два условия
    if spisok[i] > spisok[i - 1] and spisok[i] > spisok[i + 1]:
        new_sp.append(i)
        len_new_sp += 1
        c += 2  # присваивание х2

otv = 0
sp = []
len_sp = 0
c += 3  # присваивание х3
for i in range(1, len_new_sp):
    sp.append(new_sp[i] - new_sp[i - 1])
    len_sp += 1
    c += 3  # итерация + добавление + присваивание

c += 1  # условие
if len_sp == 1:
    print(sp[0])
else:
    for i in range(1, len_sp):
        c += 2  # итерация + условие
        if sp[i - 1] < sp[i]:
            otv = sp[i - 1]
            c += 1  # присваивание
        else:
            otv = sp[i]
            c += 1  # присваивание
    print(otv)

print(f'кол-во операций: {c}')
