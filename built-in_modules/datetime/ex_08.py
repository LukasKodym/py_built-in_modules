import datetime

dt = datetime.date.today()
de = datetime.date(dt.year, 12, 31)

res = de - dt

print(f'Number of days until the end of the year: {res.days}')
