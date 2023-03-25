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
        print(num, "! Factorial de un número negativo no existe")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 



if len (sys.argv) == 1:
   print("Debe ingresar un numero!")
   num1 = int(input("Ingrese el número límite: "))

   for i in range(1, num1+1):
        if(i < 0):
            print(factorial(i))
        else:
            print("Factorial ",i,"! es ", factorial(i)) 

   sys.exit()

elif len (sys.argv) == 2:
    num1 = int(sys.argv[1])
    for i in range(1, num1+1):
        if(i < 0):
            print(factorial(i))
        else:
            print("Factorial ",i,"! es ", factorial(i)) 

    sys.exit()


#Archivo modificado para solicitar rangos como argumentos
 