from BlackJack.fun import *

d = []
p = []

hide = []

def show():
    while True:

        print("1. Играть\
              \n2. Выход")
        num1 = input()

        if num1 == "1":
            cards(d, 2)
            cards(p, 2)
            print(f"dealer - {copy(d)}")
            print(f"player - {p}")
            print(sum_after(p))
            print(sum_before(p))
            if sum_after(p) == 21:
                break

            while True:
                if (((p[1][0] == p[0][0]) and (p[0][:2] != 10 or p[1][:2] != 10)) or (p[0][:2] == 10 and p[1][:2] == 10)) and (sum_after(p) > 10):
                    print("1. Еще\
                          \n2. Хватит\
                          \n3. Сдаться\
                          \n4. Разделить\
                          \n5. Удвоить")

                elif (p[1][0] == p[0][0] or (p[0][:2] == 10 and p[1][:2] == 10)) and (sum_after(p) <= 10):
                    print("1. Еще\
                                              \n2. Хватит\
                                              \n3. Сдаться\
                                              \n4. РАЗДЕЛИТЬ")

                elif (p[1][0] != p[0][0] or (p[0][:2] != 10 and p[1][:2] != 10)) and (sum_after(p) > 10):
                    print("1. Еще\
                                                                  \n2. Хватит\
                                                                  \n3. Сдаться\
                                                                  \n5. УДВОИТЬ")

                    num_abs3 = input()
                    
                    if num_abs3 == "1":
                        cards(p, 1)
                        print(f"dealer - {copy(d)}")
                        print(f"player - {p}")
                        print(sum_after(p))
                        print(checking(p))
                        if sum_after(p) > 21:
                            break

                    if num_abs3 == "2":
                        while sum_after(d) <= 17:
                            cards_for_d(d)
                        print(f"dealer - {d}")
                        print(f"player - {p}")
                        print(check_for_d(d))
                        if sum_after(d) > 21:
                            break
                        else:
                            if sum_after(p) > sum_after(d) and sum_after(p) <= 21:
                                print(f"У вас {sum_after(p)} очков, у дилера - {sum_after(d)}. Вы выиграли!")
                                break
                            elif sum_after(p) < sum_after(d) or sum_after(p) > 21:
                                print(f"У вас {sum_after(p)} очков, у дилера - {sum_after(d)} . Вы проиграли.")
                                break
                            else:
                                print(f"У вас {sum_after(p)} очков, у дилера - {sum_after(d)} . Ничья!")
                                break

                    if num_abs3 == "3":
                        break

                    if num_abs3 == "5":
                        cards(p, 1)
                        while sum_after(d) <= 17:
                            cards_for_d(d)
                        print(f"dealer - {d}")
                        print(f"player - {p}")
                        print(sum_after(p))
                        if (sum_after(p) > sum_after(d) and sum_after(p) <= 21) or (
                                sum_after(d) > 21 and sum_after(p) <= 21):
                            print(f"У вас {sum_after(p)} очков, у дилера - {sum_after(d)}. Вы выиграли!")
                            break
                        elif sum_after(p) < sum_after(d) or sum_after(p) > 21:
                            print(f"У вас {sum_after(p)} очков, у дилера - {sum_after(d)} . Вы проиграли.")
                            break
                        else:
                            print(f"У вас {sum_after(p)} очков, у дилера - {sum_after(d)} . Ничья!")
                            break
                    else:
                        continue

                else:
                    print("1. Еще\
                                                                                      \n2. Хватит\
                                                                                      \n3. Сдаться")

                num2 = input()

                if num2 == "1":
                    cards(p, 1)
                    print(f"dealer - {copy(d)}")
                    print(f"player - {p}")
                    print(sum_after(p))
                    print(checking(p))
                    if sum_after(p) > 21:
                        break

                elif num2 == "2":
                    while sum_after(d) <= 17:
                        cards_for_d(d)
                    print(f"dealer - {d}")
                    print(f"player - {p}")
                    print(check_for_d(d))
                    if sum_after(d) > 21:
                        break
                    else:
                        if sum_after(p) > sum_after(d) and sum_after(p) <= 21:
                            print(f"У вас {sum_after(p)} очков, у дилера - {sum_after(d)}. Вы выиграли!")
                            break
                        elif sum_after(p) < sum_after(d) or sum_after(p) > 21:
                            print(f"У вас {sum_after(p)} очков, у дилера - {sum_after(d)} . Вы проиграли.")
                            break
                        else:
                            print(f"У вас {sum_after(p)} очков, у дилера - {sum_after(d)} . Ничья!")
                            break

                elif num2 == "3":
                    break

                elif num2 == "4":
                    p1 = [p[0]]
                    p2 = [p[1]]
                    cards(p1,1)
                    cards(p2,1)
                    print(f"dealer - {copy(d)}")
                    print(f"player - {p1}\
                                   \n\t\t{p2}")
                    print("1. Еще для первой\
                        \n2. Еще для второй\
                        \n3. Хватит для первой\
                        \n4. Хватит для второй\
                        \n5. Сдаться")

                    num3 = input()

                    if num3 == "1":
                        continue #######################################################################

                    else:
                        continue

                # elif num2 == "5":
                #     cards(p, 1)
                #     while sum_after(d) <= 17:
                #         cards_for_d(d)
                #     print(f"dealer - {d}")
                #     print(f"player - {p}")
                #     print(sum_after(p))
                #     if (sum_after(p) > sum_after(d) and sum_after(p) <= 21) or (sum_after(d) > 21 and sum_after(p) <= 21):
                #         print(f"У вас {sum_after(p)} очков, у дилера - {sum_after(d)}. Вы выиграли!")
                #         break
                #     elif sum_after(p) < sum_after(d) or sum_after(p) > 21:
                #         print(f"У вас {sum_after(p)} очков, у дилера - {sum_after(d)} . Вы проиграли.")
                #         break
                #     else:
                #         print(f"У вас {sum_after(p)} очков, у дилера - {sum_after(d)} . Ничья!")
                #         break


                else:
                    continue

            d.clear()
            p.clear()

        elif num1 == '2':
            break

        else:
            continue

if __name__ == "__main__":
    show()