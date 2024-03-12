nums = int(input("Введите количество элементов: "))
mass = []
while len(mass) != nums:
    print(f"Введите через пробел ровно {nums} элементов!")
    mass = input().split()
for i in range(len([x for x in mass if mass.count(x) == 1])):
    print([x for x in mass if mass.count(x) == 1][i], end = ' ')