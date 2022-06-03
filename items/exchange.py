import json
import requests
import csv
from items.currency import Currency
from items.money import Money

read_money = open("C:\\Users\Admin\PycharmProjects\src\\bank_exchange\items\\amount", "r")
money = csv.DictReader(read_money, delimiter=",", quoting=csv.QUOTE_MINIMAL)
currency_amount=[]
dic={}
for i in money:
    currency_amount.append(i)
for a in currency_amount:
    if a['cur'] == "USD":
        print(a['amount'])
    if a['cur'] == "UAH":
        print(a['amount'])

get_request = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
if get_request.status_code == 200:
    get = json.loads(get_request.content)
    with open("course", "w") as f:
        json.dump(get, f)
    with open("course") as file:
        course=json.load(file)
    for item in course:
        if item["ccy"] == "USD":
            d = [item]


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Exchange(metaclass=SingletonMeta):

    def __init__(self):
        self.currency = [Currency(item["ccy"], item["base_ccy"], float(item["buy"]), float(item["sale"])) for item in d]
        self.money = [Money(i['cur'], float(i['amount'])) for i in currency_amount]

    def greetings(self):
        print("Welcome to ARSENALBANK!", "You can choose any of the available options:")
        print("To view the exchange rate - enter COURSE (enter the desired currency)",
              "To exchange currency - enter EXCHANGE (enter the desired currency + amount)",
              "To exit from programme - enter STOP", "Please enter your choice: ", sep="\n")

    def course(self, course, amount, want):
        for item in course:
            for i in amount:
                if item.ccy == want:
                    print(f"RATE {item.buy} AVAILABLE {i.amount}")
                    break
                elif item.base_ccy == want:
                    print(f"RATE {item.sale} AVAILABLE {i.amount}")
                    break
                else:
                    print(f"INVALID CURRENCY {want}")
                    break


    def change(self, course, amount, want, price):
        for item in course:
            for i in amount:
                try:
                    price=float(price)
                    i.UAH = float(i.UAH)
                    i.USD = float(i.USD)
                    assert price > 0
                    if item.ccy == want:
                        c = price * item.buy
                        if c < i.UAH:
                            i.UAH-=c
                            print(f'{item.base_ccy}={c} RATE {i.UAH}')
                            break
                        else:
                            print(f'UNAVAILABLE, REQUIRED BALANCE UAH {i.UAH}, AVAILABLE {c}')
                            break
                    elif item.base_ccy == want:
                        c = price // item.sale
                        if c < i.USD:
                            i.USD -= c
                            print(f'{item.ccy}={c} RATE {i.USD}')
                            break
                        else:
                            print(f'UNAVAILABLE, REQUIRED BALANCE USD {i.USD}, AVAILABLE {c}')
                            break
                    else:
                        print(f"INVALID CURRENCY {want}")
                except ValueError:
                    print("Incorrect input! Enter correct amount!")
                except AssertionError:
                    print("Amount must be positive!")



