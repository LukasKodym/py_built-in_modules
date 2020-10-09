import os
import random

random.seed(30)
images_3 = [f"{str(i).zfill(3)}_image.{random.choice(['png', 'jpg'])}" for i in range(1, 20)]

base_dir = 'images_3'

if not os.path.exists(base_dir):
    os.mkdir(base_dir)

png_dir = os.path.join(base_dir, 'images_png')
jpg_dir = os.path.join(base_dir, 'images_jpg')

if not os.path.exists(png_dir):
    os.mkdir(png_dir)

if not os.path.exists(jpg_dir):
    os.mkdir(jpg_dir)
    for image in images_3:
        if image.endswith('png'):
            if not os.path.exists(image):
                open(image, 'w')


for root, dirs, files in os.walk(base_dir):
    print(root)
    for file in sorted(files):
        print(f"\t{file}")
