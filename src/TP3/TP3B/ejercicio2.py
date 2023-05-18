# Patron Bridge
class laminadora_5mts:

	def fabricar_lamina(self, espesor, ancho):

		print("laminadora de 5 metros comienza a fabricar lámina")
		print(f"Especificaciones: \n -espesor: {espesor} \n -ancho: {ancho}")

class laminadora_10mts:

	def fabricar_lamina(self, espesor, ancho):

		print("laminadora de 10 metros comienza a fabricar lámina")
		print(f"Especificaciones: \n -espesor: {espesor} \n -ancho: {ancho}")


class Lamina:

	def __init__(self, espesor, ancho, producingAPI):

		self._espesor = espesor
		self._ancho = ancho
		
        #Atributo que indica que tipo de implementación se va a utilizar
		self._producingAPI = producingAPI


	def produce(self):
        # Llamamos al metodo fabricar_lamina del objeto creado correspondiente a la clase
        # de implementación especificada
		self._producingAPI.fabricar_lamina(self._espesor, self._ancho)


# Main
lamina1 = Lamina(0.5, 1.5, laminadora_5mts())
lamina1.produce()

lamina2 = Lamina(0.5, 1.5, laminadora_10mts())
lamina2.produce()