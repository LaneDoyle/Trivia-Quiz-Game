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

answered_questions = []
button_pressed = ""

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
        frm_question_select.tkraise()
        
    def raise_highscores(self):
        frm_highscores.tkraise()
        
class Question(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = FRMBACKGROUND)
        self.tk_which_answer = tk.StringVar()
        self.correct_answer = ""
        
        self.selected_question = "Question Placeholder"
        self.answer1 = "Answer 1"
        self.answer2 = "Answer 2"
        self.answer3 = "Answer 3"
        self.answer4 = "Answer 4"
        
        self.lbl_number = tk.Label(self, text = "Question #" + str(question_count), font = TITLE_FONT, bg = FRMBACKGROUND)
        self.lbl_number.grid(row = 0, column = 0, columnspan = 2, sticky = "news")
        
        self.lbl_question = tk.Label(self, text = self.selected_question, font = TITLE_FONT, bg = FRMBACKGROUND)
        self.lbl_question.grid(row = 1, column = 0, columnspan = 2, sticky = "news")
        
        self.rad_answer1 = tk.Radiobutton(self, text = self.answer1, value = self.answer1, variable = self.tk_which_answer,
                                     bg = FRMBACKGROUND)
        self.rad_answer1.grid(row = 2, column = 0)
        
        self.rad_answer2 = tk.Radiobutton(self, text = self.answer2, value = self.answer2, variable = self.tk_which_answer,
                                     bg = FRMBACKGROUND)
        self.rad_answer2.grid(row = 2, column = 1)        
        
        self.rad_answer3 = tk.Radiobutton(self, text = self.answer3, value = self.answer3, variable = self.tk_which_answer,
                                     bg = FRMBACKGROUND)
        self.rad_answer3.grid(row = 3, column = 0)
        
        self.rad_answer4 = tk.Radiobutton(self, text = self.answer4, value = self.answer4, variable = self.tk_which_answer,
                                     bg = FRMBACKGROUND)
        self.rad_answer4.grid(row = 3, column = 1)
        
        self.btn_quit = tk.Button(self, text = "Quit", font = WIDGET_FONT,
                                command = self.quit, bg = BTNBACKGROUNDSTATIC, 
                                activebackground = BTNBACKGROUNDACTIVE)
        self.btn_quit.grid(row = 4, column = 0)
        
        self.btn_ok = tk.Button(self, text = "Ok", font = WIDGET_FONT,
                                command = self.answer, bg = BTNBACKGROUNDSTATIC, 
                                activebackground = BTNBACKGROUNDACTIVE)
        self.btn_ok.grid(row = 4, column = 1)
        
    def update(self):
        self.lbl_number.configure(text = "Question #" + str(question_count))
        self.lbl_question.configure(text = self.selected_question)
        self.rad_answer1.configure(text = self.answer1, value = self.answer1)
        self.rad_answer2.configure(text = self.answer2, value = self.answer2)
        self.rad_answer3.configure(text = self.answer3, value = self.answer3)
        self.rad_answer4.configure(text = self.answer4, value = self.answer4)
        
    def quit(self):
        frm_question_select.tkraise()
        
    def answer(self):
        global button_pressed
        if self.correct_answer == self.tk_which_answer.get():
            popup = tk.Tk()
            popup.title("")
            msg = "That's correct!"
            frm_correct = GenericMessage(popup, msg)
            frm_correct.grid(row = 0, column = 0)
        else:
            popup = tk.Tk()
            popup.title("")
            msg = "That's incorrect!"
            frm_incorrect = GenericMessage(popup, msg)
            frm_incorrect.grid(row = 0, column = 0)
        QuestionSelect.raise_question(self, option = button_pressed)
        
