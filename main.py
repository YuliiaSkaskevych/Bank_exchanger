from items.exchange import Exchange
exchange = Exchange()
exchange.greetings()

while True:
    try:
        options = input()
        g=options.upper()
        o = g.split()
        if o[0] == "COURSE" and len(o) == 2:
            exchange.course(exchange.currency, exchange.money, o[1])
        elif o[0] == "EXCHANGE" and len(o) == 3:
            exchange.change(exchange.currency, exchange.money, o[1], o[2])
        elif options == "STOP" and len(o) == 1:
            print("Good luck!")
            break
        else:
            print("Incorrect input! Try again!")
    except ValueError:
        print("Incorrect input! You need to enter correct options!!")
    except IndexError:
        print("Error! No options!")




