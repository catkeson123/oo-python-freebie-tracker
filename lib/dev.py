from .freebie import Freebie


class Dev:

    def __init__(self, name):
        self.name = name

    @property
    def freebies(self):
        return [f for f in Freebie.all if f.dev == self]

    @property
    def companies(self):
        return [f.company for f in self.freebies]

    def received_one(self, item_name):
        # for f in self.freebies:
        #     if f.item_name == item_name:
        #         return True
        # return False
        new_list = [f.item_name for f in self.freebies]
        return True if item_name in new_list else False

    def give_away(self, dev, freebie):
        if freebie in self.freebies:
            freebie.dev = dev
        else:
            print("Freebie does not belong to dev")
    
    
