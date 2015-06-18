import nltk
import codecs
import unicodedata


path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
lines = codecs.open(path,encoding='latin2').readlines()
line = lines[2]

print line.encode('unicode_escape')
print '-----------utf-8 code----------------' 
for c in line:
    if ord(c) > 127:
        print '%r U+%04x %s' % (c.encode('utf-8'),ord(c),unicodedata.name(c))

print '-----------utf-8 char----------------' 

for c in line:
    if ord(c) > 127:
        print '%s U+%04x %s' % (c.encode('utf-8'),ord(c),unicodedata.name(c))
