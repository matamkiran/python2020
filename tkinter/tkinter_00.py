# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:05:46 2021

@author: Divya
"""

import tkinter

# Let's create the Tkinter window.
window = tkinter.Tk()
window.title("Tkinter Tutorials with KK")

# You will first create a division with the help of Frame class and align them on TOP and BOTTOM with pack() method.
top_frame = tkinter.Frame(window).pack()

bottom_frame = tkinter.Frame(window).pack(side = "bottom")

label = tkinter.Label(window, text = "Welcome to Python GUI's Tutorial on Tkinter!").pack()
label = tkinter.Label(window, text = "class on april19").pack()


window.mainloop()