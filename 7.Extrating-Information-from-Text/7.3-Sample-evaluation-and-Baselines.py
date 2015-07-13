from nltk.corpus import conll2000
import nltk

cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('test.txt',chunk_types=['NP'])
print cp.evaluate(test_sents)

grammer = r"NP:{<[CDJNP].*>+}"
cp = nltk.RegexpParser(grammer)
print cp.evaluate(test_sents)