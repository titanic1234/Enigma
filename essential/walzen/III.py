import time
import asyncio
import os
import sys


ab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

III = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']#['Q', 'U', 'D', 'L', 'Y', 'R', 'F', 'E', 'K', 'O', 'N', 'V', 'Z', 'A', 'X', 'W', 'H', 'M', 'G', 'P', 'J', 'B', 'S', 'I', 'C', 'T']

def iii_walze(text, pos):
    text = list(text)
    text_iii_liste = []
    a = 0 + III.index(pos)
    b = 0

    for i in text:
        #print(a)
        #print(b)
        if i == " ":
            text_iii_liste.append(" ")
            continue
        ab_in = ab.index(i)
        #print(ab_in)
        if int((ab_in + a) / 26) >= 1:
            b = int(int(int(ab_in + a) / 26) * 26)
        x = III[ab_in+a-b]
        #print(x)
        text_iii_liste.append(x)
        a += 1


    text_iii = "".join(text_iii_liste)

    a = a % 26

    return text_iii, III[a]