import os
import json

def generar(event, name):
    
    # event = json.loads(event)
    print(event)
    os.system("pdfforms inspect memo.pdf")

    file = open("data.csv", "w")
    file.write("memo.pdf,,,\n")

    file.write("0,Entitat,")
    event["Entitat"] = 'Mavent'
    file.write(event["Entitat"])
    
    file.write("\n11,email,")
    event["email"] = 'email'
    file.write(event["email"])
    
    file.write("\n7,cif,")
    event["cif"] = '123456789V'
    file.write(event["cif"])
    
    file.write("\n2,cp,")
    event["CodiPost"] = '08310'
    file.write(event["CodiPost"])
    
    file.write("\n8,NomCog,")
    file.write(name)
    
    file.write("\n4,Poblacio,")
    file.write(event["localitzacio"])
    
    file.write("\n10,tlf,")
    event["Telefon"] = '623789321'
    file.write(event["Telefon"])
    
    file.write("\n")
    file.close()
    print('aa')
    os.system("pdfforms fill data.csv")
    print('bb')
