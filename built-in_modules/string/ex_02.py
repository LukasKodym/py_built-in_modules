##
from string import Template

names = ['John', 'Paul', 'Lisa', 'Michael']

res = Template('Hello $name,\n\nThank you for visiting our website.\nTeam XYZ\n$sign')

for name in names:
    print(res.substitute(name=name, sign='-' * 35))

