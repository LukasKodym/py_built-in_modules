from datetime import datetime, timedelta

dt = datetime(2020, 1, 1)

dt_7d = dt + timedelta(days=7)
dt_30d = dt + timedelta(days=30)
dt_30h = dt + timedelta(hours=30)
dt_15m = dt + timedelta(minutes=15)

print(dt_7d)
print(dt_30d)
print(dt_30h)
print(dt_15m)
