import os
import json

def generar(event, name, dni, email, localitzacio):
    
    # event = json.loads(event)
    print(event)
    os.system("pdfforms inspect memo.pdf")

    file = open("data.csv", "w")
    file.write("memo.pdf,,,\n")

    file.write("0,Entitat,")
    event["Entitat"] = 'MataroViva'
    file.write(event["Entitat"])
    
    file.write("\n11,email,")
    file.write(email)
    
    file.write("\n7,cif,")
    event["cif"] = 'R9347909E'
    file.write(event["cif"])
    
    file.write("\n9,dniuser,")
    file.write(dni)
    
    file.write("\n2,cp,")
    event["CodiPost"] = '08302'
    file.write(event["CodiPost"])
    
    file.write("\n8,NomCog,")
    file.write(name)
    
    file.write("\n4,Poblacio,")
    file.write(localitzacio)
    
    file.write("\n5,tlf,")
    event["Telefon"] = '623789321'
    file.write(event["Telefon"])
    
    file.write("\n")
    file.close()
    print('aa')
    os.system("pdfforms fill data.csv")
    print('bb')
