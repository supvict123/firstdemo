# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 19:07:14 2017

@author: supvicp123
"""

from sklearn.feature_extraction.text import HashingVectorizer
import re
import os
import pickle

cur_dir = os.path.dirname(__file__)
stop = pickle.load(open(os.path.join(cur_dir,'movieclassifier',
                            'pkl_objects', 'stopwords.pkl'), 'rb'))
def tokenizer(text):
    preprocessor(text)
    tokenized = [w for w in text.split() if w not in stop]
    return tokenized

def preprocessor(text):
    text = re.sub('<[^>]*>','', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W]+', ' ', text.lower())+ ''.join(emoticons).replace('-', '')
    return text

vect = HashingVectorizer(decode_error='ignore', n_features=2**21, 
                         preprocessor=None, tokenizer=tokenizer)

