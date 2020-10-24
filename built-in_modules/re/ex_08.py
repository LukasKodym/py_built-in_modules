##

import re

text = "Please send an email to info@template.com or sales-info@template.it"

print(re.findall(r'[\w\.-]+@[\w\.-]+', text))
