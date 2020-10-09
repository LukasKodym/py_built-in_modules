import os

base_dir = "images_2"
dir_names = [os.path.join(base_dir, base_dir + i) for i in ['_jpg', '_png']]

for name in dir_names:

    if not os.path.exists(base_dir):
        os.mkdir(base_dir)

    if not os.path.exists(name):
        os.mkdir(name)

for root, dirs, files in os.walk(base_dir):
    print(root)
