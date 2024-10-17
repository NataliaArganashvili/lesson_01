month = int(input("Введите номер месяца: "))

def month_to_season(month):
    if month in range (1, 3) or month == 12:
        print("Зима")
    if month in range (3, 6):
        print("Весна")
    if month in range (6, 9):
        print("Лето")
    if month in range (9, 12):
        print("Осень")

month_to_season(month)
