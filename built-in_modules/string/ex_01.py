import string

docs = 'programming in python'

code_map = {k: v for (k, v) in enumerate(string.ascii_lowercase)}

code_map_inv = {v: k for k, v in code_map.items()}

res = ''
idx = 0

for i in docs:
    if i:  in code_map_inv.keys():

