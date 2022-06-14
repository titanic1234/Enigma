import time
import asyncio
import os
import sys


#Text geht durch Walze

ab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

II = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']

def ii_walze(text, pos, schluesselung):
    if schluesselung == "0": c = 1
    else: c = -1
    text = list(text)
    text_i_liste = []

    a = 0 + II.index(pos)
    b = 0

    for i in text:

        if i == " ":
            text_i_liste.append(" ")
            continue
        ab_in = ab.index(i)

        if int((ab_in + a) / 26) >= 1:
            b = int(int(int(ab_in + a) / 26) * 26)
        x = II[(ab_in+a-b) % 26]

        text_i_liste.append(x)
        a += c


    text_i = "".join(text_i_liste)

    a = a % 26

    return text_i, II[a]
