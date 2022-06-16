class Money:

    def __init__(self, USD: float, UAH: float):
        self.USD = USD
        self.UAH = UAH

    def __str__(self):
        return f'UAH → {self.UAH} USD → {self.USD}'
