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

    
    def give_freebie(self, dev, item_name, value):
        return Freebie(item_name, value, dev, self)

    @classmethod
    def oldest_company(cls):
        oldest = cls.all[0]
        for c in cls.all:
            if c.fyear < oldest.fyear:
                oldest=c
        return oldest
        
        
        
        
