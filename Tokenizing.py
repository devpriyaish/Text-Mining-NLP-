import os
import nltk
import nltk.corpus
print(os.listdir(nltk.data.find("corpora")))

AI = 'In computer science, artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Computer science defines AI research as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.[1] Colloquially, the term "artificial intelligence" is used to describe machines that mimic "cognitive" functions that humans associate with other human minds, such as "learning" and "problem solving".[2]'

type(AI)

#importing word tokenizer
from nltk.tokenize import word_tokenize

#tokenizing
AI_tokens = word_tokenize(AI)
#printing tokens
AI_tokens

#printing length of the token
len(AI_tokens)

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

#prints the number of paragraphs
from nltk.tokenize import blankline_tokenize
AI_blank = blankline_tokenize(AI)
len(AI_blank)

#working with bigrams, trigrams & ngrams
#importing
from nltk.util import bigrams, trigrams, ngrams

#string on which we will perform bigram, trigram & ngram
string = "The best & most beautiful things in the world cannot be seen or even touched, they must be felt with the heart."
quotes_tokens = nltk.word_tokenize(string)
quotes_tokens

#bigram
quotes_bigrams = list(nltk.bigrams(quotes_tokens))
quotes_bigrams

#trigram
quotes_trigrams = list(nltk.trigrams(quotes_tokens))
quotes_trigrams

#ngram
quotes_ngrams = list(nltk.ngrams(quotes_tokens,5))
quotes_ngrams



