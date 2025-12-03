
file=open("lesen und schreiben in text file.txt","a+")
file.writelines("\n")
file.writelines("text hinten dran gehaengt")
file.seek(0)
inhalt=file.readlines()
file.close()

print(inhalt)