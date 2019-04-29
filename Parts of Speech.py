#Parts Of Speech
import os
import nltk

#importing word tokenizer
from nltk.tokenize import word_tokenize

#gives the POS for each tokens in both the cases
#case 1
sent = "Timothy is a natural when it comes to drawing"
sent_tokens = word_tokenize(sent)
sent_tokens

for token in sent_tokens:
    print(nltk.pos_tag([token]))

#case 2
sent2 = "Shivani is eating a delicious cake"
sent2_tokens = word_tokenize(sent2)
for token in sent2_tokens:
    print(nltk.pos_tag([token]))
