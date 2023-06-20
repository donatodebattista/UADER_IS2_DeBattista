# uncompyle6 version 3.5.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.5 (default, Nov 16 2020, 22:23:17) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)]
# Embedded file name: getJason.py
# Compiled at: 2022-06-15 03:15:55
import json, sys

try:
    if(sys.argv[1]):

        #Si el argumento 1 es -h mostrara un mensaje de ayuda 
        if(sys.argv[1] == "-h"):  
            print("mensaje de ayuda: \n - Debe ingresar el archivo json como primer argumento\n - Debe ingresar un token como segundo argumento" )
        
        else:
            try:                
                if (sys.argv[2]):
                    
                    jsonfile = sys.argv[1]
                    jsonkey = sys.argv[2]
                    try:
                        with open(jsonfile, 'r') as (myfile):
                            data = myfile.read()
                        obj = json.loads(data)
                        print (str(obj[jsonkey]))
                    except: print("Error: No se ha podido recuperar la clave. Es posible que alguno de los argumentos sean invalidos. Ingrese -h para ayuda.")
            except:
                print("Error: Segundo argumento inexistente. Ingrese -h para ayuda.")
except:
        print("Error: Pirmer argumento inexistente. Ingrese -h para ayuda.")





""" 
!-----Programa antiguo------!    

jsonfile = sys.argv[1]
jsonkey = 
with open(jsonfile, 'r') as (myfile):
    data = myfile.read()
obj = json.loads(data)
print str(obj[jsonkey]) """