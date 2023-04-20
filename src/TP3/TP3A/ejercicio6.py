#*-------------------------------------------------------------------------
#* prototipo.py
#* Ejemplo para creación de prototipos
#*-------------------------------------------------------------------------
from abc import ABC, abstractmethod
import time
from datetime import datetime
import copy
import os

#*-------------------------------------------------------------------------
#* La clase prototipo utilizada como ejemplo puede estar en una librería
#* externa y ser importada.
#* Define los atributos mandatorios y relevantes, simula actividad por
#* medio de retardos
#*-------------------------------------------------------------------------
# Class Creation
class Prototype(ABC):
    # Constructor:
    def __init__(self):
        time.sleep(1) # Las demás clases tambien tienen un tiempo de 1s

        # Base attributes
        self.height = None
        self.age = None
        self.defense = None
        self.attack = None

    # Metodo para mostrar los atributos en pantalla
    def getSpecifications(self):
        return f"Height: {self.height}. Age: {self.age}. Defense: {self.defense}. Attack: {self.attack}."

#*------------------------------------------------------------------------------
#* El método clone() no está definido en el prototipo y mediante @abstractmethod
#* se fuerza a que cualquier instancia que se haga de ésta clase lo tenga que
#* definir.
#*------------------------------------------------------------------------------
    # Clone Method:
    @abstractmethod
    def clone(self):
        pass 


#*------------------------------------------------------------------------------
#* Clase productiva que puedo querer usar como plantilla
#*------------------------------------------------------------------------------
class Shopkeeper(Prototype):
    def __init__(self, height, age, defense, attack):
        super().__init__()
        time.sleep(1) # Se suma al tiempo de la clase super
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        # Subclass-specific Attribute
        self.charisma = 30

    # Overwrite agregando el atributo especifico de la clase
    def getSpecifications(self):
        return super().getSpecifications() + (f" Charisma: {self.charisma}")

    # Implementa el método de clonado mediante una copia de arbol de métodos
    def clone(self):
        return copy.deepcopy(self)    


class Warrior(Prototype):
    def __init__(self, height, age, defense, attack):
        super().__init__()

        time.sleep(1) # Se suma al tiempo de la clase super
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        # Concrete class attribute
        self.stamina = 60

    # Overwrite agregando el atributo especifico de la clase
    def getSpecifications(self):
        return super().getSpecifications() + (f" Stamina: {self.stamina}")


    # Overwriting Cloning Method
    def clone(self):
        return copy.deepcopy(self)  

class Mage(Prototype):
    def __init__(self, height, age, defense, attack):
        super().__init__()
        time.sleep(1) # Se suma al tiempo de la clase super
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        # Concrete class attribute
        self.mana = 100

    # Overwrite agregando el atributo especifico de la clase
    def getSpecifications(self):
        return super().getSpecifications() + (f" Mana: {self.mana}")


    # Overwriting Cloning Method
    def clone(self):
        return copy.deepcopy(self) 

#*--------------------------------------------------------------------------
#* Punto de entrada de ejecución
#*--------------------------------------------------------------------------
os.system("clear")
print("Ejemplo de taller para patrón prototipo")

dt = datetime.now()
print('Comienzo creando un objeto Shopkeeper NPC: ', dt)
shopkeeper = Shopkeeper(180, 22, 5, 8)

dt = datetime.now()
print('Finaliza la creación del objeto Shopkeeper NPC: ', dt)
print('Atributos: ' + ', '.join("%s: %s" % item for item in vars(shopkeeper).items()))

dt = datetime.now()
print('Instanciando ahora trader: ', dt)
for i in range(5):
    shopkeeper = Shopkeeper(180, 22, 5, 8)
    dt = datetime.now()
    print(f'Creo Shopkeeper NPC {i} at: ', dt)

dt = datetime.now()
print('Finalizó de crear el grupo trader: ', dt)

# Aqui comienza el desarrollo del punto 6
print('CREACION DE PROTOTIPOS:')
dt = datetime.now()
print("- Comienza la creacion de shopkeeper...", dt)
shopkeeper_template = Shopkeeper(180, 22, 5, 8)
dt = datetime.now()
print("- Finalizo la creacion de shopkeeper:", dt)

print("- Comienza la creacion de warrior...", dt)
warrior_template = Warrior(185, 22, 4, 21)
dt = datetime.now()
print("- Finalizó la creacion de warrior: ", dt)

print("- Comienza la creacion de warrior...", dt)
mage_template = Mage(172, 65, 8, 15)
dt = datetime.now()
print("- Finalizó la creacion de mage: ", dt)




# Una vez creadas los prototipos, comienza la clonacion
# Para este ejercicio se clonaran 20 shopkeepers
print("COMIENZA LA CLONACION")
for i in range(1, 21): 
    dt = datetime.now()
    print(f"Creando clon de shopkeeper N° {i}: {dt}")
    time.sleep(2) # Simula que la clonación lleva tiempo
    shopkeeper_clone = shopkeeper_template.clone()
    dt = datetime.now()
    print(f"Clon de shopkeeper {i} Finalizado. {dt}") 
    print(f"Atributos: {shopkeeper_clone.getSpecifications()}")
    print("-----------------------------------")

dt = datetime.now()
print('Finalizó la clonación de shopkeepers at', dt)
