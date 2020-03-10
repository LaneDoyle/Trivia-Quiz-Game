#!/usr/bin/python3
# trivia_game.py
# Lane D. and Dominic M.
# 9/3/2020

''' Program to ask the user trivia questions and log high scores'''

import pickle as pk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import random as rd

#Constants
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
                                 command = self.raise_question, bg = BTNBACKGROUNDSTATIC, 
                                 activebackground = BTNBACKGROUNDACTIVE)
        self.btn_start.grid(row = 1, column = 0)
        
        self.btn_scores = tk.Button(self, text = "High Scores", font = WIDGET_FONT,
                                  command = self.raise_highscores, bg = BTNBACKGROUNDSTATIC, 
                                 activebackground = BTNBACKGROUNDACTIVE)
        self.btn_scores.grid(row = 2, column = 0)
        
    def raise_question(self):
        question_select.tkraise()
        
    def raise_highscores(self):
        highscores.tkraise()
        
class Question(tk.Frame):
    def __init__(self, question = "Question Placeholder"):
        tk.Frame.__init__(self, bg = FRMBACKGROUND)
        self.tk_which_answer = tk.IntVar()
        
        self.answer1 = "Answer 1"
        self.answer2 = "Answer 2"
        self.answer3 = "Answer 3"
        self.answer4 = "Answer 4"
        
        self.lbl_number = tk.Label(self, text = "Question #:", font = TITLE_FONT, bg = FRMBACKGROUND)
        self.lbl_number.grid(row = 0, column = 0, columnspan = 2, sticky = "news")
        
        self.lbl_question = tk.Label(self, text = question, font = TITLE_FONT, bg = FRMBACKGROUND)
        self.lbl_question.grid(row = 1, column = 0, columnspan = 2, sticky = "news")
        
        rad_answer1 = tk.Radiobutton(self, text = answer1, value = 1, variable = self.tk_which_answer,
                                     bg = FRMBACKGROUND, fg = "white")
        rad_answer1.grid(row = 2, column = 0)
        
        rad_answer2 = tk.Radiobutton(self, text = answer2, value = 2, variable = self.tk_which_answer,
                                     bg = FRMBACKGROUND, fg = "white")
        rad_answer2.grid(row = 2, column = 1)        
        
        rad_answer3 = tk.Radiobutton(self, text = answer3, value = 3, variable = self.tk_which_answer,
                                     bg = FRMBACKGROUND, fg = "white")
        rad_answer3.grid(row = 3, column = 0)
        
        rad_answer4 = tk.Radiobutton(self, text = answer4, value = 4, variable = self.tk_which_answer,
                                     bg = FRMBACKGROUND, fg = "white")
        rad_answer4.grid(row = 3, column = 1)
        
        self.btn_ok = tk.Button(self, text = "Ok", font = WIDGET_FONT,
                                command = self.answer, bg = BTNBACKGROUNDSTATIC, 
                                activebackground = BTNBACKGROUNDACTIVE)
        self.btn_ok.grid(row = 4, column = 0, columnspan = 2)        
        
    def answer(self):
        print(self.tk_which_answer)
        
