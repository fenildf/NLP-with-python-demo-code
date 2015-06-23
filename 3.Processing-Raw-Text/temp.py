# test   nltk.ConditionalFreqDist(cvs)
import nltk

dq = ['cs','sb','df'];

cfd = nltk.ConditionalFreqDist(dq)
cfd.tabulate()
