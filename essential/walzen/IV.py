import time
import asyncio
import os
import sys


ab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

IV = ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B']

def iv_walze(text, pos):
    text = list(text)
    text_i_liste = []

    a = 0 + IV.index(pos)
    b = 0

    for i in text:

        if i == " ":
            text_i_liste.append(" ")
            continue
        ab_in = ab.index(i)

        if int((ab_in + a) / 26) >= 1:
            b = int(int(int(ab_in + a) / 26) * 26)
        x = IV[ab_in + a - b]

        text_i_liste.append(x)
        a += 1


    text_i = "".join(text_i_liste)

    a = a % 26

    return text_i, IV[a]