class QuestionSelect(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = FRMBACKGROUND)
        
        self.lbl_title = tk.Label(self, text = "Select a Mode", font = TITLE_FONT,
                                  bg = FRMBACKGROUND)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.btn_history = tk.Button(self, text = "History", font = WIDGET_FONT,
                                     command = self.history_questions, bg = BTNBACKGROUNDSTATIC, 
                                     activebackground = BTNBACKGROUNDACTIVE)
        self.btn_history.grid(row = 1, column = 0)
        
        self.btn_geography = tk.Button(self, text = "Geography", font = WIDGET_FONT,
                                       command = self.geography_questions, bg = BTNBACKGROUNDSTATIC, 
                                       activebackground = BTNBACKGROUNDACTIVE)
        self.btn_geography.grid(row = 2, column = 0)
        
        self.btn_music = tk.Button(self, text = "Music", font = WIDGET_FONT,
                                   command = self.music_questions, bg = BTNBACKGROUNDSTATIC, 
                                   activebackground = BTNBACKGROUNDACTIVE)
        self.btn_music.grid(row = 3, column = 0)
    
        self.btn_games = tk.Button(self, text = "Games", font = WIDGET_FONT,
                                   command = self.games_questions, bg = BTNBACKGROUNDSTATIC, 
                                   activebackground = BTNBACKGROUNDACTIVE)
        self.btn_games.grid(row = 4, column = 0)
        
        self.btn_random = tk.Button(self, text = "Random", font = WIDGET_FONT,
                                    command = self.random_questions, bg = BTNBACKGROUNDSTATIC, 
                                    activebackground = BTNBACKGROUNDACTIVE)
        self.btn_random.grid(row = 5, column = 0)
        
        self.btn_back = tk.Button(self, text = "Back", font = WIDGET_FONT,
                                  command = self.raise_main, bg = BTNBACKGROUNDSTATIC, 
                                  activebackground = BTNBACKGROUNDACTIVE)
        self.btn_back.grid(row = 6, column = 0)
        
    def raise_question(self, option):
        global question_count
        global answered_questions
        
        chosen_question = 0
        question_count += 1
        
        if option == "History":
            if answered_questions == []:
                chosen_question = rd.randint(1,2)
            else:
                if chosen_question == 0:
                    chosen_question = rd.randint(1,2)
                while questions[chosen_question][0] not in answered_questions:
                    chosen_question = rd.randint(1,2)
        elif option == "Geography":
            if answered_questions == []:
                chosen_question = rd.randint(3,4)
            else:
                while questions[chosen_question][0] not in answered_questions:
                    chosen_question = rd.randint(3,4)
        elif option == "Music":
            if answered_questions == []:
                chosen_question = rd.randint(5,6)
            else:
                while questions[chosen_question][0] not in answered_questions:
                    chosen_question = rd.randint(5,6)
        elif option == "Games":
            if answered_questions == []:
                chosen_question = rd.randint(7,8)
            else:
                while questions[chosen_question][0] not in answered_questions:
                    chosen_question = rd.randint(7,8)
        elif option == "Random":
            if answered_questions == []:
                chosen_question = rd.randint(1,8)
            else:
                while questions[chosen_question][0] not in answered_questions:
                    chosen_question = rd.randint(1,8)
        
        answered_questions.append(questions[chosen_question][0])
        
        answers = [questions[chosen_question][1],questions[chosen_question][2],
                   questions[chosen_question][3],questions[chosen_question][4]]
        frm_question.correct_answer = questions[chosen_question][1]
        temp_placed_answers = []
        
        while len(temp_placed_answers) != 4:
            temp_answer = rd.choice(answers)
            if temp_answer not in temp_placed_answers:
                temp_placed_answers.append(temp_answer)
                
        frm_question.selected_question = questions[chosen_question][0]
        frm_question.answer1 = temp_placed_answers[0]
        frm_question.answer2 = temp_placed_answers[1]
        frm_question.answer3 = temp_placed_answers[2]
        frm_question.answer4 = temp_placed_answers[3]
        frm_question.update()
        frm_question.tkraise()
        
        if question_count >= 3:
            global button_pressed
            popup = tk.Tk()
            popup.title("")
            msg = "That's all folks!!!"
            frm_incorrect = GenericMessage(popup, msg)
            frm_incorrect.grid(row = 0, column = 0)
            answered_questions = []
            frm_mainmenu.tkraise()
            button_pressed = ""
        
        print(answered_questions)
        
    def history_questions(self):
        global button_pressed
        button_pressed = "History"
        self.raise_question("History")
        
    def geography_questions(self):
        global button_pressed
        button_pressed = "Geography"
        self.raise_question("Geography")
        
    def music_questions(self):
        global button_pressed
        button_pressed = "Music"
        self.raise_question("Music")
        
    def games_questions(self):
        global button_pressed
        button_pressed = "Games"
        self.raise_question("Games")
    
    def random_questions(self):
        global button_pressed
        button_pressed = "Random"
        self.raise_question("Random")
        
    def raise_main(self):
        frm_mainmenu.tkraise()
        
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
        frm_mainmenu.tkraise()
    
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
        
class GenericMessage(tk.Frame):
    def __init__(self, parent, msg =  "generic"):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        
        self.lbl_continue = tk.Label(self, text = msg)
        self.lbl_continue.grid(row = 0, column = 0)
        
        self.btn_ok = tk.Button(self, text = "Ok", 
                                command = self.parent.destroy)
        self.btn_ok.grid(row = 1, column = 0)

        
if __name__ == "__main__":
    global question_count
    question_count = 0
    
    questions = {}
    datafile = open("questions_lib.pickle", "rb")
    questions = pk.load(datafile)
    datafile.close()
    
    root = tk.Tk()
    root.title("Trivia")
    #root.geometry("900x700")
    
    frm_mainmenu = MainMenu()
    frm_mainmenu.grid(row = 0, column = 0, sticky = "news")
    
    frm_question_select = QuestionSelect()
    frm_question_select.grid(row = 0, column = 0, sticky = "news")
    
    frm_question = Question()
    frm_question.grid(row = 0, column = 0, sticky = "news")
    
    frm_highscores = HighScores()
    frm_highscores.grid(row = 0, column = 0, sticky = "news")
    
    frm_mainmenu.tkraise()
    root.grid_columnconfigure(0, weight = 1)
    root.mainloop()     
    