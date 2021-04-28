# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 08:51:27 2021

@author: Divya
"""

movie="it's astonishing how frightening the actor actor norton looks with a shaved head and a swastika on his chest."

print(movie.find("actor",37,42))

if(movie.find("actor",37,42)==-1):
    print("word not found")

print(movie.count("actor"))

print(movie.replace("actor actor", "actor"))
