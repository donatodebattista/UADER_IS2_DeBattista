class Singleton():
    _instancia = None

    def __new__(cls):
        if cls._instancia == None:
            cls._instancia = super().__new__(cls)
        return cls._instancia


class Factorial(Singleton):
    def getFactorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.getFactorial(n-1)
        

factorial1 = Factorial()
print(factorial1.getFactorial(5)) 
print(factorial1)

factorial2 = Factorial()
print(factorial2.getFactorial(3))
print(factorial2)

# Imprimo factorial1 y factorial2 para verificar que
# son la misma instancia (misma dirección de memoria)