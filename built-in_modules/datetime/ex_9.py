import datetime

today = datetime.datetime.today()

dt = datetime.datetime(today.year + 1, 1, 1)

res = dt - today

print(f'Until the end of the year: {res}')
