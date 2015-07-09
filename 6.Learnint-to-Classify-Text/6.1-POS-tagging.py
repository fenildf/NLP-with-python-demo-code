import nltk
from nltk.corpus import brown

suffix_fdist = nltk.FreqDist()
for word in brown.words():
    word = word.lower()
    suffix_fdist.inc(word[-1:])
    suffix_fdist.inc(word[-2:])
    suffix_fdist.inc(word[-3:])

common_suffix = suffix_fdist.keys()[:100]
print common_suffix