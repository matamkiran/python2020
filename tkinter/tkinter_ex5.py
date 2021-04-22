# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:17:04 2021

@author: Divya
"""

import tkinter
# Let's create the Tkinter window
window = tkinter.Tk()
window.title("GUI")

# creating a function called myTkinter_binding_command()
def myTkinter_binding_command():
    tkinter.Label(window, text = "GUI with Tkinter!").pack()

tkinter.Button(window, text = "Click Me!To Call Ur function", command = myTkinter_binding_command).pack()
window.mainloop()