import matplotlib.pyplot as plt
import numpy as np

def collatz(n):
    sucesion = [n]
    if n == 1:
        sucesion.append(n)
        return sucesion
    if n > 0:
        while n != 1:
            if n % 2:  
                n = n * 3 + 1
            else:
                n //= 2
            sucesion.append(n)
    return sucesion

arrayEjeX = []
arrayEjeY = []

for i in range(1, 11):    
    resultado = collatz(i)
    #print("Resultado de la sucesion de", i, resultado)

    arrayEjeX.append(i)
    arrayEjeY.append(len(resultado))


# Los parametros del grafico son
# EJE X: Los numeros de 1 al 10000
# EJE Y: La cantidad de pasos de cada valor de x hasta llegar a la secuencia repetitiva
plt.plot(arrayEjeX, arrayEjeY)
plt.show()