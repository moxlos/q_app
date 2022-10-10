#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 21:19:12 2022

@author: lefteris

@subject: Quote Barain
"""

import html

class QuoteBrain:

    def __init__(self, q_list):
        self.quote_number = 0
        self.score = {y:0 for y in set([x.dim for x in q_list])}
        self.quote_list = q_list
        self.current_quote = None

    def still_has_quotes(self):
        return self.quote_number < len(self.quote_list)

    def next_quote(self):
        self.current_quote = self.quote_list[self.quote_number]
        self.quote_number += 1
        q_text = html.unescape(self.current_quote.quote.text)
        return f"Q.{self.quote_number}: {q_text} (Like/Dislike): "
        
    
    def check_answer(self, user_answer):
        if user_answer.lower() == 'like':
            self.score[self.current_quote.dim] += 1
        elif user_answer.lower() == 'dislike':
            self.score[self.current_quote.dim] -= 1
        else: pass

        




