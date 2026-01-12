import os



def spielfeld_anzeigen(spielfeld):
    os.system('cls' if os.name=="nt" else "clear")

    print(spielfeld[7] + " | " + spielfeld[8] + " | " + spielfeld[9])
    print("---------")
    print(spielfeld[4] + " | " + spielfeld[5] + " | " + spielfeld[6])
    print("---------")
    print(spielfeld[1] + " | " + spielfeld[2] + " | " + spielfeld[3])
    
    



test_spielfeld=["#","X","O","X","O","X","O","X","O","X"]
#test_spielfeld=["#","1","2","3","4","5","6","7","8","9"]
spielfeld_anzeigen(test_spielfeld)


def spieler_eingabe():
    markierung=""
    while markierung !="X" and markierung !="O":
        markierung=input("Spieler1: X oder O ?\n> ").upper()
    if markierung == "X":
        return ("X","O")
    else:
        return ("O","X")
    
spieler1, spieler2 = spieler_eingabe()

print(f"Spieler1: {spieler1}  |  Spieler2: {spieler2}")


def markierung_setzen(spielfeld, markierung, position):
    spielfeld[position]=markierung

markierung_setzen(test_spielfeld, "§", 8)
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
print(sieg_check(test_spielfeld,"X"))