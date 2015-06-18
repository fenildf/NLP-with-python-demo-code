# Error:p51 code,forget a ")" in the last line

import nltk;
from nltk.corpus import udhr;

languages = ['Chickasaw','English','Greenlandic_Inuktikut','Hungarian_Magyar','Ibibio_Efik'];

cfd = nltk.ConditionalFreqDist(
        (lang,len(word))
        for lang in languages
        for word in udhr.words(lang+'-Latin1'))

cfd.plot(cumulative=True)
