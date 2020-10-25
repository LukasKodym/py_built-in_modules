##

from collections import Counter

poll_1 = {'yes': 140, 'no': 120, None: 12}
poll_2 = {'yes': 113, 'no': 132, None: 9}
poll_3 = {'yes': 16, 'no': 14}

c_poll_1 = Counter(poll_1)
c_poll_2 = Counter(poll_2)
c_poll_3 = Counter(poll_3)

res = c_poll_1 + c_poll_2 + c_poll_3

print(res.get('yes'))
# print(res['yes'])
