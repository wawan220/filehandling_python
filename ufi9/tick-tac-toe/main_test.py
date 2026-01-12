# print([1,2,3])
# print([4,5,6])
# print([7,8,9])

def ausgabe(reihe1,reihe2,reihe3):
    print(reihe1)
    print(reihe2)
    print(reihe3)

def nutzer_eingabe():
    eingabe="falsch"
    akzeptierte_werte=range(1,10)
    im_bereich=False

    while eingabe.isdigit()==False or im_bereich==False:
        eingabe=input("gebe eine zahl zwischen 1-10 ein: \n> ")

        if eingabe.isdigit()==False:
            print("ungültige eingabe bitte erneut")

        if eingabe.isdigit()==True:
            if int(eingabe) in akzeptierte_werte:
                im_bereich=True
            else:
                print("eingabe befindet sich nicht im bereich!")
                im_bereich=False


    return int(eingabe)-1
# reihe=[1,2,3]
reihe1=["","",""]
reihe2=["","",""]
reihe3=["","",""]

reihe2[1]="X"
reihe2[2]="O"

eingabe=nutzer_eingabe()
# eingabe=int(input("bitte gebe einen wert ein: \n> "))
print(eingabe)
ausgabe(reihe1,reihe2,reihe3)