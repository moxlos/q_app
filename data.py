#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: lefteris

@subject: data for Qapp
"""

import requests
from bs4 import BeautifulSoup


#TODO Get it real
dimensions = [('extrovert', 'E', 'Society'),
              ('introvert', 'I', 'Friendship'),
              ('intuition', 'N','Intuition'),
              ('senses','S', 'Senses'),
              ("feeling",'F', 'Feelings'),
              ('judging','J', 'Judgment'),
              ('perceiving','P', 'Perception')]

quote_data = {}

for dim in dimensions:
    response = requests.get(
    	url="https://en.wikiquote.org/wiki/" + dim[2],
    ).text
    soup = BeautifulSoup(response, 'html5lib')
    print(soup.title)    
    
    #TODO return random
    quotes = soup.find_all('li', {'class': None}, limit = 10)
    quote_data[dim[2]] = [quotes[i] for i in [0,2,4]]
    
    






