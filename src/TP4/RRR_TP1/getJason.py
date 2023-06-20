# uncompyle6 version 3.5.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.5 (default, Nov 16 2020, 22:23:17) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)]
# Embedded file name: getJason.py
# Compiled at: 2022-06-15 03:15:55
# coding=utf-8


import json, sys

class Singleton():
    _instancia = None

    def __new__(cls):
        if cls._instancia == None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

class GetJason(Singleton):

    def getHelp(self):
        print("mensaje de ayuda: \n - Debe ingresar el archivo json como primer argumento\n - Debe ingresar un token como segundo argumento" )
    def getToken(self, jsf, token):
        try:
            with open(jsf, 'r') as (myfile):
                data = myfile.read()
                obj = json.loads(data)
                print (str(obj[token]))
        except: print("Error: No se ha podido recuperar la clave. Es posible que alguno de los argumentos sean invalidos. Ingrese -h para ayuda.")


gj1 = GetJason()
gj2 = GetJason()

try:
    if(sys.argv[1]):

        if(sys.argv[1] == "-h"):  
            gj1.getHelp()

        else:
            try:                
                if (sys.argv[2]):
                    gj1.getToken(sys.argv[1], sys.argv[2])
            except:
                print("Error: Segundo argumento inextistente. Ingrese -h para ayuda.")
except:
    print("Error: Pirmer argumento inexistente. Ingrese -h para ayuda.")