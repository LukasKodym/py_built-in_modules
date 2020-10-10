import os

fnames = [f'{str(i).zfill(3)}_sales.csv' for i in range(1, 25)]

paths = []

for name in fnames:
    paths.append(os.path.join(os.getcwd(), name))

# paths = [os.path.join(os.getcwd(), name) for name in fnames]

print(paths)
