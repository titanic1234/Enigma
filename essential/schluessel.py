import os
import sys
import time
import asyncio
import walze

def erkennung(schluessel, text, walzen):
    if schluessel == None:
        return None
    schluessel = str(schluessel).split("-")
    zeit = list(schluessel[0])
    print(f"Die Nachricht wurde laut dem Spruchschlüssel um {zeit[0] + zeit[1]}:{zeit[2] + zeit[3]} geschickt.")
    wahr = input("Wenn das von der Uhrzeit stimmen kann tippe jetzt bitte 1 und Enter!\n")
    if wahr != "1":
        return False, None, None, None



    text = text.replace(" ", "")
    f = True
    if schluessel[1] == "pass":
        f = False
    elif int(schluessel[1]) != len(list(text)) and f:
        return False, None, None, None

    print(schluessel)

    #text_rueckgabe = walze.walzen_main(schluessel[2].split(" ")[1], walzen, schluessel[2].split(" ")[0])
    return True, schluessel[2].split(" ")[1], walzen, schluessel[2].split(" ")[0]
    #return text_rueckgabe
