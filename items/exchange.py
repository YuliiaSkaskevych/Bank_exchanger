import json
import requests
import csv
from items.currency import Currency
from items.money import Money

def decor(method):
    def inner(x,y,z,n):
        a = "-"*40
        print(a)
        method(x,y,z,n)
        print(a)
    return inner

def decor2(method):
    def inner(x,y,z,n,m):
        a = "-"*40
        print(a)
        method(x,y,z,n,m)
        print(a)
    return inner

try:
    get_request = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
    if get_request.status_code == 200:
        get = json.loads(get_request.content)
        with open("course", "w") as f:
            json.dump(get, f)
except requests.exceptions.ConnectionError:
    print("No internet connection")

read_money = open("src\\bank_exchange\items\\amount", "r")
money = csv.DictReader(read_money, delimiter=",", quoting=csv.QUOTE_MINIMAL)
currency_amount=[]
for i in money:
    currency_amount.append(i)
dic_amount={}
for i in currency_amount:
    dic_amount[i['cur']]=(i['amount'])
    amount=[dic_amount]

with open("course") as file:
    currency_course=json.load(file)
    for item in currency_course:
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
        self.money = [Money(float(i['USD']),float(i['UAH'])) for i in amount]

    def greetings(self):
        print("Welcome to ARSENALBANK!", "You can choose any of the available options:",
              "To view the exchange rate - enter COURSE (enter the desired currency)",
              "To exchange currency - enter EXCHANGE (enter the desired currency + amount)",
              "To exit from programme - enter STOP", "Please enter your choice: ", sep="\n")
    @decor
    def course(self, course, amount, valuta):
        for item in course:
            for i in amount:
                if item.ccy == valuta:
                    print(f"RATE {round(item.sale,1)} AVAILABLE {round(i.USD,2)}")
                    break
                elif item.base_ccy == valuta:
                    print(f"RATE {round(item.buy,1)} AVAILABLE {round(i.UAH,2)}")
                    break
                else:
                    print(f"INVALID CURRENCY {valuta}")
                    break

    @decor2
    def change(self, course, amount, valuta, price):
        for item in course:
            for i in amount:
                try:
                    price=float(price)
                    assert price > 0
                    if item.ccy == valuta:
                        c = price * item.buy
                        if c < i.UAH:
                            i.UAH -= c
                            i.USD += price
                            print(f'{item.base_ccy} = {round(c,2)} | RATE {round(i.UAH,2)}')
                            ch = {'cur': 'amount', 'USD': i.USD, 'UAH': i.UAH}
                            with open("src\\bank_exchange\items\\amount", "w") as file:
                                for key, value in ch.items():
                                    file.write(f'{key},{value}\n')
                            break
                        else:
                            print(f'UNAVAILABLE, REQUIRED BALANCE UAH {round(i.UAH,2)}, AVAILABLE {round(c,2)}')
                            break
                    elif item.base_ccy == valuta:
                        c = price / item.sale
                        if c < i.USD:
                            i.USD -= c
                            i.UAH += price
                            print(f'{item.ccy} = {round(c,2)} | RATE {round(i.USD,2)}')
                            ch = {'cur': 'amount', 'USD': i.USD, 'UAH': i.UAH}
                            with open("src\\bank_exchange\items\\amount", "w") as file:
                                for key, value in ch.items():
                                    file.write(f'{key},{value}\n')
                            break
                        else:
                            print(f'UNAVAILABLE, REQUIRED BALANCE USD {round(i.USD,2)}, AVAILABLE {round(c,2)}')
                            break
                    else:
                        print(f"INVALID CURRENCY {valuta}")
                except ValueError:
                    print("Incorrect input! Enter correct amount!")
                except AssertionError:
                    print("Amount must be positive!")



