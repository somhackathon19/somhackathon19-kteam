import os
import json

with open('recive.json', encoding='utf-8') as data_file:
    var = json.loads(data_file.read())

os.system("pdfforms inspect memo.pdf")

file = open("data.csv", "w")


file.write("memo.pdf,,,\n")

file.write("0,Entitat,")
file.write(var["Entitat"])


file.write("\n11,email,")
file.write(var["email"])

file.write("\n7,cif,")
file.write(var["cif"])

file.write("\n2,cp,")
file.write(var["CodiPost"])

file.write("\n8,NomCog,")
file.write(var["Nom&Cog"])

file.write("\n4,Poblacio,")
file.write(var["Poblacio"])

file.write("\n10,tlf,")
file.write(var["Telefon"])
    
file.write("\n")



file.close()

os.system("pdfforms fill data.csv")
