
class Freebie:

    all = []

    def __init__(self, item_name, value, dev, company):
        self.item_name = item_name
        self.value = value
        self.dev = dev
        self.company = company
        Freebie.all.append(self)

    @property
    def print_details(self):
        print(f"{self.dev.name} owns a {self.item_name} from {self.company.name}")

    
