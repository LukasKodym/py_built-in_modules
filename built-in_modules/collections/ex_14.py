##

from collections import ChainMap

default_setting = {'mode': 'eco', 'power_level': '7'}
user_setting = {}

settings = ChainMap(user_setting, default_setting)

print(settings['mode'])
