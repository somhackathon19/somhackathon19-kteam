import os
import json

def generar(event, name):
    print(event)
    print(name)
    os.system("pdfforms inspect memo.pdf")

    file = open("data.csv", "w")
    file.write("memo.pdf,,,\n")

    file.write("0,Entitat,")
    file.write(event["Entitat"])
    
    file.write("\n11,email,")
    file.write(event["email"])
    
    file.write("\n7,cif,")
    file.write(event["cif"])
    
    file.write("\n2,cp,")
    file.write(event["CodiPost"])
    
    file.write("\n8,NomCog,")
    file.write(name)
    
    file.write("\n4,Poblacio,")
    file.write(event["Poblacio"])
    
    file.write("\n10,tlf,")
    file.write(event["Telefon"])
    
    file.write("\n")
    file.close()

    os.system("pdfforms fill data.csv")
