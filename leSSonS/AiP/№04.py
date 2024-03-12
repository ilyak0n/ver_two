spisok = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        spisok.append(n)
count = 1
k = 0
for i in range(1,len(spisok)):
    if spisok[i] == spisok[i-1]:
        count += 1
    else:
        k = count
        count = 1
print(max(count,k))
