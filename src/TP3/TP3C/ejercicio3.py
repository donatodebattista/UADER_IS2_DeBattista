from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List



class Subject(ABC):
    """
    Interface que representa al objeto notificador.
    """

    @abstractmethod
    def attach(self, observer: Observador) -> None:
        """
        Añade un nuevo observador a Subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observador) -> None:
        """
        Elimina un observador de Subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notifica a los observadores de algun evento.
        """
        pass


class Notificador_de_IDs(Subject):

    # El id arranca en None por defecto, cuando cambie de estado se debe notificar
    _id: str = None
    _observers: List[Observador] = []

    def attach(self, observer: Observador) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observador) -> None:
        self._observers.remove(observer)



    # Metodos de manejo de suscripciones
    # Cuando el id del Subject cambia, se debe notificar
    def notify(self) -> None:
        print("Subject: Notificando a los observadores...")
        for Observador in self._observers:
            Observador.update(self)

    def cambio_de_id(self, newID) -> None:

        print("El observado está cambiando de id")
        self._id = newID

        print(f"Observado: He cambiado de id: {self._id}")
        self.notify()




class Observador(ABC):
    """ Interface para los observadores"""

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Recibe la actualizacion de id del Subject.
        """
        pass




class SuscriptorA(Observador):

    _id = 'a111'
    def update(self, subject: Subject) -> None:
        if subject._id == self._id:
            print("El observador A reacciono")


class SuscriptorB(Observador):
    _id = 'b222'

    def update(self, subject: Subject) -> None:
        if subject._id == self._id:
            print("El observador B reacciono")

class SuscriptorC(Observador):
    _id = 'c333'

    def update(self, subject: Subject) -> None:
        if subject._id == self._id:
            print("El observador C reacciono")


class SuscriptorD(Observador):
    _id = 'd444'

    def update(self, subject: Subject) -> None:
        if subject._id == self._id:
            print("El observador D reacciono")



if __name__ == "__main__":
    # The client code.

    # Creo la clase observada y los observadores
    notificador = Notificador_de_IDs()
    observadorA = SuscriptorA()
    observadorB = SuscriptorB()
    observadorC = SuscriptorC()
    observadorD = SuscriptorD()

    # Agrego los observadores a la clase observada
    notificador.attach(observadorA)
    notificador.attach(observadorB)
    notificador.attach(observadorC)
    notificador.attach(observadorD)


    # El cambio de id es un evento que se debe notificar a los observadores
    # Mediante este metodo, el objeto observado cambia su estado (valor de su id) 
    # y llama al metodo notify, el cual recorre la lista de observadores e implementa el metodo
    # update de cada uno de ellos, para comparar si los IDs son iguales.
    notificador.cambio_de_id('a111')
    print("")
    notificador.cambio_de_id('nfj2')
    print("")
    notificador.cambio_de_id('ksh3')
    print("")
    notificador.cambio_de_id('b222')
    print("")
    notificador.cambio_de_id('c333')
    print("")
    notificador.cambio_de_id('sgeg')
    print("")
    notificador.cambio_de_id('2421')
    print("")
    notificador.cambio_de_id('d444')