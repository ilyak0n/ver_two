listik = []
while True:
    n = int(input())
    if n != 0:
        listik.append(n)
    else:
        break
mn = set(sorted(listik))
a = list(mn)
print(a[-2])

print('\no(n)')