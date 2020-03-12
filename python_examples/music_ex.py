# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 00:13:41 2020

@author: 666292
"""

from music21 import converter

# Define data directory
data_dir = '../audio/'

# Parse MIDI file and convert notes to chords
score = converter.parse(data_dir+'giuliani.mid').chordify()

# Display as sheet music
print(score.show())