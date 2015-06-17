# To find words includes 3 morpheme,start with 'P' and end by 'T'
# ----con't run-----
import nltk

entries = nltk.corpus.cmudict.entries

for word,pron in entries:
    if len(pron) == 3:
        ph1,ph2,ph3 = pron
        if ph1 == 'P' and ph3 == 'T':
            print word,ph2,
