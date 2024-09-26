import datetime
import pandas as pd
from data import *


data = []
for i in range(0, 20):
    departure_day = datetime.datetime.today() + datetime.timedelta(days=i)
    
    departure_datetime_1 = departure_day.replace(hour=5, minute=55)
    destination_datetime_1 = departure_day.replace(hour=9, minute=42)
    sapsan_1 = Train("754", "Сапсан", "Москва", departure_datetime_1, "Санкт-Петербург", destination_datetime_1, 2500)

    print(1)
    departure_datetime_2 = departure_day.replace(hour=6, minute=50)
    destination_datetime_2 = departure_day.replace(hour=10, minute=46)
    sapsan_2 = Train("756", "Сапсан", "Москва", departure_datetime_2, "Санкт-Петербург", destination_datetime_2, 2600)

    print(2)
    departure_datetime_3 = departure_day.replace(hour=9, minute=30)
    destination_datetime_3 = departure_day.replace(hour=13, minute=25)
    sapsan_3 = Train("760", "Сапсан", "Москва", departure_datetime_3, "Санкт-Петербург", destination_datetime_3, 2700)

    print(3)
    departure_datetime_4 = departure_day.replace(hour=13, minute=30)
    destination_datetime_4 = departure_day.replace(hour=17, minute=30)
    sapsan_4 = Train("768", "Сапсан", "Москва", departure_datetime_4, "Санкт-Петербург", destination_datetime_4, 2700)

    print(4)
    departure_datetime_5 = departure_day.replace(hour=15, minute=30)
    destination_datetime_5 = departure_day.replace(hour=19, minute=40)
    sapsan_5 = Train("772", "Сапсан", "Москва", departure_datetime_5, "Санкт-Петербург", destination_datetime_5, 2700)

    print(5)
    departure_datetime_6 = departure_day.replace(hour=19, minute=30)
    destination_datetime_6 = departure_day.replace(hour=23, minute=37)
    sapsan_6 = Train("778", "Сапсан", "Москва", departure_datetime_6, "Санкт-Петербург", destination_datetime_6, 3000)

    print(6)
    departure_datetime_7 = departure_day.replace(hour=5, minute=30)
    destination_datetime_7 = departure_day.replace(hour=9, minute=18)
    sapsan_7 = Train("751", "Сапсан", "Санкт-Петербург", departure_datetime_7, "Москва", destination_datetime_7, 2000)

    print(7)
    departure_datetime_8 = departure_day.replace(hour=13, minute=0)
    destination_datetime_8 = departure_day.replace(hour=17, minute=0)
    sapsan_8 = Train("767", "Сапсан", "Санкт-Петербург", departure_datetime_8, "Москва", destination_datetime_8, 2300)

    print(8)
    departure_datetime_9 = departure_day.replace(hour=17, minute=0)
    destination_datetime_9 = departure_day.replace(hour=20, minute=50)
    sapsan_9 = Train("775", "Сапсан", "Санкт-Петербург", departure_datetime_9, "Москва", destination_datetime_9, 2500)

    print(9)
    departure_datetime_10 = departure_day.replace(hour=19, minute=10)
    destination_datetime_10 = departure_day.replace(hour=23, minute=15)
    sapsan_10 = Train("781", "Сапсан", "Санкт-Петербург", departure_datetime_10, "Москва", destination_datetime_10, 2000)


    for sapsan in (sapsan_1, sapsan_2, sapsan_3, sapsan_4, sapsan_5, sapsan_6, sapsan_7, sapsan_8, sapsan_9, sapsan_10):
        for passenger in sapsan.passengers:
            data.append({
                "ФИО": passenger.name,
                "Паспорт": passenger.passport,
                "Откуда": sapsan.departure_city,
                "Куда": sapsan.destination_city,
                "Дата отъезда": sapsan.departure_datetime.strftime("%d %B %Y, %H:%M:%S"),
                "Дата приезда": sapsan.destination_datetime.strftime("%d %B %Y, %H:%M:%S"),
                "Рейс": sapsan.number,
                "Вагон и место": f"{passenger.wagon}-{passenger.seat}",
                "Стоимость": passenger.cost,
                "Карта оплаты": passenger.cost
            })
    
df = pd.DataFrame(data)

df.to_csv("train_tickets.csv", index=False)
