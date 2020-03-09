#!/usr/bin/python3
#Lane Doyle
#1/28/20

import pickle 

'''Program to reset the dictionary'''

questions = {1: ["When was the war of 1812?", "1812", "1776", "1790", "1810"],
             2: ["What is the longest river in South America?", "The Amazon", "The Nile River", 
                 "The Atlantic Ocean", "El Caribe"],
             3: ["Who is the lead singer of Pearl Jam?", "Eddie Vedder", "Buddie Hollie", "Van Houten", 
                 "James P. Sullivan"],
             4: ["Im cool", "Yes",  "Yes",  "Yes",  "Yes"]}

data_file = open("questions_lib.pickle", "wb")
pickle.dump(questions, data_file)
data_file.close()