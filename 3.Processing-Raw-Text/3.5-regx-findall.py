
import re
word = 'supercalifragilisticexpialidocious'

print re.findall(r'[aeiou]',word)

print len(re.findall(r'[aeiou]',word))

# find two or more [aeiou] and their freqdist

import nltk

wsj = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist(vs for word in  wsj
        for vs in re.findall(r'[aeiou]{2,}',word))

print fd.items()
