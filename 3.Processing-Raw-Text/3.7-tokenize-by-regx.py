

import re
raw = """"'When I'M a Duchess,'she said to herself,(not in a very hopeful tone
though),'I won't have any pepper in my kitchen AT ALL.Soup does very hot-tempered,'..."""

print re.split(r' ',raw)

print re.split(r'[ \t\n]+',raw) # = r'\s+' 

print re.split(r'\W+',raw)
print raw.split(r'[\W+]') # = r'\s+' 

# hte final regx

print re.findall(r"\w+(?:[-']\w+)*|'|[-.)]+|\S\w*",raw)
