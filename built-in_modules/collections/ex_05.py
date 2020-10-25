##

from collections import Counter

text = 'python programming - introduction'

res = Counter(text)

print(res.most_common(3))