class QuestionSelect(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = FRMBACKGROUND)
        self.lbl_title = tk.Label(self, text = "Select a Mode", font = TITLE_FONT,
                                  bg = FRMBACKGROUND)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.btn_history = tk.Button(self, text = "History", font = WIDGET_FONT,
                                     command = self.raise_question, bg = BTNBACKGROUNDSTATIC, 
                                     activebackground = BTNBACKGROUNDACTIVE)
        self.btn_history.grid(row = 1, column = 0)
        
        self.btn_geography = tk.Button(self, text = "Geography", font = WIDGET_FONT,
                                       command = "", bg = BTNBACKGROUNDSTATIC, 
                                       activebackground = BTNBACKGROUNDACTIVE)
        self.btn_geography.grid(row = 2, column = 0)
        
        self.btn_music = tk.Button(self, text = "Music", font = WIDGET_FONT,
                                   command = "", bg = BTNBACKGROUNDSTATIC, 
                                   activebackground = BTNBACKGROUNDACTIVE)
        self.btn_music.grid(row = 3, column = 0)
    
        self.btn_games = tk.Button(self, text = "Games", font = WIDGET_FONT,
                                   command = "", bg = BTNBACKGROUNDSTATIC, 
                                   activebackground = BTNBACKGROUNDACTIVE)
        self.btn_games.grid(row = 4, column = 0)
        
        self.btn_random = tk.Button(self, text = "Random", font = WIDGET_FONT,
                                    command = "", bg = BTNBACKGROUNDSTATIC, 
                                    activebackground = BTNBACKGROUNDACTIVE)
        self.btn_random.grid(row = 5, column = 0)
        
        self.btn_back = tk.Button(self, text = "Back", font = WIDGET_FONT,
                                  command = self.raise_main, bg = BTNBACKGROUNDSTATIC, 
                                  activebackground = BTNBACKGROUNDACTIVE)
        self.btn_back.grid(row = 6, column = 0)
        
    def raise_question(self):
        self.answers = [questions[1][1], questions[1][2], questions[1][3], questions[1][4]]
        temp_placedanswers = []
        while len(temp_placedanswers) != 4:
            temp_answers = rd.choice(self.answers)
            if temp_answers not in temp_placedanswers:
                temp_placedanswers.append(temp_answers)
        Question.answer1 = temp_answers[0]        
        question.tkraise()
        
    def raise_main(self):
        mainmenu.tkraise()
        
class HighScores(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = FRMBACKGROUND)
        self.lbl_title = tk.Label(self, text = "High Scores", font = TITLE_FONT,
                                  bg = FRMBACKGROUND)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.btn_history = tk.Button(self, text = "History", font = WIDGET_FONT,
                                     command = self.raise_history, bg = BTNBACKGROUNDSTATIC, 
                                     activebackground = BTNBACKGROUNDACTIVE)
        self.btn_history.grid(row = 1, column = 0)
        
        self.btn_geography = tk.Button(self, text = "Geography", font = WIDGET_FONT,
                                       command = self.raise_geography, bg = BTNBACKGROUNDSTATIC, 
                                       activebackground = BTNBACKGROUNDACTIVE)
        self.btn_geography.grid(row = 2, column = 0)
        
        self.btn_music = tk.Button(self, text = "Music", font = WIDGET_FONT,
                                   command = self.raise_music, bg = BTNBACKGROUNDSTATIC, 
                                   activebackground = BTNBACKGROUNDACTIVE)
        self.btn_music.grid(row = 3, column = 0)
    
        self.btn_games = tk.Button(self, text = "Games", font = WIDGET_FONT,
                                   command = self.raise_games, bg = BTNBACKGROUNDSTATIC, 
                                   activebackground = BTNBACKGROUNDACTIVE)
        self.btn_games.grid(row = 4, column = 0)
        
        self.btn_random = tk.Button(self, text = "Random", font = WIDGET_FONT,
                                    command = "", bg = BTNBACKGROUNDSTATIC, 
                                    activebackground = BTNBACKGROUNDACTIVE)
        self.btn_random.grid(row = 5, column = 0)
        
        self.btn_back = tk.Button(self, text = "Back", font = WIDGET_FONT,
                                  command = self.raise_main, bg = BTNBACKGROUNDSTATIC, 
                                  activebackground = BTNBACKGROUNDACTIVE)
        self.btn_back.grid(row = 6, column = 0)         
        
    def raise_history(self):
        popup = tk.Tk()
        popup.title("High Scores")
        msg = "History"
        frm_error = PopUp(popup, msg)
        frm_error.grid(row = 0, column = 0)
        
    def raise_geography(self):
        popup = tk.Tk()
        popup.title("High Scores")
        msg = "Geography"
        frm_error = PopUp(popup, msg)
        frm_error.grid(row = 0, column = 0) 
    
    def raise_music(self):
        popup = tk.Tk()
        popup.title("High Scores")
        msg = "Music"
        frm_error = PopUp(popup, msg)
        frm_error.grid(row = 0, column = 0)
    
    def raise_games(self):
        popup = tk.Tk()
        popup.title("High Scores")
        msg = "Games"
        frm_error = PopUp(popup, msg)
        frm_error.grid(row = 0, column = 0)     
        
    def raise_main(self):
        mainmenu.tkraise()
    
