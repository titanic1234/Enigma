#Datei wird nicht genutzt. Der Code steht in einer Funktion in main.py




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

def walzen_main(text, walze, schluesselung, stellung = None):
    walzen = walze.split(" ")
    pos = list(stellung)

    for i in range(len(walzen)):
        if walzen[i] == "1":
            text, pos[i] = Ix1.i_walze(text, pos[i])
        if walzen[i] == "2":
            text, pos[i] = Ix2.ii_walze(text, pos[i])
        if walzen[i] == "3":
            text, pos[i] = Ix3.iii_walze(text, pos[i])
        if walzen[i] == "4":
            text, pos[i] = Ix4.iv_walze(text, pos[i])
        if walzen[i] == "5":
            text, pos[i] = Ix5.v_walze(text, pos[i])
        print(text)

    #Für Tests



    text = UKW.ukw_walze(text)





    for i in range(len(walzen), 0):
        print(i)
        if walzen[i] == "1":
            text, pos[i] = Ix1.i_walze(text, pos[i])
        if walzen[i] == "2":
            text, pos[i] = Ix2.ii_walze(text, pos[i])
        if walzen[i] == "3":
            text, pos[i] = Ix3.iii_walze(text, pos[i])
        if walzen[i] == "4":
            text, pos[i] = Ix4.iv_walze(text, pos[i])
        if walzen[i] == "5":
            text, pos[i] = Ix5.v_walze(text, pos[i])


    return text

