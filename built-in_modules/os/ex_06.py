import os

os.mkdir('documents')

dir_names = [f'{str(i).zfill(2)}_sales' for i in range(1, 13)]

for names in dir_names:
    x = os.path.join('documents', names)
    os.mkdir(x)

dir(os.path)

print(sorted(os.listdir('documents')))

""" this solution is very simple but takes more time
os.mkdir('documents')

os.mkdir('documents/01_sales')
os.mkdir('documents/02_sales')
os.mkdir('documents/03_sales')
os.mkdir('documents/04_sales')
os.mkdir('documents/05_sales')
os.mkdir('documents/06_sales')
os.mkdir('documents/07_sales')
os.mkdir('documents/08_sales')
os.mkdir('documents/09_sales')
os.mkdir('documents/10_sales')
os.mkdir('documents/11_sales')
os.mkdir('documents/12_sales')

print(sorted(os.listdir('documents')))
"""
