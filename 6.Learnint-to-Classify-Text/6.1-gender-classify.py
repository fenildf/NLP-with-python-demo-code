import nltk
from nltk.corpus import names
import random

def gender_features(word):
    return {'last_letter':word[-1]}

#get data
names = ([(name,'male') for name in names.words('male.txt')]+
         [(name,'female') for name in names.words('female.txt')])
random.shuffle(names)

#train
feature_set = [(gender_features(n),g) for (n,g) in names]
train_set,test_set = feature_set[500:],feature_set[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

#test
print classifier.classify(gender_features('Ron'))


