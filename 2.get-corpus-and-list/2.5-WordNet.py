import nltk
from nltk.corpus import wordnet as wn

# print the synset of motorcar
print wn.synsets('motorcar')

# method of synset
print wn.synset('car.n.01').lemma_names()
print wn.synset('car.n.01').definition()
print wn.synset('car.n.01').examples()

# get all the lemmas for a given synset
print wn.synset('car.n.01').lemmas()

#look up a particular lemma
print wn.lemma('car.n.01.automobile')

# get the synset corresponding to a lemma
print wn.lemma('car.n.01.automobile').synset()

# get the name of lemma
wn.lemma('car.n.01.automobile').name

