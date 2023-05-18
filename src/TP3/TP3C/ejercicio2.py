from collections.abc import Iterable, Iterator


class Chain_iterator(Iterator):

    _position: int = None
    _reverse: bool = False

    def __init__(self, collection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class Cadena(Iterable):
    def __init__(self) -> None:
        self._collection = []

    def __iter__(self) -> Chain_iterator:
        """Devuelve un objeto iterador, por defecto es en orden ascendente"""
        return Chain_iterator(self._collection)
 
    def get_reverse_iterator(self) -> Chain_iterator:
        # retorna lo mismo que __iter__ pero inicializa el atributo reverse
        # del objeto de la clase iteradora en True
        return Chain_iterator(self._collection, True)

    def add_item(self, item):
        self._collection.append(item)


if __name__ == "__main__":
    collection = Cadena()
    
    # Cadena: aT?%Dae#Ex
    collection.add_item("a")
    collection.add_item("T")
    collection.add_item("?")
    collection.add_item("%")
    collection.add_item("D")
    collection.add_item("a")
    collection.add_item("e")
    collection.add_item("#")
    collection.add_item("E")
    collection.add_item("x")



    print("Sentido directo")
    print("".join(collection), end="")
    print("\n")


    print("Sentido Reverso")
    print("".join(collection.get_reverse_iterator()), end="")
    print("\n")
 