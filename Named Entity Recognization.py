#Named Entity Recognization
import os
import nltk

#importing word tokenizer
from nltk.tokenize import word_tokenize

from nltk import ne_chunk

#case1
NE_sent = "The US President stays in the White House"
NE_tokens = word_tokenize(NE_sent)
NE_tags = nltk.pos_tag(NE_tokens)
NE_tags

#prints NER in tree representation
NE_NER = ne_chunk(NE_tags)
NE_NER

#prints NER in normal text
print(NE_NER)

#case2
new = "The big cat ate the little mouse who was after the cheese"
new_tokens = nltk.pos_tag(word_tokenize(new))
new_tokens

#treats DT,JJ&NN as NP
grammar_np = r"NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(grammar_np)
chunk_result = chunk_parser.parse(new_tokens)
chunk_result
