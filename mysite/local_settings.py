# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 13:20:25 2017

@author: supvicp123
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True