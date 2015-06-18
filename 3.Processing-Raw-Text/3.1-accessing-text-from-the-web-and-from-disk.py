# import chapter3

import nltk
from urllib import urlopen

url="http://www.gutenberg.org/"
raw = urlopen(url).read()

# str type
print type(raw)
print len(raw)
print raw[:20]

# type token
tokens = nltk.word_tokenize(raw)
print type(tokens)
print len(tokens)
print tokens[:30]

# type text
text = nltk.Text(tokens)
print type(text)
print text[:30]
print text.collocations()

# print tokens.len()
# print text.len()
