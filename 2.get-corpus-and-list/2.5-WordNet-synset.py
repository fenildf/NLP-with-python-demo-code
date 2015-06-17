import nltk
from nltk.corpus import wordnet as wn

motorcar = wn.synset('car.n.01')
types = motorcar.hyponyms()
print types[26]

# code in books forget 2()
print sorted([lemma.name() for synset in types for lemma in synset.lemmas()])

