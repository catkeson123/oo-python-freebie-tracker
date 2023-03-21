from .freebie import Freebie


class Company:

    all = []

    def __init__(self, name, fyear):
        self.name = name
        self.fyear = fyear
        Company.all.append(self)

    @property
    def freebies(self):
        return [f for f in Freebie.all if f.company == self]

    @property
    def devs(self):
        return [f.dev for f in Freebie.all if f.company == self]
