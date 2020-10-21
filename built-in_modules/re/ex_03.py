##

import re

code = '0010-000-423'

print(re.compile('[1-9]').findall(code))

# re.findall(r'[^0-]', code)
