class Guitar:
    def __init__(self, name='', year=0, price=0):
        self.name = name
        self.price = price
        self.year = year

    def __str__(self):
        return "{} made in the year {}, costs ${}".format(self.name, self.year, self.price)

    def __lt__(self, other):
        return self.year > other