class PopUp(tk.Frame):
    def __init__(self, parent, msg = "History",
                 first_place = "Christian", second_place = "Dominic", third_place = "Gentry",
                 fourth_place = "Kendal", fifth_place = "Chris"):
        tk.Frame.__init__(self, master = parent, bg = FRMBACKGROUND)
        self.parent = parent
        
        self.lbl_title = tk.Label(self, text = msg, font = TITLE_FONT, bg = FRMBACKGROUND)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 2)
        
        self.lbl_first = tk.Label(self, text = "1st", font = TITLE_FONT,
                                  bg = FRMBACKGROUND)
        self.lbl_first.grid(row = 1, column = 0)
        
        self.ent_first = tk.Entry(self, font = WIDGET_FONT)
        self.ent_first.grid(row = 1, column = 1)
        
        self.lbl_second = tk.Label(self, text = "2nd", font = TITLE_FONT,
                                   bg = FRMBACKGROUND)
        self.lbl_second.grid(row = 2, column = 0)
        
        self.ent_second = tk.Entry(self, font = WIDGET_FONT)
        self.ent_second.grid(row = 2, column = 1)
        
        self.lbl_third = tk.Label(self, text = "3rd", font = TITLE_FONT,
                                  bg = FRMBACKGROUND)
        self.lbl_third.grid(row = 3, column = 0)
        
        self.ent_third = tk.Entry(self, font = WIDGET_FONT)
        self.ent_third.grid(row = 3, column = 1)
        
        self.lbl_fourth = tk.Label(self, text = "4th", font = TITLE_FONT,
                                   bg = FRMBACKGROUND)
        self.lbl_fourth.grid(row = 4, column = 0)
        
        self.ent_fourth = tk.Entry(self, font = WIDGET_FONT)
        self.ent_fourth.grid(row = 4, column = 1)
        
        self.lbl_fifth = tk.Label(self, text = "5th", font = TITLE_FONT,
                                  bg = FRMBACKGROUND)
        self.lbl_fifth.grid(row = 5, column = 0)
        
        self.ent_fifth = tk.Entry(self, font = WIDGET_FONT)
        self.ent_fifth.grid(row = 5, column = 1)
        
        self.btn_back = tk.Button(self, text = "Back", font = WIDGET_FONT,
                                  command = self.raise_main, bg = BTNBACKGROUNDSTATIC, 
                                 activebackground = BTNBACKGROUNDACTIVE)
        self.btn_back.grid(row = 6, column = 0, columnspan = 2)
        
    def raise_main(self):
        self.parent.destroy()
        
if __name__ == "__main__":
    questions = {}
    datafile = open("questions_lib.pickle", "rb")
    questions = pk.load(datafile)
    datafile.close()    
    
    root = tk.Tk()
    root.title("Trivia")
    #root.geometry("900x700")
    
    mainmenu = MainMenu()
    mainmenu.grid(row = 0, column = 0, sticky = "news")
    
    question_select = QuestionSelect()
    question_select.grid(row = 0, column = 0, sticky = "news")
    
    question = Question()
    question.grid(row = 0, column = 0, sticky = "news")
    
    highscores = HighScores()
    highscores.grid(row = 0, column = 0, sticky = "news")
    
    mainmenu.tkraise()
    root.grid_columnconfigure(0, weight = 1)
    root.mainloop()     
    