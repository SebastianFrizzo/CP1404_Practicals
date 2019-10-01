class Date:
    def __init__(self, day=1, month=1, year=1):
        """
        Initialises the Date class
        """
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "{}/{}/{}".format(self.day, self.month, self.year)

    def add_days(self, n_of_days):
        if self.day + n_of_days > 31:
            self.month += 1
            self.day += (n_of_days - 31)
        else:
            self.day += n_of_days
