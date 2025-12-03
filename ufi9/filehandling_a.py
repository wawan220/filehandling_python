file=open("append in text file.txt","a")
file.write("\n")
file.write(f"{input("schreibe was \n> ")}")
file.close()