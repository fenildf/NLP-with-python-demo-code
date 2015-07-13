import nltk
import re
import pprint

cp = nltk.RegexpParser('ChUNK:{<V.*><TO><V.*>}')
brown = nltk.corpus.brown

for sent in brown.tagged_sents():
    tree = cp.parse(sent)
    for subtree in tree.subtrees():
        if subtree.node == 'CHUNK':
            print subtree