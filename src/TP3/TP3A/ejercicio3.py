<<<<<<< HEAD
""" En este ejercicio se utilizó el patron creacional factory """

from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def operation(self) -> str:
        hamburguesa = self.factory_method()
        result = f"Modo de entrega de hamburguesa: {hamburguesa.modo_de_entrega()}"

        return result


class Creador_hamburguesa_mostrador(Creator):
    def factory_method(self) -> Hamburguesa:
        return Hamburguesa_mostrador()

class Creador_hamburguesa_cliente(Creator):
    def factory_method(self) -> Hamburguesa:
        return Hamburguesa_cliente()

class Creador_hamburguesa_delivery(Creator):
    def factory_method(self) -> Hamburguesa:
        return Hamburguesa_delivery()


class Hamburguesa(ABC):


    @abstractmethod
    def modo_de_entrega(self) -> str:
        pass


class Hamburguesa_mostrador(Hamburguesa):
    def modo_de_entrega(self) -> str:
        return "entrega en mostrador"

class Hamburguesa_cliente(Hamburguesa):
    def modo_de_entrega(self) -> str:
        return "retira el cliente"

class Hamburguesa_delivery(Hamburguesa):
    def modo_de_entrega(self) -> str:
        return "entrega por delivery"
    
def client_code(creator: Creator) -> None:
    print(creator.operation()) 


if __name__ == "__main__":

    print("Se crea una hamburguesa para retirar en mostrador")
    client_code(Creador_hamburguesa_mostrador())
    print("\n")

    print("Se crea una hamburguesa para ser retirada por el cliente")
    client_code(Creador_hamburguesa_cliente())
    print("\n")

    print("Se crea una hamburguesa que será entregada por delivery")
    client_code(Creador_hamburguesa_delivery())
=======
""" En este ejercicio se utilizó el patron creacional factory """

from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def operation(self) -> str:
        hamburguesa = self.factory_method()
        result = f"Modo de entrega de hamburguesa: {hamburguesa.modo_de_entrega()}"

        return result


class Creador_hamburguesa_mostrador(Creator):
    def factory_method(self) -> Hamburguesa:
        return Hamburguesa_mostrador()

class Creador_hamburguesa_cliente(Creator):
    def factory_method(self) -> Hamburguesa:
        return Hamburguesa_cliente()

class Creador_hamburguesa_delivery(Creator):
    def factory_method(self) -> Hamburguesa:
        return Hamburguesa_delivery()


class Hamburguesa(ABC):


    @abstractmethod
    def modo_de_entrega(self) -> str:
        pass


class Hamburguesa_mostrador(Hamburguesa):
    def modo_de_entrega(self) -> str:
        return "entrega en mostrador"

class Hamburguesa_cliente(Hamburguesa):
    def modo_de_entrega(self) -> str:
        return "retira el cliente"

class Hamburguesa_delivery(Hamburguesa):
    def modo_de_entrega(self) -> str:
        return "entrega por delivery"
    
def client_code(creator: Creator) -> None:
    print(creator.operation()) 


if __name__ == "__main__":

    print("Se crea una hamburguesa para retirar en mostrador")
    client_code(Creador_hamburguesa_mostrador())
    print("\n")

    print("Se crea una hamburguesa para ser retirada por el cliente")
    client_code(Creador_hamburguesa_cliente())
    print("\n")

    print("Se crea una hamburguesa que será entregada por delivery")
    client_code(Creador_hamburguesa_delivery())
>>>>>>> 380ec65d399c497c79285d5753787abefbf16d1a
