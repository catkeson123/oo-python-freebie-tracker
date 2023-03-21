import ipdb
from lib import *

# code here

c1 = Company("My Company", 2020)
d1 = Dev("My Developer")
d2 = Dev("New Developer")
f1 = Freebie("T-shirt", 40, d1, c1)
f2 = Freebie("Hat", 20, d2, c1)

ipdb.set_trace()
