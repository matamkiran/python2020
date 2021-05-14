# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 13:04:50 2021

@author: Divya
"""

sentence="the cat in the hat had two sidekicks, things one and thing two"

#split sentence to words with space as delimiter 
words=sentence.lower().replace(',',"").split()

print(words)
#converting list of words to set of words 
print(set(words))

# set of words whose length is <=3
unique_words={word for word in words if len(word)<=3}
print(unique_words)

# set of words whose length is >3
unique_words={word for word in words if len(word)>3}
print(unique_words)




"""
# capitalize the word letter if its start with H
unique_words={word.capitalize() if word[0]=='h' else word for word in words if len(word)<=3}
print(unique_words)


#Nested set comprehension
vowels=['a','e','i','o','u']

consonants ={frozenset({letter for letter in word if letter not in vowels}) for word in words }
print(consonants)
"""
