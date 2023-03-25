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
   print("Debe informar el rango de factoriales a calcular!")
   num1 = int(input("Ingrese el numero inferior del rango: "))
   num2 = int(input("Ingrese el numero superior del rango: "))

   for i in range(num1, num2+1):
        if(i < 0):
            print(factorial(i))
        else:
            print("Factorial ",i,"! es ", factorial(i)) 

   sys.exit()

elif len (sys.argv) == 2:
    print("Debe igresar también el numero superior del rango")
    num1 = int(sys.argv[1])
    print("Limite inferior: ", num1)
    num2 = int(input("Ingrese el numero superior del rango: "))

    for i in range(num1, num2+1):
        if(i < 0):
            print(factorial(i))
        else:
            print("Factorial ",i,"! es ", factorial(i)) 

    sys.exit()
    
elif len (sys.argv) == 3:
    num1= int(sys.argv[1])
    num2= int(sys.argv[2])
    for i in range(num1, num2+1):
        if(i < 0):
            print(factorial(i))
        else:
            print("Factorial ",i,"! es ", factorial(i)) 

#Archivo modificado para solicitar rangos como argumentos
 