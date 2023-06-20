""" Este modulo permite recuperar clave de acceso API a 
    microservicios contenidos en un archivo JSON 
"""

# uncompyle6 version 3.5.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.5 (default, Nov 16 2020, 22:23:17)
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)]
# Embedded file name: getJason.py
# Compiled at: 2022-06-15 03:15:55
# coding=utf-8

#copyright IS2 2022,2023 todos los derechos reservados

import json
import sys

class Singleton():
    """ Declara un metodo que devuelve la misma instancia de su propia clase """
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

class GetJson(Singleton):
    """ Clase que permite recuperar las Api tokens """
    def get_help(self):
        """ Muestra un mensaje de ayuda en pantalla """
        print("mensaje de ayuda:")
        print("- Debe ingresar el archivo json como primer argumento")
        print("- Debe ingresar un token como segundo argumento")

    def get_token(self, jsf, token):
        """ Muestra en pantalla la clave de acceso API correspondiente al token ingresado """
        try:
            with open(jsf, 'r') as (my_file):
                data = my_file.read()
                obj = json.loads(data)
                print (str(obj[token]))
        except:
            print("Error: No se ha podido recuperar la clave. ")
            print("Es posible que alguno de los argumentos sean invalidos. Ingrese -h para ayuda.")

#-----------MAIN-----------#
gj1 = GetJson()
gj2 = GetJson()

# El control de los argumentos se realiza previo al llamado de los metodos
try:
    if sys.argv[1]:

        # Si el primer argumento es -h se invoca al metodo getHelp del objeto GetJason
        if sys.argv[1] == "-h":
            gj1.get_help()

        else:
            try:
                if sys.argv[2]:
                    # Si existe un segundo argumento se invoca al metodo getToken
                    gj1.get_token(sys.argv[1], sys.argv[2])
            except:
                print("Error: Segundo argumento inextistente. Ingrese -h para ayuda.")
except:
    print("Error: Pirmer argumento inexistente. Ingrese -h para ayuda.")
