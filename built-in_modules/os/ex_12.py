import os

folder = 'paths'

paths = [os.path.join(folder, f'dir_{str(i).zfill(2)}') for i in range(1, 14)]

for path in paths:

    if not os.path.exists(folder):
        os.mkdir(folder)

    if not os.path.exists(path):
        os.mkdir(path)

os.rmdir(paths[-1])
os.chdir(folder)

print([name for name in sorted(os.listdir()) if len(name) == 6])
