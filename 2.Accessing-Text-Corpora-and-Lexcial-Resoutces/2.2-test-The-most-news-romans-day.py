import nltk;
from nltk.corpus import brown;

week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'];

# files =  for fileid in brown.fileids();

cfd = nltk.ConditionalFreqDist(
        (days,fileid)
        for fileid in brown.fileids(["news","romance"])
        for w in brown.words(fileid)
        for days in week
        if w.lower().startswith(days) )

cfd.plot();


