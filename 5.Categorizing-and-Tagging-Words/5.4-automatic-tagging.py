from nltk.corpus import brown
import nltk

# get the sents
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

# get tags
tags = [tag for (word,tag) in brown.tagged_words(categories='news')]
# print tags

# all tagged by 'NN'
raw = 'I do now like green eggs and ham,I do not like them Sam I am!'
tokens = nltk.word_tokenize(raw)
default_tagger = nltk.DefaultTagger('NN')
print default_tagger.tag(tokens)
print default_tagger.evaluate(brown_tagged_sents)

# regexp_tagger
patterns = [
    (r'.*ing$','VBG'),
    (r'.*ed$','VBD'),
    (r'.*es$','VBZ'),
    (r'.ould$','MD'),
    (r'.*\'s$','NN$'),
    (r'.*s$','NNS'),
    (r'^-?[0-9]+(.[0-9]+)?$','CD'),
    (r'.*','NN')
]

regexp_tagger = nltk.RegexpTagger(patterns)
print regexp_tagger.tag(brown_sents[3])
print regexp_tagger.evaluate(brown_tagged_sents)