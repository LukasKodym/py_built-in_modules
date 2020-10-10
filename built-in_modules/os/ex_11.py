import os

fnames = [f'{str(i).zfill(2)}_sales.csv' for i in range(1, 25)]

y_20 = '2020'
y_21 = '2021'
i = 0

for name in sorted(fnames):

    if i < 12:
        print(os.path.join(os.getcwd(), y_20, name))
    else:
        print(os.path.join(os.getcwd(), y_21, name))
    i += 1
