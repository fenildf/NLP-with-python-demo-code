import nltk

from nltk.corpus import swadesh

# swadesh dict
print swadesh.fileids()
print swadesh.words('en')

# a samlple dict
fr2en = swadesh.entries(['fr','en'])
print fr2en[:5]
translate = dict(fr2en)
print translate['chien']
print translate['jeter']

# compare germ with latin
language = ['en','de','nl','es','fr','pt','la']
for i in [139,140,141,142]:
    print swadesh.entries(language)[i]
