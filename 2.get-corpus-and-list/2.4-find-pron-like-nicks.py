import nltk
entries = nltk.corpus.cmudict.entries()

syllable = ['N','IH0','K','S']
print [word for word,pron in entries if pron[-4:] == syllable]
