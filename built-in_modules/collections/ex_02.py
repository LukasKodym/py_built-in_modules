##

from collections import Counter

poll_1 = {'yes': 140, 'no': 120, None: 12}
poll_2 = {'yes': 113, 'no': 132, None: 9}

c_poll_1 = Counter(poll_1)
c_poll_2 = Counter(poll_2)

print(c_poll_1 + c_poll_2)
