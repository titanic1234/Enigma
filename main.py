import os
import sys
import essential.steckbrett
import essential.aufteilung
import essential.walze
import essential.schluessel as s

import essential.walzen.I as Ix1
import essential.walzen.II as Ix2
import essential.walzen.III as Ix3
import essential.walzen.IV as Ix4
import essential.walzen.V as Ix5
import essential.walzen.ukw as UKW


import time
import asyncio
import tkinter as tk
import datetime

#SZ GT DV KU FO MY EW JN IX LQ

def main():
    schlusseln, spruchschluessel, text = infos()

    stecker, walzen2 = date()

    stellung = ss(text, spruchschluessel, walzen2)

    text_aufgeteilt = aufteilen(text, schlusseln)
    print(text_aufgeteilt)

    steckerrueckgabe, stecker_json = stecken(stecker, text_aufgeteilt)
    print(steckerrueckgabe)


    text_walzen = walzen(steckerrueckgabe, walzen2, stellung)
    print(text_walzen)

    steckerrueckgabe, stecker_json = stecken(stecker, text_aufgeteilt, stecker_json)
    #print(steckerrueckgabe)

    print("-----------------------------------------\n")
    print("Fertig verschlüsselt:")
    print(steckerrueckgabe)








def infos():
    print("Willkommen bei dem Enigmaprogramm zur Ver- und Entschlüsselung von Nachrichten!")
    schluesseln = str(input("Willst du deine Nachricht verschlüsseln? Dann tippe jetzt 0 und Enter. Wenn du sie entschlüsseln möchtest, tippe 1 und Enter! "))
    #stecker = input("Bitte gib hier die Steckverbindungen ein. Bitte jeweils in Zweiergruppen wie z. B. AB CD. Bitte jeden Buchstaben nur einmal! ")
    spruchschluessel = input("Bitte gib hier den Spruchschlüssel ein. Z. B. 2200-204-QWE EWG ")
    #walzen2 = input("Bitte gib jetzt noch an, welche Walzen genutzt werden sollen und achte bitte auf die Reihenfolge. Z. B. 1 5 3: ")
    text = input("Bitte gib jetzt den gesammten Text ein: ")

    return schluesseln, spruchschluessel, text


#ss für Spruchschlüssel
def ss(text, schluessel, walzen):
    ans = s.erkennung(schluessel, text, walzen)
    if ans == False:
        print("Die Nachricht wurde als Falsch erkannt!")
        sys.exit(0)
    return ans


def aufteilen(text, schluesseln):

    aufgeteilt = essential.aufteilung.aufteilen(text, schluesseln)

    return aufgeteilt



def stecken(stecker, text, stecker_json_=None): #spruchschluessel,

    if stecker_json_ == None:
        steckerrueckgabe, stecker_json = essential.steckbrett.steckverbindungen(stecker, text)

    else:
        steckerrueckgabe, stecker_json = essential.steckbrett.steckverbindungen(stecker, text, stecker_json_)


    return steckerrueckgabe, stecker_json


def walzen(text, walzen, stellung):

    text_rueckgabe = walzen_main(text, walzen, stellung)#essential.walze.walzen_main(text, walzen, stellung)

    return text_rueckgabe


def date():
    tag = datetime.datetime.now().strftime("%d")
    liste = [["DP BM NZ CK OV HQ AP UY SW JO", "2 1 3"], ["BN HU EG PY KQ CP OS JW AI VZ", "4 5 1"],
             ["KR MP CN BF EH DZ IW AV GJ LO", "5 1 2"], ["AC BL OZ EK QW OP SU DH JM TX", "2 4 1"],
             ["MV CL GK OQ BI FU HS PX NW EY", "5 2 4"], ["DQ GU BW NP HK AZ CI PO JX VY", "3 1 5"],
             ["UX IZ HN BK OQ CP FT JY MW AR", "1 4 2"], ["FI NQ SY CU BZ AH EL TX DO KP", "4 2 5"],
             ["QY BS LN KT AP IU DW HO RV JZ", "5 1 3"], ["LR IK MS QU HW PT DO VX PZ EN", "3 5 4"],
             ["KN UY HR PW FM BO EZ QT DX JV", "2 4 3"], ["MU BP CY RZ KX AN JT DG IL PW", "5 2 4"],
             ["LY AG KM BR IQ JU HV SW ET CX", "1 3 2"], ["GM JR KS IY HZ PL AX BT CQ NV", "4 1 5"],
             ["DS HY MR GW LX AJ BQ CO IP NT", "2 4 1"], ["HM JO DI NR BY XZ OS PU FQ CT", "5 2 3"],
             ["IR KZ LS EM OV GY QX AP JP BU", "1 4 2"], ["EJ OY IV AQ KW FX WT PS LU BD", "4 2 5"],
             ["OX PR FH WY DL CM AE TZ JS GI", "5 3 1"], ["DP HO QZ AU RY SV JL OX BE TW", "3 4 5"],
             ["RU HL PY OS GZ DM AW CE TV NX", "1 5 2"], ["PJ ES IM RX LV AY OU BG WZ CN", "2 4 5"],
             ["QV FR AK EO DH CJ MZ SX GN LT", "4 2 1"], ["TY AS OW KV JM DR HX GL CZ NU", "5 1 4"],
             ["OR FV AD IT PK HJ LZ NS EQ CW", "4 3 1"], ["VZ AL RT KO CG EI BJ DU PS HP", "1 4 5"],
             ["DY IN BV GR AM LO FP HT EX UW", "3 1 4"], ["CR FV AI DK OT MQ EU BX LP GJ", "2 3 5"],
             ["DJ AT CV IO ER QS LW PZ FN BH", "3 2 1"], ["IS EV MX RW DT UZ JQ AO CH NY", "4 3 2"],
             ["SZ GT DV KU FO MY EW JN IX LQ", "1 5 3"]]
    tag = int(tag) - 1
    steck = liste[tag][0]
    walz = liste[tag][1]
    print(steck)
    print(walz)
    return steck, walz

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
    pos = list(stellung)

    text, pos_5 = Ix5.v_walze(text, pos[0])
    text, pos_3 = Ix3.iii_walze(text, pos[1])
    text, pos_1 = Ix1.i_walze(text, pos[2])
    text = UKW.ukw_walze(text)
    text, _ = Ix1.i_walze(text, pos_1)
    text, _ = Ix3.iii_walze(text, pos_3)
    text, _ = Ix5.v_walze(text, pos_5)


    return text

if __name__ == "__main__":
    main()