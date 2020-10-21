##

print('Hello', 'World', 2 + 3, file=open('file.txt', 'w'))

##
from string import Template

names = ['John', 'Paul', 'Lisa', 'Michael']

email = """Hello $name,

Thank you for visiting our website.
Team, XYZ"""

template = Template(email)

for name in names:
    print(template.substitute(name=name))
    print('-' * 35)

##
# usage the 'r' prefix in strings

print('this is text \nseparated by new line')
print(r'this is text \nseparated by new line')

##
import re

numbers = '156987156314896dsadfknlasdf09432- -09432 -3 '

print(re.findall(r'[^6a -]', numbers))
