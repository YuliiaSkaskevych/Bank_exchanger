
from items.exchange import Exchange
exchange = Exchange()
exchange.greetings()
while True:
        try:
            options = input()
            o = options.split()
            if o[0] == "COURSE":
                exchange.course(exchange.currency, exchange.money, o[1])
            elif o[0] == "EXCHANGE":
                exchange.change(exchange.currency, exchange.money, o[1], o[2])
            elif options == "STOP":
                print("Good luck!")
                break
            else:
                print("Incorrect input! Try again!")
        except ValueError:
            print("Incorrect input! Try again!")
        except IndexError:
            print("Incorrect input! Try again!")




