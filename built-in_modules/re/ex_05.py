##
import re

code = 'PL code: XG-GH-110'
res = re.findall(pattern=r'PL|\d+', string=code)
print(res)
