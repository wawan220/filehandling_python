
import sqlite3
#
#connection= sqlite3.connect("personalverwaltung.db")
#cursor=connection.cursor()
##sql_anweisung="CREATE TABLE Person(" \
##                "PersonID INTEGER PRIMARY KEY AUTOINCREMENT," \
##                "Name TEXT," \
##                "Vorname TEXT," \
##                "Groesse REAL," \
##                "Gewicht REAL," \
##                "Geburtsdatum DATE," \
##                "OrtID INTEGER" \
##                ")"
#
##ql_anweisung2="INSERT INTO Person(" \
##               "Name, Vorname, Groesse, Gewicht, Geburtsdatum, OrtID)" \
##               "VALUES(" \
##               "'Pohl', 'Waldemar', 1.90, 120.00, '29.09.1996' , 75180 )"
##
##ql_anweisung3="INSERT INTO Person(" \
##               "Name, Vorname, Groesse, Gewicht, Geburtsdatum, OrtID)" \
##               "VALUES(" \
##               "'Wald', 'Sven', 1.60, 40.00, '10.06.1992' , 76596 )"
##sql_anweisung4=f"INSERT INTO Person(" \
##                f"Name, Vorname, Groesse, Gewicht, Geburtsdatum, OrtID)" \
##                f"VALUES(" \
##                f"'{input("gebe Name: \n> ")}', '{input("gebe Vorname: \n> ")}', {float(input("gebe Groesse: \n> "))}, {float(input("gebe Gewicht: \n> "))}, '{input("gebe Geburtsdatum: \n> ")}' , {input("gebe OrtID: \n> ")} )"
#
#sql_anweisung5="SELECT * FROM Person"
#cursor.execute(sql_anweisung5)
#for datensatz in cursor:
#    print( str(datensatz[0])  +" "+ #PersonID
#           str(datensatz[1])  +" "+ #Name
#           str(datensatz[2])  +" "+ #Vorname
#           str(datensatz[3])  +" "+ #Groesse
#           str(datensatz[4])  +" "+ #Gewicht
#           str(datensatz[5])  +" "+ #Geburtsdatum
#           str(datensatz[6])  +"\n") #OrtID
#           
#
##cursor.execute(sql_anweisung5)
#connection.commit()
#connection.close()

#-------------------------------------------------------------


print("was möchtest du machen: \n (1) Todoliste ausgeben \n (2) Todos eingeben \n (3) Todos updaten \n (4) Eintrag löschen")
option= int(input("gebe deine wahl ein: \n> "))


connection= sqlite3.connect("todo_list.db")
cursor=connection.cursor()

#sql_anweisung="CREATE TABLE todos(" \
#               "TodoID INTEGER PRIMARY KEY AUTOINCREMENT," \
#               "Todoname TEXT," \
#               "DueDate DATE," \
#               "Status TEXT" \
#               ")"

if option==1:
    sql_anweisung_ausgabe="SELECT * FROM todos"
    cursor.execute(sql_anweisung_ausgabe)

    for datensatz in cursor:
        print( str(datensatz[0])  +" "+ #TodoID
                str(datensatz[1])  +" "+ #Todoname
                str(datensatz[2])  +" "+ #DueDate
                str(datensatz[3])  +"\n") #Status
         
elif option==2:
    sql_anweisung_eingabe=f"INSERT INTO todos(" \
                    f"Todoname, DueDate, Status)" \
                    f"VALUES(" \
                    f"'{input("gebe Todoname: \n> ")}', '{input("gebe DueDate: \n> ")}', '{input("gebe Status: \n> ")}' )"
    cursor.execute(sql_anweisung_eingabe)

elif option==3:
    update_input_key=input("was möchtest du verändern? Todoname, DueDate, Status \n> ")
    update_datensatz=input("Welche ID möchtest dus ändern? \n> ")
    Update_input_value=input("was soll eingetragen werden? \n>")
    sql_anweisung_update=f"UPDATE todos SET {update_input_key} = '{Update_input_value}' WHERE TodoID == {update_datensatz}"
    cursor.execute(sql_anweisung_update)
elif option==4:
    delete_datensatz=input("Welchen ID möchtest du löschen \n> ")
    sql_anweisung_delete=f"DELETE FROM todos WHERE TodoID == {delete_datensatz}"
    cursor.execute(sql_anweisung_delete)
    print(f"der eintrag mit ID : {delete_datensatz} wurde gelöscht!" )
else:
    print("eingabe ungültig")

connection.commit()
connection.close()


