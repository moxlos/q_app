#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Ntovoris Eleftherios (lefteris)

@subject: ui interface
"""

import tkinter as tk
from quote_brain import QuoteBrain

THEME_COLOR = "#375362"

class QappInterface():
    
    def __init__(self, quote_brain: QuoteBrain):
        self.test = quote_brain
        
        self.window = tk.Tk()
        self.window.title("Qapp")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = tk.Canvas(width=700, height=500, bg='white')
        self.quote_text = self.canvas.create_text(
            400,
            200,
            width = 500,
            text="Some Quote here",
            fill=THEME_COLOR,
            font = ('Arial', 12,'italic'))
        self.canvas.grid(row=1,column=0, columnspan=2, pady=50)
        
        like_image = tk.PhotoImage(file='images/like.png')
        self.like_button = tk.Button(image =like_image,
                                     highlightthickness=0,
                                     command = self.like_pressed)
        self.like_button.grid(row=2,column=0)
        
        dislike_image = tk.PhotoImage(file='images/dislike.png')
        self.dislike_button = tk.Button(image =dislike_image,
                                      highlightthickness=0,
                                      command = self.dislike_pressed)
        self.dislike_button.grid(row=2,column=1)
        
        self.get_next_quote()
        
        self.window.mainloop()


    def get_next_quote(self):
        self.canvas.config(bg='white')
        if self.test.still_has_quotes():
            q_text = self.test.next_quote()
            self.canvas.itemconfig(self.quote_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quote_text,
                                   text='You have reached the end of the test\n'+self.print_hist())
            
            self.like_button.config(state='disabled')
            self.dislike_button.config(state='disabled')

    def like_pressed(self):
        self.test.check_answer('Like')
        self.window.after(1000, self.get_next_quote)

    def dislike_pressed(self):
        self.test.check_answer('Dislike')
        self.window.after(1000, self.get_next_quote)

        
    def print_hist(self):
        string_hist = ''
        sorted_score = dict(sorted(self.test.score.items(), key=lambda item: -item[1]))
        for dim, val in sorted_score.items():
            tmp_sting = '*' *val if val >= 0  else '-' *abs(val)
            string_hist += (dim + tmp_sting)
            string_hist += '\n'
            
        return string_hist
        















