import datetime

rate = 0.04
pv = 1000

dt1 = datetime.datetime(2021, 7, 1)
dt2 = datetime.datetime(2021, 12, 31)

diff = (dt2 - dt1).days

res = pv * ((1 + (rate / 365)) ** diff)

print(f'Future value: {res:.2f} USD')
