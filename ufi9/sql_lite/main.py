
import sqlite3

connection= sqlite3.connect("personalverwaltung.db")
cursor=connection.cursor()
#sql_anweisung="CREATE TABLE Person(" \
#                "PersonID INTEGER PRIMARY KEY AUTOINCREMENT," \
#                "Name TEXT," \
#                "Vorname TEXT," \
#                "Groesse REAL," \
#                "Gewicht REAL," \
#                "Geburtsdatum DATE," \
#                "OrtID INTEGER" \
#                ")"

sql_anweisung2="INSERT INTO Person(" \
                "Name, Vorname, Groesse, Gewicht, Geburtsdatum, OrtID)" \
                "VALUES(" \
                "'Pohl', 'Waldemar', 1.90, 120.00, '29.09.1996' , 75180 )"

sql_anweisung3="INSERT INTO Person(" \
                "Name, Vorname, Groesse, Gewicht, Geburtsdatum, OrtID)" \
                "VALUES(" \
                "'Wald', 'Sven', 1.60, 40.00, '10.06.1992' , 76596 )"
sql_anweisung4=f"INSERT INTO Person(" \
                f"Name, Vorname, Groesse, Gewicht, Geburtsdatum, OrtID)" \
                f"VALUES(" \
                f"'{input("gebe Name: \n> ")}', '{input("gebe Vorname: \n> ")}', {float(input("gebe Groesse: \n> "))}, {float(input("gebe Gewicht: \n> "))}, '{input("gebe Geburtsdatum: \n> ")}' , {input("gebe OrtID: \n> ")} )"


cursor.execute(sql_anweisung4)
connection.commit()
connection.close()