nums = int(input("Введите количество элементов: "))
mass = []
while len(mass) != nums:
    print(f"Введите через пробел ровно {nums} элементов!")
    mass = input().split()
new = [x for x in mass if mass.count(x) == 1]
for i in range(len(new)):
    print(new[i], end = ' ')

print('\n0(n)')