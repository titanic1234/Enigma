import time
import asyncio
import os
import sys


ab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

I = ['K', 'P', 'T', 'Y', 'U', 'E', 'L', 'O', 'C', 'V', 'G', 'R', 'F', 'Q', 'D', 'A', 'N', 'J', 'M', 'B', 'S', 'W', 'H', 'Z', 'X', 'I']


def i_walze(text, pos):
    text = list(text)
    text_i_liste = []
    print(pos)
    a = 0 + I.index(pos)
    b = 0

    for i in text:
        #print(a)
        #print(b)
        if i == " ":
            text_i_liste.append(" ")
            continue
        ab_in = ab.index(i)
        #print(ab_in)
        if int((ab_in + a) / 26) >= 1:
            b = int(int(int(ab_in + a) / 26) * 26)
        x = I[ab_in+a-b]
        #print(x)
        text_i_liste.append(x)
        a += 1


    text_i = "".join(text_i_liste)

    a = a % 26

    return text_i, I[a]