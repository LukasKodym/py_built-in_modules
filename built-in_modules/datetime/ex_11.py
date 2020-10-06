import datetime

dt = datetime.datetime(2020, 1, 1)

dates = [dt + datetime.timedelta(hours=i) for i in range(0, 8 * 12, 8)]

for i in dates:
    print(i)
