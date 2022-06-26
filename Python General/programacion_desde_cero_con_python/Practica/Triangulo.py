frase = input("Digite una frase: ")
tamaño= len(frase)

com = frase[0:1]
com1 = frase[4:5]



if tamaño == 5:
    if  com == com1:
        print("\t          "+frase[0])
        print("            "+frase[1]+"\t       "+frase[1])
        print("        "+frase[2]+"\t            "+frase[2])
        print("   "+frase[3]+"\t                         "+frase[3])
        print(frase[4] +    "\t"+frase[1]   +      "\t  "+frase[2]   +    "\t    "+frase[3]+"\t    "+frase[4])
        print()
        print("Programa finalizado")
    else:
        print(com + " y " + com1 + " Las letra inicial y final no coinciden")
else:
    print("El tamaño no cumple los requisitos  tiene: ",tamaño," caracteres")   
    
    


