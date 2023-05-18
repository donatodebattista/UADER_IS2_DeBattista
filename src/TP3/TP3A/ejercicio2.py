<<<<<<< HEAD
class Singleton():
    instancia = None

    def __new__(cls):
        if cls.instancia == None:
            cls.instancia = super().__new__(cls)
        return cls.instancia


class Presupuesto(Singleton):

    def getIVA(self, n):
        return (21*n)/100
    
    def getIIBB(self, n):
        return (n*5)/100
    
    def getImpuestoMunicipal(self, n):
        return (n*1.2)/100
        
    def getTotal(self, n):
        return self.getIVA(n) + self.getIIBB(n) + self.getImpuestoMunicipal(n) + n


presupuesto1 = Presupuesto()

=======
class Singleton():
    instancia = None

    def __new__(cls):
        if cls.instancia == None:
            cls.instancia = super().__new__(cls)
        return cls.instancia


class Presupuesto(Singleton):

    def getIVA(self, n):
        return (21*n)/100
    
    def getIIBB(self, n):
        return (n*5)/100
    
    def getImpuestoMunicipal(self, n):
        return (n*1.2)/100
        
    def getTotal(self, n):
        return self.getIVA(n) + self.getIIBB(n) + self.getImpuestoMunicipal(n) + n


presupuesto1 = Presupuesto()

>>>>>>> 380ec65d399c497c79285d5753787abefbf16d1a
print(presupuesto1.getTotal(3)) 