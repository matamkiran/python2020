# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:14:03 2021

@author: Divya
"""

import tkinter
# Let's create the Tkinter window
window = tkinter.Tk()
window.title("GUI")


# You will create two text labels namely 'username' and 'password' and and two input labels for them

tkinter.Label(window, text = "Username").grid(row = 0) #'username' is placed on position 00 (row - 0 and column - 0)

# 'Entry' class is used to display the input-field for 'username' text label
tkinter.Entry(window).grid(row = 0, column = 1) # first input-field is placed on position 01 (row - 0 and column - 1)

tkinter.Label(window, text = "Password").grid(row = 1) #'password' is placed on position 10 (row - 1 and column - 0)

tkinter.Entry(window).grid(row = 1, column = 1) #second input-field is placed on position 11 (row - 1 and column - 1)

# 'Checkbutton' class is for creating a checkbutton which will take a 'columnspan' of width two (covers two columns)
tkinter.Checkbutton(window, text = "Keep Me Logged In").grid(columnspan = 2)       

#tkinter.Button(window, text = "Login").grid()(row = 3)
"""
# A basic 'if/else' block where if user clicks on 'Yes' then it returns 1 else it returns 0. For each response you will display a message with the help of 'Label' method.
if(response == 'yes'):
    tkinter.Label(window, text = "Yes, offcourse I love Deep Learning!").pack()
else:
    tkinter.Label(window, text = "No, I don't love Deep Learning!").pack()          
"""
window.mainloop()