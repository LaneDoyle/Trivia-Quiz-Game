#!/usr/bin/python3
#Lane Doyle
#1/28/20

import pickle 

'''Program to reset the dictionary'''

questions = {1: ["When was the war of 1812?",
                 "1812", "1776", "1790", "1810"],
             2: ["How many theses did Martin Luther" + "\n" + "nail to the church door?",
                 "95", "80", "20", "13"],
             3: ["What is the longest river in South America?",
                 "The Amazon", "The Nile River", "The Atlantic Ocean", "El Caribe"],
             4: ["Where did the Renaissance start?",
                 "Italy", "Germany", "France", "Poland"],
             5: ["Who is the lead singer of Pearl Jam?",
                 "Eddie Vedder", "Buddie Hollie", "Van Houten", "James P. Sullivan"],
             6: ["When was Daft Punks" + "\n" + "'Discovery'Album Released?",
                 "2001", "1997", "2002", "2010"],
             7: ["What is the name of the woman Mario is trying to save in the original Donkey Kong?", 
                 "Pauline", "Princess Peach", "Princess Daisy", "Rosalina"],
             8: ["What is the Best-Selling Video Game" + "\n" + "of all time?",
                 "Tetris", "Minecraft", "Mario Kart Wii", "Wii Sports"]}

data_file = open("questions_lib.pickle", "wb")
pickle.dump(questions, data_file)
data_file.close()