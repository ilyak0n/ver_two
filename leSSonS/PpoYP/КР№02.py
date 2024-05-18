'''Опишите класс ДАТА, заданный тремя атрибутами для года, месяца и дня. Включите в описание класса методы,
позволяющие вычислить дату предыдущего дня, вычислить дату через задан-ное число дней, и свойство, позволяющее
определить время года (зима, весна, лето, осень)'''
'''
1 3 5 7 8 10 12
4 6 9 11
2
'''

from calendar import isleap
from datetime import date, timedelta

class Data():
    def __init__(self, year, month, day, season=''):
        self.year = year
        self.month = month
        self.day = day
        self.season = season

    def GetYesterday(self):
        if self.day == 1 and self.month == 1:  # проверка на первое января
            return f"Вчера было 31-12-{self.year - 1}"
        elif self.day != 1:  # обычный день без перехода на месяц назад
            return f"Вчера было {self.day - 1}-{self.month}-{self.year}"
        elif self.day == 1 and self.month != 1:  # проверка на первое число любого другого месяца
            if self.month == 2 or 4 or 6 or 8 or 9 or 11:  # вчера было 31 число
                return f"Вчера было 31-{self.month - 1}-{self.year}"
            elif self.month == 5 or 7 or 10 or 12:  # вчера было 30 число
                return f"Вчера было 30-{self.month - 1}-{self.year}"
            elif self.month == 3 and isleap(self.year):  # проверка на февраль
                return f"Вчера было 29-{self.month - 1}-{self.year}"
            elif self.month == 3 and not isleap(self.year):
                return f"Вчера было 28-{self.month - 1}-{self.year}"
        return "Задание выполнил студент Конушкин Илья группы 2023-ФГиИБ-ПИ-1б "

    def GetNextDay(self):
        day = ""
        month = ""
        days = input('Через какое количество дней вы хотите получить дату: ')
        if len(str(self.day)) == 1:
            day = f"0{self.day}"
        else:
            day = self.day
        if len(str(self.month)) == 1:
            month = f"0{self.month}"
        else:
            month = self.month
        current_data = f"{self.year}-{month}-{day}"
        current_data = date.fromisoformat(current_data)
        delta = timedelta(days=int(days))
        return f"Через {days} дней будет {current_data + delta}\nЗадание выполнил студент Конушкин Илья группы 2023-ФГиИБ-ПИ-1б"


    def GetSeason(self):
        if self.month == 12 or 1 <= self.month <= 2:
            self.season = "Зима"
        elif 3 <= self.month <= 5:
            self.season = "Весна"
        elif 6 <= self.month <= 8:
            self.season = "Лето"
        elif 9 <= self.month <= 11:
            self.season = "Осень"
        return f"{self.season}\nЗадание выполнил студент Конушкин Илья группы 2023-ФГиИБ-ПИ-1б"


# обработка на правильность дня
while True:
    try:
        year = int(input("Введите год: "))
        month = int(input("Введите месяц: "))
        day = int(input("Введите день: "))

        if not (year > 0 and 1 <= month <= 12 and 1 <= day <= 31):  # проверка на существование года, месяца, дня
            raise Exception("Надо чтобы праивльно было")
        else:  # проверка частных случаев
            if month == 4 or 6 or 9 or 10:
                if not (1 <= day <= 30):
                    raise Exception("Такого дня нет")
            elif month == 2 and isleap(year):
                if not (1 <= day <= 29):
                    raise Exception("Такого дня нет")
            elif month == 2 and not isleap(year):
                if not (1 <= day <= 28):
                    raise Exception("Такого дня нет")
    except Exception:
        print("Случилась ошибка")
    else:  # инициализация класса если ошибок нет
        MyDay = Data(year, month, day)
        while True:
            print("\nВыберите функцию:\n"
                  "0. Выход\n"
                  "1. Дата предыдущего дня\n"
                  "2. Дата через заданное число дней\n"
                  "3. Определить время года")
            choice = input()
            if choice == "0":
                break
            elif choice == "1":
                print(MyDay.GetYesterday())
            elif choice == "2":
                print(MyDay.GetNextDay())
            elif choice == "3":
                print(MyDay.GetSeason())
            else:
                print("\n")
        break