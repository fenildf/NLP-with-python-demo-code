
import re
word = 'supercalifragilisticexpialidocious'

print re.findall(r'[aeiou]',word)

print len(re.findall(r'[aeiou]',word))
