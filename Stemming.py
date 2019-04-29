#Stemming - Normalize words into its base form or root form
import os
import nltk
import nltk.corpus

#importing stemmer
#PorterStemmer
from nltk.stem import PorterStemmer
pst = PorterStemmer()

words_to_stem = ['give', 'giving', 'given', 'gave']
for words in words_to_stem:
    print(words + ':' + pst.stem(words))
#LancasterStemmer
from nltk.stem import LancasterStemmer
lst = LancasterStemmer()
for words in words_to_stem:
    print(words + ':' + lst.stem(words))
