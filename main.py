#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 11:35:58 2022

@author: lefteris

@subject: main section of Qapp
"""


from quote_model import Quote #TODO
from data import quote_data #TODO
from quote_brain import QuoteBrain #TODO
from ui import QappInterface #TODO
import random

quote_bank = []
for dim, quote in quote_data.items():
    
    for text in quote:
        new_quote = Quote(dim,text)
        quote_bank.append(new_quote)


random.shuffle(quote_bank)
psy_test = QuoteBrain(quote_bank)
psy_ui = QappInterface(psy_test)

print("You've completed the test")

#TODO: predict personality

#print(f"You are a : ")
