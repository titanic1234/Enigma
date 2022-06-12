import time
import os
import asyncio


def aufteilen(text, schluesseln):

    if schluesseln == "0":
        pass

    #print(text)
    #text = "Diese Nachricht ist streng geheim & darf unter keinen Umständen in die Hände der Feinde fallen! 1 2 3 ?ß ü,ö"
    #Der Staat Liechtenstein liefert in rhythmischen Abständen nummerierte Stanniolsäckchen an Libyen und Hawaii.

    text = text.casefold()
    text = text.upper()


    #print(text)


    liste = list(text)



    #Wichtige Variablen werden definiert

    i = 0
    x = len(liste) - 1
    zeichen = [',', '.', '-', ';', ':', '_', '+', '#', '*', "'", '~', '§', '$', '%', '&', '/', '(', ')', '=', '`', '´',
               '\\', '}', ']', '[', '{', '³', '²', '<', '>', '|', '"', "?", "!", ","]
    zahlen = {
        "1": "EINS",
        "2": "ZWEI",
        "3": "DREI",
        "4": "VIER",
        "5": "FUENF",
        "6": "SEQS",
        "7": "SIEBEN",
        "8": "ACHT",
        "9": "NEUN",
        "0": "NULL"
    }
    zahlenliste = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    #Zahlen werden ersetzt

    """
    while i <= x:
        if liste[i] in zahlenliste:
            zahl = zahlen[liste[i]]
            zahl = list(zahl)
            a = i + 1
            liste[i] = zahl[0]
            for b in range(1, len(zahl)):
                liste.insert(a + b, zahl[b])
        
        i += 1
    
    #"""



    #Die Nachricht wird gefiltert. Zeichen etc. werden entfernt. (So wie bei der echten Enigma)

    while i <= x:
        #print(i)
        #print(x)
        #print(liste)



        if liste[i] == " ":
            if schluesseln == "0":
                liste[i] = "X"
            else:
                del liste[i]
                x -= 1
                continue
        if liste[i] in zeichen:
            liste.remove(liste[i])
            x -= 1
            continue
        try:
            if schluesseln == "0":

                if liste[i] == "C" and liste[i+1] == "H":
                    liste[i] = "Q"
                    #liste.remove(liste[i+1])
                    #x -= 1
                    continue

                if liste[i] == "C" and liste[i+1] == "K":
                    liste[i] = "Q"
                    #liste.remove(liste[i+1])
                    #x -= 1
                    continue
            elif schluesseln == "1":
                b = 1  # b ist nur 2, falls die nächste Stelle ein Leerzeichen ist, um ein QH oder QK trotzdem zu finden
                if liste[i + 1] == " ":
                    b = 2
                if liste[i] == "Q" and liste[i + b] == "H":
                    liste[i] = "C"
                    # liste.remove(liste[i+1])
                    # x -= 1
                    continue

                if liste[i] == "Q" and liste[i + b] == "K":
                    liste[i] = "C"
                    # liste.remove(liste[i+1])
                    # x -= 1
                    continue
        except Exception:
            pass

        if liste[i] == "Ä":
            liste[i] = "A"
            try:
                liste.insert(i+1, "E")
            except Exception:
                liste.append("E")
            x += 1
            continue
        if liste[i] == "Ö":
            liste[i] = "O"
            try:
                liste.insert(i + 1, "E")
            except Exception:
                liste.append("E")
            x += 1
            continue
        if liste[i] == "Ü":
            liste[i] = "U"
            try:
                liste.insert(i + 1, "E")
            except Exception:
                liste.append("E")
            x += 1
            continue

        if liste[i] in zahlenliste:
            print(liste)
            zahl = zahlen[liste[i]]
            zahl = list(zahl)
            #a = i+1
            liste[i] = zahl[0]
            print(liste)

            for b in range(1, len(zahl)):
                print(liste)
                liste.insert(i+b, zahl[b])
                x += 1
            print(liste)
            #continue


        i += 1


        #"""







    #Weitere Variablen

    liste2 = []
    x = 0
    zwischenliste = []


    str_fertig = ""

    #Die Nachricht wird von Liste zu einem str und in Fünfergruppen eingeteilt

    if schluesseln == "0":

        for i in range(0, len(liste)):
            if len(zwischenliste) <= 4:

                zwischenliste.append(liste[i])

            else:

                zwischenliste.append(" ")
                str_fertig = str_fertig + "".join(zwischenliste)

                zwischenliste = []
                zwischenliste.append(liste[i])


        if zwischenliste != []:
            str_fertig = str_fertig + "".join(zwischenliste)

    else:

        str_fertig = "".join(liste)
        str_fertig.replace("X", " ")


    return str_fertig