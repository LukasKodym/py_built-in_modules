##

import re

text = 'Python 3.8'

p = re.compile('[0-9]')

print(p.findall(text))
