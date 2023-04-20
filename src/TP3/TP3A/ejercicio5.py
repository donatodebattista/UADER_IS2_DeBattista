import os

class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
	   
   def getPlane(self):
      plane = Plane()
      
      # Primero el body
      body = self.__builder.getBody()
      plane.setBody(body)
      
      # Luego las alas
      ala = self.__builder.getAla()
      plane.attachAla(ala)
      ala = self.__builder.getAla()
      plane.attachAla(ala)
      
      # Luego el tren de aterrizaje
      tren_de_aterrizaje = self.__builder.getTrenDeAterrizaje()
      plane.setTrenDeAterrizaje(tren_de_aterrizaje)
      
      # Por último las turbinas
      turbina = self.__builder.getTurbina()
      plane.attachTurbina(turbina)
      turbina = self.__builder.getTurbina()
      plane.attachTurbina(turbina)

      # Retorna el avión completo
      return plane

#*----------------------------------------------------------------
#* Esta es la definición de un objeto avión inicializando 
#* todos sus atributos
#*----------------------------------------------------------------
class Plane:
   def __init__(self):
      self.__alas = []
      self.__turbinas = []
      self.__body = None
      self.__tren_de_terrizaje = None

   def setBody(self, body):
      self.__body = body

   def attachAla(self, ala):
      self.__alas.append(ala)

   def attachTurbina(self, turbina):
      self.__turbinas.append(turbina)

   def setTrenDeAterrizaje(self, tren_aterrizaje):
      self.__tren_de_terrizaje = tren_aterrizaje

   def specification(self):
      print (f"Cuerpo: {self.__body.metros_de_largo}")
   
      print (f"Alas: {self.__alas[0].metros_de_largo}")
      print (f"Alas: {self.__alas[1].metros_de_largo}")

      print (f"Tren de Aterrizaje: {self.__tren_de_terrizaje.altura}")
   
      print (f"Turbinas: {self.__turbinas[0].horsePower}")
      print (f"Turbinas: {self.__turbinas[1].horsePower}")



class Builder:
	
      def getBody(self): pass
      def getAla(self): pass
      def getTrenDeAterrizaje(self): pass
      def getTurbina(self):pass



# Un Builder para un avion boeing747 concreto
class Boeing747Builder(Builder):
   
   def getAla(self):
      ala = Ala()
      ala.metros_de_largo = 30
      return ala
   
   def getTurbina(self):
      turbina = Turbina()
      turbina.horsePower = 100000
      return turbina
   
   def getBody(self):
      body = Body()
      body.metros_de_largo = 76
      return body

   def getTrenDeAterrizaje(self):
      tren_de_aterrizaje = TrenAterrizaje()
      tren_de_aterrizaje.altura = 4
      return tren_de_aterrizaje



# Define partes genéricas para un avión (sin inicializar)
class Ala:
   metros_de_largo = None

class Turbina:
   horsePower = None

class Body:
   metros_de_largo = None

class TrenAterrizaje:
   altura = None




def main():

   BuilderBoeing747 = Boeing747Builder() 
   director = Director()


   # El builder que le seteamos al director es el que creamos especificamente
   # para un boeing747 
   director.setBuilder(BuilderBoeing747)


   # El director seguira los pasos para crear el avion
   # nos retorna un objeto Plane de acuerdo al builder especifico que le seteamos al director
   boeing747 = director.getPlane()

#*---------------------------------------------------------------
#* Finalizada la construcción verifica que sea completa
#*---------------------------------------------------------------
   print("Especificaciones de avión boeing-747:" )
   boeing747.specification()
   print ("\n\n")


if __name__ == "__main__":
   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avión\n")
   main()
