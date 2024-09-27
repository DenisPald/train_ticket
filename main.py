import datetime
import pandas as pd
from data import *


data = list()
data_counter = 0

while True:
    try:
        data_size = int(input("Введите требуемый размер датасета:"))
        if data_size < 0:
            raise ValueError
        break
    except ValueError:
        print("Ошибка: введите числовое значение.")

i = 0
while True:
    departure_day = datetime.datetime.today() + datetime.timedelta(days=i)
    
    departure_datetime_1 = departure_day.replace(hour=5, minute=55)
    destination_datetime_1 = departure_day.replace(hour=9, minute=42)
    train_1 = Train("754", "Сапсан", "Москва", departure_datetime_1, "Санкт-Петербург", destination_datetime_1, 2500)

    departure_datetime_2 = departure_day.replace(hour=6, minute=50)
    destination_datetime_2 = departure_day.replace(hour=10, minute=46)
    train_2 = Train("756", "Сапсан", "Москва", departure_datetime_2, "Санкт-Петербург", destination_datetime_2, 2600)

    departure_datetime_3 = departure_day.replace(hour=9, minute=30)
    destination_datetime_3 = departure_day.replace(hour=13, minute=25)
    train_3 = Train("760", "Сапсан", "Москва", departure_datetime_3, "Санкт-Петербург", destination_datetime_3, 2700)

    departure_datetime_4 = departure_day.replace(hour=13, minute=30)
    destination_datetime_4 = departure_day.replace(hour=17, minute=30)
    train_4 = Train("768", "Сапсан", "Москва", departure_datetime_4, "Санкт-Петербург", destination_datetime_4, 2700)

    departure_datetime_5 = departure_day.replace(hour=15, minute=30)
    destination_datetime_5 = departure_day.replace(hour=19, minute=40)
    train_5 = Train("772", "Сапсан", "Москва", departure_datetime_5, "Санкт-Петербург", destination_datetime_5, 2700)

    departure_datetime_6 = departure_day.replace(hour=19, minute=30)
    destination_datetime_6 = departure_day.replace(hour=23, minute=37)
    train_6 = Train("778", "Сапсан", "Москва", departure_datetime_6, "Санкт-Петербург", destination_datetime_6, 3000)

    departure_datetime_7 = departure_day.replace(hour=5, minute=30)
    destination_datetime_7 = departure_day.replace(hour=9, minute=18)
    train_7 = Train("751", "Сапсан", "Санкт-Петербург", departure_datetime_7, "Москва", destination_datetime_7, 2000)

    departure_datetime_8 = departure_day.replace(hour=13, minute=0)
    destination_datetime_8 = departure_day.replace(hour=17, minute=0)
    train_8 = Train("767", "Сапсан", "Санкт-Петербург", departure_datetime_8, "Москва", destination_datetime_8, 2300)

    departure_datetime_9 = departure_day.replace(hour=17, minute=0)
    destination_datetime_9 = departure_day.replace(hour=20, minute=50)
    train_9 = Train("775", "Сапсан", "Санкт-Петербург", departure_datetime_9, "Москва", destination_datetime_9, 2500)

    departure_datetime_10 = departure_day.replace(hour=19, minute=10)
    destination_datetime_10 = departure_day.replace(hour=23, minute=15)
    train_10 = Train("781", "Сапсан", "Санкт-Петербург", departure_datetime_10, "Москва", destination_datetime_10, 2000)

    departure_datetime_11 = departure_day.replace(hour=6, minute=25)
    destination_datetime_11 = departure_day.replace(hour=10, minute=24)
    train_11 = Train("727Г", "Ласточка", "Нижний Новгород", departure_datetime_10, "Москва", destination_datetime_10, 1100)

    departure_datetime_11 = departure_day.replace(hour=16, minute=20)
    destination_datetime_11 = departure_day.replace(hour=20, minute=44)
    train_11 = Train("732Г", "Ласточка", "Москва", departure_datetime_11, "Нижний Новгород", destination_datetime_11, 800)

    departure_datetime_12 = departure_day.replace(hour=12, minute=00)
    destination_datetime_12 = departure_day.replace(hour=15, minute=59)
    train_12 = Train("731М", "Ласточка", "Москва", departure_datetime_12, "Смоленск", destination_datetime_12, 700)

    departure_datetime_13 = departure_day.replace(hour=16, minute=00)
    destination_datetime_13 = departure_day.replace(hour=19, minute=41)
    train_13 = Train("721М", "Ласточка", "Москва", departure_datetime_13, "Смоленск", destination_datetime_13, 700)

    departure_datetime_14 = departure_day.replace(hour=13, minute=15)
    destination_datetime_14 = departure_day.replace(hour=18, minute=9)
    train_14 = Train("803C", "Ласточка", "Краснодар", departure_datetime_14, "Адлер", destination_datetime_14, 670)

    departure_datetime_15 = departure_day.replace(hour=12, minute=47)
    destination_datetime_15 = departure_day.replace(hour=17, minute=32)
    train_15 = Train("803C", "Ласточка", "Адлер", departure_datetime_14, "Краснодар", destination_datetime_14, 670)

    for train in (train_1, train_2, train_3, train_4, train_5, train_6, train_7, train_8, train_9, train_10, train_11, train_12, train_13, train_14, train_15):
        for passenger in train.passengers:
            data.append({
                "ФИО": passenger.name,
                "Паспорт": passenger.passport,
                "Откуда": train.departure_city,
                "Куда": train.destination_city,
                "Дата отъезда": train.departure_datetime.strftime("%d-%m-%YT%H:%M"),
                "Дата приезда": train.destination_datetime.strftime("%d-%m-%YT%H:%M"),
                "Рейс": train.number,
                "Вагон и место": f"{passenger.wagon}-{passenger.seat}",
                "Стоимость": passenger.cost,
                "Карта оплаты": passenger.card
            })
            data_counter+=1
            if data_counter == data_size:
                df = pd.DataFrame(data)

                df.to_csv("train_tickets.csv", index=False)
                df.to_excel("train_ticket.xlsx", index=False)
                exit()

    i+=1
