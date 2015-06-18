# Find the name both for woman and man from nltk.corpus.names

import nltk
from nltk.corpus import names

names = nltk.corpus.names

print names.fileids()

male_name = names.words('male.txt')
female_name = names.words('female.txt')

print [w for w in male_name if w in female_name]


# draw a FreqDist describe the relationship between sex and the last alpha.

# Usually end by 'a e i' is for female
# End by k o r s t is for male.

cfd = nltk.ConditionalFreqDist(
        (fileid,name[-1])
        for fileid in names.fileids()
        for name in names.words(fileid))

cfd.plot()
