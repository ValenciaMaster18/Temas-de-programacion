#!/usr/bin/python
# -*- coding: utf-8 -*-
 
while True:
    try:
        value=input("Ingrese temperatura en grados Celsius:")
    except KeyboardInterrupt:
        # CTRL+C
        break
 
    # su pulsa por ejemplo X, finalizara el programa
    if value=="X":
        break
 
    # controlamos que no ponga letras
    try:
        C=float(value)
    except ValueError:
        print ("Tiene que ser un valor numerico")
        continue
 
    F=(1.8*C)+32
    K=C+273.15
    R=(C+273.15)*1.8
 
    print ("La temperatura en grados Fahrenheit es:",F,"")
    print ("La temperatura en grados Kelvin es:",K,"")
    print ("La temperatura en grados Rankine es:",R,"")
    print ("")