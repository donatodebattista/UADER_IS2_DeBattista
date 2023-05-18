<<<<<<< HEAD
""" En este ejercicio se utilizó el patron creacional factory """

from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def operation(self) -> str:
        factura = self.factory_method()
        result = f"TIPO DE FACTURA: {factura.mostrar_tipo_factura()}"

        return result


class Creador_factura_IVA_responsable(Creator):
    def factory_method(self) -> Factura:
        return Factura_IVA_responsable()

class Creador_factura_IVA_no_inscripto(Creator):
    def factory_method(self) -> Factura:
        return Factura_IVA_no_inscripto()

class Creador_factura_IVA_excento(Creator):
    def factory_method(self) -> Factura:
        return Factura_IVA_excento()


class Factura(ABC):

    @abstractmethod
    def mostrar_tipo_factura(self) -> str:
        pass


class Factura_IVA_responsable(Factura):
    def mostrar_tipo_factura(self) -> str:
        return "Factura IVA responsable"

class Factura_IVA_no_inscripto(Factura):
    def mostrar_tipo_factura(self) -> str:
        return "Factura IVA no inscripto"

class Factura_IVA_excento(Factura):
    def mostrar_tipo_factura(self) -> str:
        return "Factura IVA excento"
    
def client_code(creator: Creator) -> None:
    print(creator.operation()) 


if __name__ == "__main__":

    print("Factura 1")
    client_code(Creador_factura_IVA_responsable())
    print("\n")

    print("Factura 2")
    client_code(Creador_factura_IVA_no_inscripto())
    print("\n")

    print("Factura 3")
    client_code(Creador_factura_IVA_excento())
=======
""" En este ejercicio se utilizó el patron creacional factory """

from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def operation(self) -> str:
        factura = self.factory_method()
        result = f"TIPO DE FACTURA: {factura.mostrar_tipo_factura()}"

        return result


class Creador_factura_IVA_responsable(Creator):
    def factory_method(self) -> Factura:
        return Factura_IVA_responsable()

class Creador_factura_IVA_no_inscripto(Creator):
    def factory_method(self) -> Factura:
        return Factura_IVA_no_inscripto()

class Creador_factura_IVA_excento(Creator):
    def factory_method(self) -> Factura:
        return Factura_IVA_excento()


class Factura(ABC):

    @abstractmethod
    def mostrar_tipo_factura(self) -> str:
        pass


class Factura_IVA_responsable(Factura):
    def mostrar_tipo_factura(self) -> str:
        return "Factura IVA responsable"

class Factura_IVA_no_inscripto(Factura):
    def mostrar_tipo_factura(self) -> str:
        return "Factura IVA no inscripto"

class Factura_IVA_excento(Factura):
    def mostrar_tipo_factura(self) -> str:
        return "Factura IVA excento"
    
def client_code(creator: Creator) -> None:
    print(creator.operation()) 


if __name__ == "__main__":

    print("Factura 1")
    client_code(Creador_factura_IVA_responsable())
    print("\n")

    print("Factura 2")
    client_code(Creador_factura_IVA_no_inscripto())
    print("\n")

    print("Factura 3")
    client_code(Creador_factura_IVA_excento())
>>>>>>> 380ec65d399c497c79285d5753787abefbf16d1a
