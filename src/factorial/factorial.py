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


#En caso de que no se pasen parametros
if len (sys.argv) == 1:
    print("Debe igresar 2 números!")
    num1 = int(input("Ingrese el límite 'hasta' (se calculará desde 1 hasta el número indicado): "))
    num2 = int(input("Ingrese el 'desde' (se calculará desde el numero indicado hasta 60): "))

    print("----------------")
    print("Calculo de factorial para los números entre 1 y", num1)
    for i in range(1, num1+1):
            if(i < 0):
                print(factorial(i))
            else:
                print("Factorial ",i,"! es ", factorial(i)) 

    print("----------------")
    print("Calculo de factorial para los números entre", num2, "y 60")
    for i in range(num2, 61):
        if(i < 0):
            print(factorial(i))
        else:
            print("Factorial ",i,"! es ", factorial(i)) 

    sys.exit()

#En caso de que se pasen los 2 numeros como parámetro
elif len (sys.argv) == 3:
    num1= int(sys.argv[1])
    num2= int(sys.argv[2])

    print("----------------")
    print("Calculo de factorial para los números entre 1 y", num1)
    for i in range(1, num1+1):
            if(i < 0):
                print(factorial(i))
            else:
                print("Factorial ",i,"! es ", factorial(i)) 

    print("----------------")
    print("Calculo de factorial para los números entre", num2, "y 60")
    for i in range(num2, 61):
        if(i < 0):
            print(factorial(i))
        else:
            print("Factorial ",i,"! es ", factorial(i)) 

    sys.exit()
    
# Archivo modificado para:
#   - solicitar parametro "hasta" y calcular factorial desde 1 hasta el nro indicado.
#   - Solicitar parametro "desde" y calcular factorial desde el nro indicado hasta 60.
 