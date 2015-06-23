import nltk
import re

from nltk.corpus import toolbox
regexp = r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'

def compress(word):
    pieces = re.findall(regexp,word)
    return ''.join(pieces)

english_udhr = nltk.corpus.udhr.words('English-Latin1')

print nltk.tokenwrap(compress(w) for w in english_udhr[:75])

# draw freqdist for rotokas.dic

rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
cvs = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]',w)]

cfd = nltk.ConditionalFreqDist(cvs)
cfd.tabulate()
