'''
разработать аналогичную программу №5c табулирования, но с использованием объектно-ориентированного подхода
(и точно также с учетом области ее определения при изменении аргумента значения х от начального x_0 до конечного
значения x_n постоянным шагом h_x, где значения функции выводить с точностью 3 знака после запятой)
'''
import math

class Function:
    def __init__(self, x_0, x_n, h):
        self.x_n = x_n
        self.x_0 = x_0
        self.h = h

    def iteration(self):
        while self.x_0 <= self.x_n + self.h:
            if self.x_0 <= -3:
                y = -self.x_0 - 3
                print('{:.3f}'.format(self.x_0), "\t", '{:.3f}'.format(y))
            elif -3 < self.x_0 <= -1:
                y = math.sqrt(4 - (self.x_0 + 1) ** 2)
                print('{:.3f}'.format(self.x_0), "\t", '{:.3f}'.format(y))
            elif -1 < self.x_0 <= 1:
                y = 2
                print('{:.3f}'.format(self.x_0), "\t", '{:.3f}'.format(y))
            elif 1 < self.x_0 <= 3:
                y = math.sqrt(4 - (self.x_0 - 1) ** 2)
                print('{:.3f}'.format(self.x_0), "\t", '{:.3f}'.format(y))
            elif 3 < self.x_0:
                y = 1.5 * self.x_0 - 4.5
                print('{:.3f}'.format(self.x_0), "\t", '{:.3f}'.format(y))
            self.x_0 += self.h

myFunction = Function(-10, 10, 0.05)
myFunction.iteration()

print("\nЗадание выполнил студент Конушкин Илья группы 2023-ФГиИБ-ПИ-1б ")