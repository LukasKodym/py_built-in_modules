##

import re

text = 'Please send an email to info@template.com or call to: 123-456-789'

print(re.sub(r'\d{3}-\d{3}-\d{3}', '***-***-***', text))
