import re
import nltk
wordlist = [w for  w in nltk.corpus.words.words('en') if w.islower()]

# end with 'ed'
print [w for w in wordlist if re.search('ed$',w)]

# ..j..t..$
print [w for w in wordlist if re.search('^..j..t..$',w)]

# T9
print [w for w in wordlist if re.search('^[ghi][mno][jlk][def]$',w)]
