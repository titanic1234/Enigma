import os
import sys
import time
import asyncio

def steckverbindungen(stecker, text, stecker_json=None):
    stecker = stecker.upper()
    stecker = stecker.split(" ")
    stecker_list = []


    if stecker_json == None:
        stecker_json = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
            "H": None,
            "I": None,
            "J": None,
            "K": None,
            "L": None,
            "M": None,
            "N": None,
            "O": None,
            "P": None,
            "Q": None,
            "R": None,
            "S": None,
            "T": None,
            "U": None,
            "V": None,
            "W": None,
            "X": None,
            "Y": None,
            "Z": None,
            " ": " "
        }


    for i in stecker:
        stecker_list.append(list(i))
        a = list(i)
        stecker_json[a[0]] = a[1]
        stecker_json[a[1]] = a[0]



    text_liste = list(text)
    text_steckbrett = ""
    for i in text_liste:

        y = stecker_json[i]
        if y == None:
            y = i
        text_steckbrett = str(text_steckbrett) + str(y)


    return text_steckbrett, stecker_json