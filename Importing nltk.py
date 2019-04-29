#Text Mining & NLP Tutorial
import os
import nltk
import nltk.corpus
print(os.listdir(nltk.data.find("corpora")))

nltk.corpus.gutenberg.fileids()

#importing text data named 'shakespeare-hamlet.txt'
hamlet = nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
#printing
hamlet
#printing first 500 words
for word in hamlet[:500]:
    print(word, sep=' ', end=' ')

#taking a string
AI = 'In computer science, artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Computer science defines AI research as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.[1] Colloquially, the term "artificial intelligence" is used to describe machines that mimic "cognitive" functions that humans associate with other human minds, such as "learning" and "problem solving".[2]'

#printing its type
type(AI)
