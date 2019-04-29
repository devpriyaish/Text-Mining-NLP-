#Lemmatization
#Groups together different inflected forms of a word called lemma
#Somehow similar to stemming, as it maps several words into one common root
#Output of lemmatization is a proper word
#gone, going, went--> go

import os
import nltk
import nltk.corpus

from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer
word_lem = WordNetLemmatizer()

word_lem.lemmatize('corpora')

words_to_stem = ['give', 'giving', 'given', 'gave']
for words in words_to_stem:
    print(words + ':' + word_lem.lemmatize(words))

from nltk.corpus import stopwords
eng = stopwords.words('english')
eng

len(eng)

AI = 'In computer science, artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Computer science defines AI research as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.[1] Colloquially, the term "artificial intelligence" is used to describe machines that mimic "cognitive" functions that humans associate with other human minds, such as "learning" and "problem solving".[2]'


#frequency calculator
from nltk.probability import FreqDist
fdist = FreqDist()
#word.lower convers all to lower case so that 'All' & 'all' are treated same thing
for word in AI_tokens:
    fdist[word.lower()] += 1
fdist

#printing top 10 most common elements
fdist_top10 = fdist.most_common(10)
fdist_top10

#stopword & punction can be removed
import re
punch = re.compile(r'[-.?!,:;()|0-9]')

#single puncuations are removed & stored in post_punch
post_punch = []
for words in AI_tokens:
    word = punch.sub('',words)
    if len(word)>0:
        post_punch.append(word)

post_punch

#length after removing puncuation symbols
len(post_punch)





