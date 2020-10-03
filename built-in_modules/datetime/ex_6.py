from datetime import datetime

d1 = datetime(2021, 4, 20, 11, 30)

print(d1.strftime("%Y-%m-%d"))
print(d1.strftime("%d-%m-%Y"))
print(d1.strftime("%m-%Y"))
print(d1.strftime("%B-%Y"))
print(d1.strftime("%d %B, %Y"))
print(d1)
print(d1.strftime("%m/%d/%y %H:%M:%S"))
print(d1.strftime("%d(%a) %B %Y"))
