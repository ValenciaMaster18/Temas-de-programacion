import hashlib

encontrado = 0
input_hash = input("Inserte la contraseña hasheada: ")
pass_doc = input("Inserte el diccionario: ")

try:
    pass_file = open(pass_doc, "r")
except:
    print ("Error:" + pass_doc + " no ha sido encontrado")

for palabra in pass_file:
    palabra_cifrada = palabra.encode('utf-8')
    palabra_hasheada = hashlib.md5(palabra_cifrada.strip())
    digest = palabra_hasheada.hexdigest()
    
    if digest == input_hash:
        print("contraseña encontrada!!! \n La contraseña es: " + palabra)
        encontrada = 1
        break
if not encontrada:
    print("Contraseña no  encontrada en el archivo " + pass_doc)