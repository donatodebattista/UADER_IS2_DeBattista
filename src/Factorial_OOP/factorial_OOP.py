class Factorial:
    
    def __init__(self, min, max):
        self.min = int(min) 
        self.max = int(max)

    def run(self):
        for i in range(self.min, self.max +1):
            if(i < 0):
                print(i, "!: El factorial de un número negativo no existe")
            elif (i==0):
                print(i, "!: 1")
            else:
                fact = 1
                n = i
                while(n > 1):
                    fact *= n
                    n -= 1
                print("Factorial de ", i, ": ", fact)

nuevoFactorial = Factorial(4, 12)

print("Factorial entre", nuevoFactorial.min, "y", nuevoFactorial.max)
nuevoFactorial.run()

