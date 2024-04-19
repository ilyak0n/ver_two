count = int(input())
a = []
len_a = 0
c = 3 # присваивание х3
while len_a != count:
    a.append(input())
    len_a += 1
    c += 3 # цикл + добавление + присваивание
for i in range(1, len(a), 2):
    a[i], a[i - 1] = a[i - 1], a[i]
    c += 3 # итерация + присваивание
print(a)

print(f'кол-во операций: {c}')
