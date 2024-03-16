from random import randrange

N = ["2","3",'4','5','6','7','8','9','10','J','Q','K',"A"]
M = ['♧', '♤', '♡', '♢']

def cards(mass: list, iter: int):
    for i in range(iter):
        mass.append(f"{N[randrange(len(N))]}:{M[randrange(len(M))]}")

def copy(mass: list):
    m = mass.copy()
    m[1] = "█"
    return m

def sum_before(mass: list):
    if len(mass) == 2 and ((mass[1][0] in "A" and (mass[0][0] in "JQK" or mass[0][0] == "10")) or (mass[0][0] in "A" and (mass[1][0] in "JQK" or mass[1][0] == "10"))):
        return "У вас 21!"
    else:
        return ""

def sum_after(mass: list):
    count = 0
    for i in range(len(mass)):
        if mass[i][:2] == "10":
            count += 10
        else:
            try:
                count += int(mass[i][0])
            except ValueError:
                if mass[i][0] in "JQK":
                    count += 10
                elif mass[i][0] == "A":
                    count += 1
                else:
                    count += int(mass[i][0])
    return count

def checking(mass: list):
    count = 0
    for i in range(len(mass)):
        if mass[i][:2] == "10":
            count += 10
        else:
            try:
                count += int(mass[i][0])
            except ValueError:
                if mass[i][0] in "JQK":
                    count += 10
                elif mass[i][0] == "A":
                    count += 1
                else:
                    count += int(mass[i][0])
    if count > 21:
        return "У вас перебор, вы проиграли!"
    else:
        return ''

def check_for_d(mass):
    count = 0
    for i in range(len(mass)):
        if mass[i][:2] == "10":
            count += 10
        else:
            try:
                count += int(mass[i][0])
            except ValueError:
                if mass[i][0] in "JQK":
                    count += 10
                elif mass[i][0] == "A":
                    count += 1
                else:
                    count += int(mass[i][0])
    if count > 21:
        return "У дилера перебор, вы выиграли!"
    else:
        return ''

def cards_for_d(mass):
    mass.append(f"{N[randrange(len(N))]}:{M[randrange(len(M))]}")
