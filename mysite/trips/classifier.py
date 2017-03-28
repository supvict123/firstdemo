# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 00:07:02 2017

@author: supvicp123
"""
#from sklearn.feature_extraction.text import HashingVectorizer
import re
import os
import pickle
import numpy as np
from trips.vectorizer import vect
cur_dir = os.path.dirname(__file__)

class classifier:
    def prediction(self, data):
        'load the stop word and classifier'
        clf = pickle.load(open(os.path.join(cur_dir,'movieclassifier', 'pkl_objects', 'classifier.pkl'), 'rb'))
        label = {0: 'negative', 1: 'positive'}
        X = self.load_data(data)
        return (label[clf.predict(X)[0]],np.max(clf.predict_proba(X))*100)
       
    def load_data(self, data):
        'load the vectorizer'
        data = vect.transform(data)
        return data
    

    