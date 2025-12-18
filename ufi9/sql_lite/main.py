
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

connection= sqlite3.connect("todo_list.db")
cursor=connection.cursor()
#sql_anweisung="CREATE TABLE todos(" \
#               "TodoID INTEGER PRIMARY KEY AUTOINCREMENT," \
#               "Todoname TEXT," \
#               "DueDate DATE," \
#               "Status TEXT" \
#               ")"

sql_anweisung=f"INSERT INTO todos(" \
                f"Todoname, DueDate, Status)" \
                f"VALUES(" \
                f"'{input("gebe Todoname: \n> ")}', '{input("gebe DueDate: \n> ")}', '{input("gebe Status: \n> ")}' )"

cursor.execute(sql_anweisung)
connection.commit()
connection.close()