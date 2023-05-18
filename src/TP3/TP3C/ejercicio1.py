from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass



class AbstractHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None



class PrimosHandler(AbstractHandler):
    def handle(self, n: int) -> str:
        if self.is_primo(n):
            return f"Clase primos consume al numero {n}"
        else:
            return super().handle(n)
        
    def is_primo(self, num):
        for i in range (2, num):
            if num % i == 0:
                return False
        return True


class ParesHandler(AbstractHandler):
    def handle(self, n: int) -> str:
        if n % 2 == 0:
            return f"Clase pares consume al numero {n}"
        else:
            return super().handle(n)




def client_code(handler: Handler) -> None:

    for i in range(101):
        print("\n")
        print(f"Que clase consumira a {i}?")
        result = handler.handle(i)
        if result:
            print(f"{result}", end="")
        else:
            print(f"{i} no fue consumido por nadie", end="")


if __name__ == "__main__":

    primos = PrimosHandler()
    pares = ParesHandler()

    # Creando cadena
    primos.set_next(pares)

    print("Chain: primos > pares")
    client_code(primos)
