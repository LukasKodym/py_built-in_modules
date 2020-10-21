##

import re

code = '0010-000-423-22'

print(re.split(r'\D', code))

# print(re.split('-', code))
