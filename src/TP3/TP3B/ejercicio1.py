from abc import ABC, abstractmethod
from pythonping import ping

# Interface para pingReal y pingProxy
class Subject(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass



class Ping_real(Subject):

    def execute(self, ip_direction):
        # Realiza 10 intentos de ping llamando al metodo que evalua si la ip inicia con 192
        for i in range(10):
            if self.direction_control(ip_direction):
                # Si en alguno de los 10 intentos se da la condicion, retorna el ping
                return ping(f"{ip_direction}", verbose= True)
    
        # Si no puede realizar el ping, retorna acceso denegado
        return ("Acceso denegado")
    

    # Realiza un ping a una direccion sin ningun control
    def execute_free(self, direction):
        print("Realizando ping sin ningun control")
        return ping(f"{direction}", verbose=True)
    
    # Metodo para controlar si una ip comienza con 192
    def direction_control(self, str):
        if(str.startswith("192")):
            return True
        else: return False



class Ping_proxy(Subject):

    def __init__(self, ping_real: Ping_real) -> None:
        self.ping_real = ping_real
    def execute(self, ip_direction):
        if(ip_direction == "192.168.0.254"):
            direction = 'www.google.com'
            return self.ping_real.execute_free(direction)
        else:
            return self.ping_real.execute(ip_direction)     
        


if __name__ == "__main__":
    ip = "192.168.0.254"

    ping_real = Ping_real()

    ping_proxy = Ping_proxy(ping_real)
    print(ping_proxy.execute(ip)) 

