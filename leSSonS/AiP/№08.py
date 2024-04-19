nums = int(input("Введите количество элементов: "))
mass = []
c = 0
while len(mass) != nums:
    print(f"Введите через пробел ровно {nums} элементов!")
    mass = input().split()
    c += 1
new = [x for x in mass if mass.count(x) == 1]
c += 3 * nums
for i in range(len(new)):
    c += 1
    print(new[i], end=' ')

print(f'кол-во операций: {c}')
