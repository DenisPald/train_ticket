import random
import datetime
from faker import Faker

used_passports:set[str] = set()
used_cards_counter:dict[int, int] = dict()
cards_bin:dict[str, dict[str, int]] = {
    "Сбер": {
        "Мир": 220100,
        "Visa": 400680,
        "Mastercard": 546947
    },

    "Т-Банк": {
        "Мир": 220070,
        "Visa": 437772,
        "Mastercard": 513990 
    },

    "ГазпромБанк": {
        "Мир": 220001,
        "Visa": 411927,
        "Mastercard": 521155 
    }
}

bank_chance:dict[str, dict[str, float]] = {
    # "Сбер": {
    #     "Мир": 1,
    #     "Visa": 1,
    #     "Mastercard": 1
    # },

    # "Т-Банк": {
    #     "Мир": 1,
    #     "Visa": 1,
    #     "Mastercard": 1 
    # },

    # "ГазпромБанк": {
    #     "Мир": 1,
    #     "Visa": 1,
    #     "Mastercard": 1 
    # }
}

banks = ["Сбер", "Т-Банк", "ГазпромБанк"]
cards = ["Мир", "Visa", "Mastercard"]

# Цикл для заполнения данных
for bank in banks:
    bank_chance[bank] = {}
    print(f"Введите веса для банка {bank}:")
    for card in cards:
        while True:
            try:
                chance = float(input(f"Введите вес для карты {card}: "))
                if chance < 0:
                    raise ValueError
                bank_chance[bank][card] = chance
                break
            except ValueError:
                print("Ошибка: введите числовое значение.")


pairs = [(bank, payment_system) for bank in bank_chance for payment_system in bank_chance[bank]]
weights = [bank_chance[bank][payment_system] for bank, payment_system in pairs]

faker = Faker("ru_RU")


class Passenger:
    def __init__(self, cost:int, wagon:int, seat:int):
        global used_passports, used_cards
        self.name:str = self.generate_name()
    
        self.cost:int = cost
        self.wagon:int = wagon
        self.seat:int = seat
        self.passport:str = self.generate_passport() 
        self.card:int = self.generate_card()


    @staticmethod
    def generate_name() -> str:
        global faker
        if random.choice(("Male", "Female")) == "Male":
            return f"{faker.last_name_male()} {faker.first_name_male()} {faker.middle_name_male()}" 

        return f"{faker.last_name_female()} {faker.first_name_female()} {faker.middle_name_female()}" 


    @staticmethod
    def generate_passport() -> str:
        global used_passports
        passport = f"{random.randint(1, 99):02d}{random.randint(0, 24):02d} {random.randint(1, 999999):06d}"
        while passport in used_passports:
            passport = f"{random.randint(1, 99):02d}{random.randint(0, 24):02d} {random.randint(1, 999999):06d}"
        used_passports.add(passport)
        return passport


    @staticmethod
    def generate_card() -> int:
        global used_cards_counter, cards_bin, pairs, weights
        random_pair = random.choices(pairs, weights=weights, k=1)[0]
        bank = random_pair[0]
        payment_system = random_pair[1]
        bin = str(cards_bin[bank][payment_system]) 
        card = bin + str(random.randint(10**10, (10**11)-1))
        card = int(card)
        if card in used_cards_counter:
            if used_cards_counter[card] >= 5:
                return Passenger.generate_card()
            else:
                used_cards_counter[card]+=1
        else:
            used_cards_counter[card] = 1

        return card


class Train:
    def __init__(
        self,
        number:str,
        type_of_train:str,
        departure_city:str,
        departure_datetime:datetime.datetime,
        destination_city:str,
        destination_datetime:datetime.datetime,
        base_cost:int
    ):
        self.number:str = number
        self.type_of_train:str = type_of_train
        self.departure_city:str = departure_city
        self.departure_datetime:datetime.datetime = departure_datetime
        self.destination_city:str = destination_city
        self.destination_datetime:datetime.datetime = destination_datetime
        self.base_cost:int = base_cost
        self.passengers:set[Passenger] = self.generate_passangers()

    def generate_passangers(self) -> set:
        passengers = set()
        if self.type_of_train == "Сапсан":
            
            for i in range(1, 20):
                passengers.add(Passenger(int(self.base_cost*8*random.uniform(0.9, 1.1)), 1, i))

            for i in range(1, 45):
                passengers.add(Passenger(int(self.base_cost*4*random.uniform(0.9, 1.1)), 2, i))

            for i in range(1, 67):
                passengers.add(Passenger(int(self.base_cost*random.uniform(0.9, 1.1)), 3, i))

            for i in range(1, 67):
                passengers.add(Passenger(int(2000+self.base_cost*random.uniform(0.9, 1.1)), 4, i))

            for i in range(1, 41):
                passengers.add(Passenger(int(2000+self.base_cost*random.uniform(0.9, 1.1)), 5, i))

            for i in range(1, 55):
                passengers.add(Passenger(int(self.base_cost*random.uniform(0.9, 1.1)), 6, i))

            for i in range(1, 67):
                passengers.add(Passenger(int(self.base_cost*random.uniform(0.9, 1.1)), 7, i))

            for i in range(1, 68):
                passengers.add(Passenger(int(self.base_cost*random.uniform(0.9, 1.1)), 8, i))

            for i in range(1, 68):
                passengers.add(Passenger(int(self.base_cost*random.uniform(0.9, 1.1)), 9, i))

            for i in range(1, 44):
                passengers.add(Passenger(int(self.base_cost*2*random.uniform(0.9, 1.1)), 10, i))

            return passengers

        elif self.type_of_train == "Ласточка":
            # 10 базовых вагонов
            for i in range(1, 11):
                for j in range(1, 70):
                    passengers.add(Passenger(int(self.base_cost*random.uniform(0.9, 1.1)), i, j))


        return passengers
