##
import string

docs = 'programming in python'

code_map = {k: v for (k, v) in enumerate(string.ascii_lowercase)}

code_map_inv = {v: k for k, v in code_map.items()}

res = ''

for i in docs:
    if i == ' ':
        res += ' '
        continue
    idx = (code_map_inv[i] + 3) % 26
    res += code_map[idx]

print(res)
