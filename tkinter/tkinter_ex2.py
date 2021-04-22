# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:07:35 2021

@author: Divya
"""


import tkinter

# Let's create the Tkinter window.
window = tkinter.Tk()
window.title("Tkinter Tutorials with KK")

# You will first create a division with the help of Frame class and align them on TOP and BOTTOM with pack() method.
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side = "bottom")

button_widget = tkinter.Button(window,text="Welcome to Tkinter's Tutorial with kk")
button_widget.pack()


window.mainloop()