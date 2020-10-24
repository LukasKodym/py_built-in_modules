##

import re

message = 'For more information, please call: 123-456-789'

print(re.findall(r'\d.*', message)[0])

# more universal solution, that match to template:
# print(re.findall(r"\d{3}-\d{3}-\d{3}", message)[0])
