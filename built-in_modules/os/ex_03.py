import os

lst = os.listdir()

names = [i for i in lst if i.startswith('e')]

print(sorted(names))
