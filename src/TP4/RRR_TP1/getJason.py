import json
import sys

class Handler(object):
    next_handler = None


    def __init__(self):
        self.next_Handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler
    
    def handle(self, request):
        if self.next_handler == None:
           print("Ninguna cuenta pudo realizar el pago")
           return
        self.next_handler.handle(request)




class Cuenta1Handler(Handler):

    def __init__(self, saldo):
        self.saldo = saldo

    def handle(self, monto_a_pagar):
        print("Intentando realizar pago con cuenta 1")

        if self.saldo >= monto_a_pagar:
            self.saldo = self.saldo - monto_a_pagar

            try:
                with open("./sitedata.json", 'r') as (my_file):
                    data = my_file.read()
                    obj = json.loads(data)
                    print ("token", str(obj["token1"]))
                    print("pago realizado con cuenta 1") 
                    return monto_a_pagar

            except:
                print("Error: No se ha podido recuperar la clave. ")
        else:
            print("Cuenta 1 no pudo pagar")
            super(Cuenta1Handler, self).handle(monto_a_pagar)

class Cuenta2Handler(Handler):

    def __init__(self, saldo):
        self.saldo = saldo

    def handle(self, monto_a_pagar):
        print("Intentando realizar pago con cuenta 2")
        if self.saldo >= monto_a_pagar:
            self.saldo = self.saldo - monto_a_pagar
            try:
                with open("./sitedata.json", 'r') as (my_file):
                    data = my_file.read()
                    obj = json.loads(data)
                    print("pago realizado con cuenta 2") 
                    print ("token:", str(obj["token2"]))
                    return monto_a_pagar

            except:
                print("Error: No se ha podido recuperar la clave. ")

        else:
            print("Cuenta 2 no pudo pagar")
            super(Cuenta2Handler, self).handle(monto_a_pagar)


        
class pedido_pago():
    
    def __init__(self, monto, nro_pago):
        self.monto = monto
        # El nro de pago se pasa como atributo por practicidad del ejercicio
        self.nro_pago = nro_pago




#!-----------MAIN-----------#
cuenta1 = Cuenta1Handler(1000)
cuenta2 = Cuenta2Handler(2000)
cuenta1.set_next(cuenta2)

pago1 = pedido_pago(500, 1)
pago2 = pedido_pago(1000, 2)
pago3 = pedido_pago(500, 3)
pago4 = pedido_pago(2000, 4)

cuenta1.handle(pago1.monto)
cuenta1.handle(pago2.monto)
cuenta1.handle(pago3.monto)
cuenta1.handle(pago4.monto)

historial_pagos = []

historial_pagos.append(cuenta1.handle(pago1.monto))
historial_pagos.append(cuenta1.handle(pago2.monto))
historial_pagos.append(cuenta1.handle(pago3.monto))
historial_pagos.append(cuenta1.handle(pago4.monto))

print(historial_pagos)
