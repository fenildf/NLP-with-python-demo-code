import nltk
import codecs

path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')

f = codecs.open(path,encoding='latin2')

for line in f:
    line = line.strip()
    print line.encode('unicode_escape')

print ord('a')

a = u'\u0061'
print a 

nacute = u'\u0144'
print nacute

nacute_utf = nacute.encode('utf-8')
print repr(nacute_utf)
print nacute_utf
