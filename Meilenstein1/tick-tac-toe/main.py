import os
import random

def erster_spieler():
    if random.randint(0,1)==0:
        return "spieler1"
    else:
        return "spieler2"
    
def platz_chek(spielfeld, position):
    return spielfeld[position] ==" "

def spilefeld_voll(spielfeld):
    for i in range(1,10):
        if platz_chek(spielfeld,i):
            return False
    return True

def spieler_wahl(spielfeld):
    position=0
    while position not in range(1,10) or not platz_chek(spielfeld, int(position)):
        position= int(input("wähle deine nächste position: (1-9) \n> "))
    return position

def neuses_spiel():
    return input("Nochmal spielen? (J/N) \n> ").lower().startswith("j")

def spielfeld_anzeigen(spielfeld):
    os.system('cls' if os.name=="nt" else "clear")

    print(spielfeld[7] + " | " + spielfeld[8] + " | " + spielfeld[9])
    print("---------")
    print(spielfeld[4] + " | " + spielfeld[5] + " | " + spielfeld[6])
    print("---------")
    print(spielfeld[1] + " | " + spielfeld[2] + " | " + spielfeld[3])
    
    



#test_spielfeld=["#","X","O","X","O","X","O","X","O","X"]
test_spielfeld=["#","1","2","3","4","5","6","7","8","9"]
#spielfeld_anzeigen(test_spielfeld)


def spieler_eingabe():
    markierung=""
    while markierung !="X" and markierung !="O":
        markierung=input("Spieler1: X oder O ?\n> ").upper()
    if markierung == "X":
        return ("X","O")
    else:
        return ("O","X")
    
#spieler1, spieler2 = spieler_eingabe()

#print(f"Spieler1: {spieler1}  |  Spieler2: {spieler2}")


def markierung_setzen(spielfeld, markierung, position):
    spielfeld[position]=markierung

#markierung_setzen(test_spielfeld, "§", 8)
spielfeld_anzeigen(test_spielfeld)

def sieg_check(spielfeld, markierung) :
    #Zeilen
    #Spalten
    #Diagonale

    return ((spielfeld[7]== spielfeld[8]== spielfeld[9]== markierung) or
            (spielfeld[4]== spielfeld[5]== spielfeld[6]== markierung) or
            (spielfeld[1]== spielfeld[2]== spielfeld[3]== markierung) or
            #vert
            (spielfeld[7]== spielfeld[4]== spielfeld[1]== markierung) or
            (spielfeld[8]== spielfeld[5]== spielfeld[2]== markierung) or
            (spielfeld[9]== spielfeld[6]== spielfeld[3]== markierung) or
            #dia
            (spielfeld[7]== spielfeld[5]== spielfeld[3]== markierung) or
            (spielfeld[9]== spielfeld[5]== spielfeld[1]== markierung))
#print(sieg_check(test_spielfeld,"X"))



print("willkommen Beim Tic-tac-toe")

while True:
    #setup
    das_feld=[" "]*10
    spieler1_mark, spieler2_mark =spieler_eingabe()
    zug= erster_spieler()
    print(zug + "darf beginnen")

    spielen= input("bereit? j/n \n> ")
    if spielen.lower()[0]=="j":
        spiel_laeuft=True
    else:
        spiel_laeuft=False

    #spiel#
    while spiel_laeuft:
        if zug=="spieler1":
            #spieler1
            spielfeld_anzeigen(das_feld)
            position=spieler_wahl(das_feld)
            markierung_setzen(das_feld, spieler1_mark, position)

            if sieg_check(das_feld, spieler1_mark):
                spielfeld_anzeigen(das_feld)
                print("spieler1 hat gewnnen!")
                spiel_laeuft=False
            else:
                if spilefeld_voll(das_feld):
                    spielfeld_anzeigen(das_feld)
                    print("unentschieden")
                    break
                else:
                    zug= "spieler2"


        
        else:
        #spieler2
            spielfeld_anzeigen(das_feld)
            position=spieler_wahl(das_feld)
            markierung_setzen(das_feld, spieler2_mark, position)

            if sieg_check(das_feld, spieler2_mark):
                spielfeld_anzeigen(das_feld)
                print("spieler2 hat gewnnen!")
                spiel_laeuft=False
            else:
                if spilefeld_voll(das_feld):
                    spielfeld_anzeigen(das_feld)
                    print("unentschieden")
                    break
                else:
                    zug= "spieler1"


    if not neuses_spiel():
        break