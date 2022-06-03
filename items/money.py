
class Money:

    def __init__(self, cur, amount: float):
        self.cur = cur
        self.amount = amount

    def __str__(self):
        return f'{self.cur} → {self.amount}'
