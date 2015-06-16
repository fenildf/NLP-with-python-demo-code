
# draw a freqdist plot of "america" and "citizen" in inaugural.
# There is a mistake in line 8,not "file",should be "fileid" (chinese version book)
import nltk;
from nltk.corpus import inaugural;

cfd = nltk.ConditionalFreqDist(
        (target,fileid[:4])
        for fileid in inaugural.fileids()
        for w in inaugural.words(fileid)
        for target in ['america','citizen']
        if w.lower().startswith(target));

cfd.plot();
