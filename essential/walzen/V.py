import time
import asyncio
import os
import sys


ab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

V = ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K']#['U', 'A', 'X', 'G', 'I', 'S', 'N', 'J', 'B', 'V', 'E', 'R', 'D', 'Y', 'L', 'F', 'Z', 'W', 'T', 'P', 'C', 'K', 'O', 'H', 'M', 'Q']


def v_walze(text, pos):
    text = list(text)
    text_v_liste = []
    a = 0 + V.index(pos)
    b = 0

    for i in text:

        if i == " ":
            text_v_liste.append(" ")
            continue
        ab_in = ab.index(i)

        if int((ab_in + a) / 26) >= 1:
            b = int(int(int(ab_in + a) / 26) * 26)
        x = V[ab_in+a-b]

        text_v_liste.append(x)
        a += 1


    text_v = "".join(text_v_liste)

    a = a % 26

    return text_v, V[a]

