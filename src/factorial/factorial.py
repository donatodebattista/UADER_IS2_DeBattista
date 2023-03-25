#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 



if len(sys.argv) == 1:
   print("Debe informar un número!")
   num = int(input("Ingrese el numero: "))
   print("Factorial ",num,"! es ", factorial(num)) 
   sys.exit()
else:
    num=int(sys.argv[1])
    print("Factorial ",num,"! es ", factorial(num)) 

#Archivo modificado para solicitar argumento en caso de que se omita
 