##

import re

text = """Python plays a key role in our production pipeline.
Without it a project the size of Star Wars: Episode II would have been very difficult to pull off."""

print(re.findall(r'[A-Z]\w+', text))
