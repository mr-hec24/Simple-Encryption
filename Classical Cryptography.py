#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 05:42:13 2023

@author: hectorrodriguez
"""

from tkinter import *
import re

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key = ''

root = Tk()
root.title('Classical Cryptography')
root.config(bg='skyblue')
root.geometry("400x400")

# Chnage the label text
def show():
    label.config( text = clicked.get() )
    button.config( text = clicked.get() )
    
    
def computeMessage():
    # ENCODE MESSAGE
    if clicked.get() == 'Encode':
        # Get message from the inputBox
        message = inputBox.get(1.0, 'end-1c')
        
        # Use regex to get rid of punctuation
        message = re.sub(r'[^\w\s]', '', message)
        
        # Get rid of whitespace and lower all letters
        message = message.replace(" ", "").lower()
        encodedMsg = ''
        
        # Generates the encoded message
        for char in message:
            encodedMsg += str(alphabet.index(char)) + " "
            
        # Displays the encoded message in the label
        label.config(text = encodedMsg)
        
    # DECODE MESSAGE
    if clicked.get() == 'Decode':
        # Get message from the inputBox
        message = inputBox.get(1.0, 'end-1c')
        
        # Split the message into the individual numbers
        message = message.split(" ")
        decodedMsg = ''
        
        # Generated the decoded message
        for char in message:
            decodedMsg += alphabet[int(char)]
            
        # Displays the decoded message in the label
        label.config(text = decodedMsg)

options = ['Encode', 'Decode']
clicked = StringVar()
drop = OptionMenu(root, clicked, *options)
drop.pack()

inputBox = Text(root, height = 10, width = 40)
inputBox.pack()

button = Button(root, text="Compute Message", command=computeMessage).pack()

label = Label(root, text=" ")
label.pack()

root.mainloop()

        
    


