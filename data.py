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
    "Сбер": {
        "Мир": 0.1,
        "Visa": 0.1,
        "Mastercard": 0.1
    },

    "Т-Банк": {
        "Мир": 0.1,
        "Visa": 0.1,
        "Mastercard": 0.1 
    },

    "ГазпромБанк": {
        "Мир": 0.1,
        "Visa": 0.1,
        "Mastercard": 0.2 
    }
}

pairs = [(bank, payment_system) for bank in bank_chance for payment_system in bank_chance[bank]]
weights = [bank_chance[bank][payment_system] for bank, payment_system in pairs]


class Passenger:
    def __init__(self, cost:int, wagon:int, seat:int):
        global used_passports, used_cards
        self.name = Faker("ru_RU").name()
        self.cost = cost
        self.wagon = wagon
        self.seat = seat
        self.passport = self.generate_passport() 
        self.card:int = self.generate_card()


    def generate_passport(self) -> str:
        global used_passports
        passport = f"{random.randint(1000, 9999)} {random.randint(100000, 999999)}"
        while passport in used_passports:
            passport = f"{random.randint(1000, 9999)} {random.randint(100000, 999999)}"
        used_passports.add(passport)
        return passport


    def generate_card(self) -> int:
        global used_cards_counter, cards_bin, pairs, weights
        random_pair = random.choices(pairs, weights=weights, k=1)[0]
        bank = random_pair[0]
        payment_system = random_pair[1]
        bin = str(cards_bin[bank][payment_system]) 
        card = bin + str(random.randint(10**10, (10**11)-1))
        card = int(card)
        if card in used_cards_counter:
            if used_cards_counter[card] >= 5:
                return self.generate_card()
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
        if self.type_of_train == "Сапсан":
            passengers = set()
            
            for i in range(1, 19):
                passengers.add(Passenger(self.base_cost*10, 1, i))

            for i in range(1, 45):
                passengers.add(Passenger(self.base_cost*5, 2, i))

            for i in range(1, 67):
                passengers.add(Passenger(self.base_cost, 3, i))

            for i in range(1, 67):
                passengers.add(Passenger(self.base_cost*2, 4, i))

            for i in range(1, 41):
                passengers.add(Passenger(int(self.base_cost*1.2 + 2000), 5, i))

            for i in range(1, 55):
                passengers.add(Passenger(self.base_cost, 6, i))

            for i in range(1, 67):
                passengers.add(Passenger(self.base_cost, 7, i))

            for i in range(1, 68):
                passengers.add(Passenger(self.base_cost, 8, i))

            for i in range(1, 68):
                passengers.add(Passenger(self.base_cost, 9, i))

            for i in range(1, 44):
                passengers.add(Passenger(self.base_cost*2, 10, i))

            return passengers

        return set()
