import time
import asyncio
import os
import sys


ab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

UKW = ['E', 'J', 'M', 'Z', 'A', 'L', 'Y', 'X', 'V', 'B', 'W', 'F', 'C', 'R', 'Q', 'U', 'O', 'N', 'T', 'S', 'P', 'I', 'K', 'H', 'G', 'D']#['G', 'E', 'K', 'P', 'B', 'T', 'A', 'U', 'M', 'O', 'C', 'N', 'I', 'L', 'J', 'D', 'X', 'Z', 'Y', 'F', 'H', 'W', 'V', 'Q', 'S', 'R']


def ukw_walze(text):
    text = list(text)
    text_ukw_liste = []


    for i in text:
        #print(a)
        #print(b)
        if i == " ":
            text_ukw_liste.append(" ")
            continue
        ab_in = ab.index(i)
        #print(ab_in)
        x = UKW[ab_in]
        y = UKW.index(x)
        z = ab[y]

        #print(x)
        text_ukw_liste.append(z)



    text_ukw = "".join(text_ukw_liste)

    return text_ukw