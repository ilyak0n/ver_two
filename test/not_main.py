import random


N = ["2","3",'4','5','6','7','8','9','10','J','Q','K',"A"]
M = ['♧', '♤', '♡', '♢']

dealer = []
player = []



# for i in range(2):
#     dealer.append(f"{N[random.randrange(len(N))]}:{M[random.randrange(len(M))]}")
#     player.append(f"{N[random.randrange(len(N))]}:{M[random.randrange(len(M))]}")
# print(dealer)
# print(player)





while True:
    print("1. Играть\
          \n2. Выход")

    a = input()

    if a == '1':
        for i in range(2):
            dealer.append(f"{N[random.randrange(len(N))]}:{M[random.randrange(len(M))]}")
            player.append(f"{N[random.randrange(len(N))]}:{M[random.randrange(len(M))]}")

        for_player = dealer.copy()
        for_player[1] = '*'

        print(f'dealer - {for_player}')
        print(f'player - {player}\n')

        while True:                                                                                 #Карты раздали
            print('1. Ещё\
                  \n2. Хватит')

            choose = input()

            if choose == '1':                                                                       #Выбрал взять еще
                player.append(f"{N[random.randrange(len(N))]}:{M[random.randrange(len(M))]}")
                count_p = 0
                for i in range(len(player)):
                    try:
                        count_p += int(player[i][0])
                    except ValueError:
                        if player[i][0] in "JQK":
                            count_p += 10
                        elif player[i][0] in "A":
                            if player[i][0] in "JQK":
                                count_p += 11
                            else:
                                count_p += 1

                if count_p > 21:                                                                         #Проиграл
                    print(f'dealer - {dealer}')
                    print(f'player - {player}\n')
                    print('Вы проиграли, перебор\n')
                    break
                else:                                                                                   #Тащит
                    print(f'dealer - {for_player}')
                    print(f'player - {player}\n')


            elif choose == '2':                                                                 #Выбрал остановиться
                print(f'dealer - {dealer}')
                print(f'player - {player}\n')
                print("Диллер набирает карты...")



                count_d = 0
                while count_d < 16:

                    for i in range(len(dealer)):
                        try:
                            count_d += int(dealer[i][0])
                        except ValueError:
                            if dealer[i][0] in "JQK":
                                count_d += 10
                            elif dealer[i][0] in "A":
                                if dealer[i][0] in "JQK":
                                    count_d += 11
                                else:
                                    count_d += 1
                    if count_d <= 17:
                        dealer.append(f"{N[random.randrange(len(N))]}:{M[random.randrange(len(M))]}")
                        for i in range(len(dealer)):
                            try:
                                count_d += int(dealer[i][0])
                            except ValueError:
                                if dealer[i][0] in "JQK":
                                    count_d += 10
                                elif dealer[i][0] in "A":
                                    if dealer[i][0] in "JQK":
                                        count_d += 11
                                    else:
                                        count_d += 1
                else:
                    print(f'dealer - {dealer}')
                    print(f'player - {player}\n')
                    print(count_d)


            else:
                continue


        dealer.clear()
        player.clear()


    elif a == '2':
        break
    else:
        continue