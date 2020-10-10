import os

fnames = [f'{str(i).zfill(2)}_sales.csv' for i in range(1, 25)]

y_20 = '2020'
y_21 = '2021'

for name in sorted(fnames):
    if len(fnames) < 13:
        d_20 = os.path.join(os.getcwd(), y_20, name)
    else:
        d_21 = os.path.join(os.getcwd(), y_21, name)

