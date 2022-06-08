import time
import os
import sys
import asyncio
import walzen.I as Ix1
import walzen.II as Ix2
import walzen.III as Ix3
import walzen.IV as Ix4
import walzen.V as Ix5
import walzen.ukw as UKW

def walzen_main(text, walze, stellung = None):
    walzen = walze.split(" ")
    pos = list(stellung)

    for i in range(len(walzen)):
        if walzen[i] == "1":
            pass #1
        if walzen[i] == "2":
            pass #2
        if walzen[i] == "3":
            pass #3
        if walzen[i] == "4":
            pass #4
        if walzen[i] == "5":
            pass #5


    #Für Tests


    text, pos_5 = Ix5.v_walze(text, pos[0])
    text, pos_3 = Ix3.iii_walze(text, pos[1])
    text, pos_1 = Ix1.i_walze(text, pos[2])
    text = UKW.ukw_walze(text)
    text, _ = Ix1.i_walze(text, pos_1)
    text, _ = Ix3.iii_walze(text, pos_3)
    text, _ = Ix5.v_walze(text, pos_5)


    return text

