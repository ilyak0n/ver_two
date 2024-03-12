spisok = []
while True:
    n = int(input())
    if n != 0:
        spisok.append(n)
    else:
        break
print(spisok)
new_sp = []
for i in range(1,len(spisok)-1):
    if spisok[i] > spisok[i-1] and spisok[i] > spisok[i+1]:
        new_sp.append(i)
print(new_sp)
otv = 0
sp = []
for i in range(1,len(new_sp)):
    sp.append(new_sp[i]-new_sp[i-1])
print(sp)
for i in range(1,len(sp)):
    if sp[i-1] < sp[i]:
        otv = sp[i-1]
    else:
        otv = sp[i]
print(otv)
