#!/usr/bin/python3
# trivia_game.py
# Lane D. and Dominic M.
# 9/3/2020

''' Program to ask the user trivia questions and log high scores'''

import pickle as pk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import random as rd

TITLE_FONT = ("Times New Roman", 24)
WIDGET_FONT = ("Arial", 15)
FRMBACKGROUND = "RoyalBlue1"
BTNBACKGROUNDSTATIC = "light grey"
BTNBACKGROUNDACTIVE = "ghost white"

class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = FRMBACKGROUND)
        self.lbl_title = tk.Label(self, text = "Trivia", font = TITLE_FONT, bg = FRMBACKGROUND)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.btn_start = tk.Button(self, text = "Start", font = WIDGET_FONT,
                                 command = "", bg = BTNBACKGROUNDSTATIC, 
                                 activebackground = BTNBACKGROUNDACTIVE)
        self.btn_start.grid(row = 1, column = 0)
        
        self.btn_scores = tk.Button(self, text = "High Scores", font = WIDGET_FONT,
                                  command = "", bg = BTNBACKGROUNDSTATIC, 
                                 activebackground = BTNBACKGROUNDACTIVE)
        self.btn_scores.grid(row = 2, column = 0)
        
class Question(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = FRMBACKGROUND)
        self.lbl_number = tk.Label(self, text = "Question #:", font = TITLE_FONT, bg = FRMBACKGROUND)
        self.lbl_number.grid(row = 0, column = 0, columnspan = 2, sticky = "news")
        
        self.lbl_question = tk.Label(self, text = "When was the \n war of 1812?", font = TITLE_FONT, bg = FRMBACKGROUND)
        self.lbl_question.grid(row = 1, column = 0, columnspan = 2, sticky = "news")
        
        rad_answer1 = tk.Radiobutton(self, text = "1776", bg = BTNBACKGROUNDSTATIC)
        rad_answer1.grid(row = 2, column = 0)
        
        rad_answer2 = tk.Radiobutton(self, text = "1790", bg = BTNBACKGROUNDSTATIC)
        rad_answer2.grid(row = 2, column = 1)        
        
        rad_answer3 = tk.Radiobutton(self, text = "1810", bg = BTNBACKGROUNDSTATIC)
        rad_answer3.grid(row = 3, column = 0)
        
        rad_answer4 = tk.Radiobutton(self, text = "1812", bg = BTNBACKGROUNDSTATIC)
        rad_answer4.grid(row = 3, column = 1)
        
        self.btn_ok = tk.Button(self, text = "Ok", font = WIDGET_FONT,
                                  command = "", bg = BTNBACKGROUNDSTATIC, 
                                 activebackground = BTNBACKGROUNDACTIVE)
        self.btn_ok.grid(row = 4, column = 0, columnspan = 2)        
        
   
    
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Trivia")
    #root.geometry("900x700")
    
    mainmenu = MainMenu()
    mainmenu.grid(row = 0, column = 0, sticky = "news")
    
    question = Question()
    question.grid(row = 0, column = 0, sticky = "news")
    
    #mainmenu.tkraise()
    question.tkraise()
    
    root.grid_columnconfigure(0, weight = 1)
    root.mainloop()     
    