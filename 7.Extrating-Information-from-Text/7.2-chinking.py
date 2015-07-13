import nltk
import re
import pprint

sent = [('the','DT'),('little','JJ'),('yellow','JJ'),('dog','NN'),
        ('branked','VBD'),('at','IN'),('the','DT'),('cat','NN')]

grammer = r"""
NP:
{<.*>+}
}<VBD|IN>+{
"""

cp = nltk.RegexpParser(grammer)

result = cp.parse(sent)
print result