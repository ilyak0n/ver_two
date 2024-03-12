'''
Задание №5
написать программу на Python с использованием пользовательских функций согласно конкретным формулировкам,
указанным перед каждым из 5 индивидуальных заданий Варианта.
'''
import math

def to_ten_system(number: str, system: int) -> int:
    '''
    Функция переводит число из любой системы счисления в десятеричную
    :param number: число, которое надо перевести
    :param system: система счисления, в которой записано число
    :return: число в десятеричной системе мсисления
    '''
    if system < 10:
        number = number[::-1]
        res = 0
        for i in range(len(number)):
            res += int(number[i]) * system**i
        return res
    else:
        return int(number, system)

def to_any_system(num: int or float, system: int) -> str:
    '''
    Функция переводит числа из десятеричной системы счисления в любую
    :param num: число, которое надо перевести
    :param system: требуемая система счисления
    :return: число в искомой системе счисления
    '''
    s = ''
    if num == int(num):
        while num != 0:
            s += str(num % system)
            num //= system
        s = s[::-1]
        return s
    elif num == float(num):
        f_num = num - int(num)
        num = int(num)
        while int(num) != 0:
            s += str(int(num) % system)
            num //= system
        s = s[::-1]
        s += '.'
        while f_num != 0.0:
            if len(s[s.find('.') + 1:]) == 3:
                break
            f_num *= system
            s += str(int(f_num))

            f_num -= int(f_num)
        return s

print("Пункт 1:")
print(f"15 в 7 = {to_ten_system('15', 7)}")
print(f"24 в 5 = {to_ten_system('24', 5)}")
print(f"14 в 10 = {to_ten_system('14', 10)}")
print(f"C в 16 = {to_ten_system('c',16)}")
print("Следовательно: 15 в 7 = С в 16; 24 в 5 = 14 в 10", '\n')


a1 = (to_ten_system('10000',16))
a2 = to_ten_system('1101',2)
res = math.sqrt(a1) + a2**2
print("Пункт 2:")
print(f"10000 в 16 = {to_ten_system('10000',16)}")
print(f"1101 в 2 = {to_ten_system('1101',2)}")
print(f"Следовательно: sqrt(10000 в 16) + (1101 в 2)**2 = {int(res)} = {bin(int(res))[2:]}")


print('\nПункт 3:')
n = to_ten_system("1000",2)
if n<45:
    print(f"1000 в 2 = {n}; Следовательно: 1000 в 2 < 45 в 10")
elif n>45:
    print(f"1000 в 2 = {n}; Следовательно: 1000 в 2 > 45 в 10")
else:
    print(f"1000 в 2 = {n}; Следовательно: 1000 в 2 = 45 в 10")


print("\nПункт 4:")
a = []
b1 = to_ten_system('100',2)
b2 = to_ten_system('101',2)
b3 = to_ten_system('110', 2)
b4 = to_ten_system('11111',2)
a.append(b1)
a.append(b2)
a.append(b3)
a.append(b4)
print(f'100 в 2 = {b1}', f'101 в 2 = {b2}', f'110 в 2 = {b3}', f'11111 в 2 = {b4}', '\nСледовательно:', sep='\n')

for i in range(len(a)):
    if a[i]%2 == 0:
        print(f"{bin(int(a[i]))[2:]} - Чет")
    else:
        print(f"{bin(int(a[i]))[2:]} - Нечет")

print("\nПункт 5:")
print("2/3 + 3/9 + 7/9 = ", '{:.3f}'.format(2/3 + 3/9 + 7/9))
print(f"Следовательно: {'{:.3f}'.format(2/3 + 3/9 + 7/9)} в 3 = {to_any_system(2/3+1/3+7/9,3)}")

print("Задание выполнил студент Конушкин Илья группы 2023-ФГиИБ-ПИ-1б ")