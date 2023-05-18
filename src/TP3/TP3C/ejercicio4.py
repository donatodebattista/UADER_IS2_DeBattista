import os
#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state
#*--------------------------------------------------------------------
"""State class: Base State class"""
class State:

	def scan(self):
		self.pos += 1
		if self.pos == len(self.stations):
			self.pos = 0
		print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

	def scan_memorias(self):
		self.pos_memorias += 1
		if self.pos_memorias == len(self.memorias):
			self.pos_memorias = 0
		print("Sintonizando... estación memorizada {} {}".format(self.memorias[self.pos_memorias], self.name))
#*------- Implementa como barrer las estaciones de AM
class AmState(State):

	def __init__(self, radio):
		
		self.radio = radio
		self.stations = ["1250", "1380", "1510"]
		self.pos = -1
		self.name = "AM"
		self.pos_memorias = -1
		self.memorias = ["M1", "M4"]

	def toggle_amfm(self):
		print("Cambiando a FM")
		self.radio.state = self.radio.fmstate

#*------- Implementa como barrer las estaciones de FM
"""Separate class for FM state"""
class FmState(State):

	def __init__(self, radio):

		self.radio = radio
		self.stations = ["81.3", "89.1", "103.9"]
		self.pos = -1
		self.name = "FM"
		self.pos_memorias = -1
		self.memorias = ["M2", "M3"]


	def toggle_amfm(self):
		print("Cambiando a AM")
		self.radio.state = self.radio.amstate

#*--------- Construye la radio con todas sus formas de sintonía
class Radio:


	def __init__(self):
		
		self.fmstate = FmState(self)
		self.amstate = AmState(self)

#*--- Inicialmente en FM

		self.state = self.fmstate

	def toggle_amfm(self):
		self.state.toggle_amfm()

	def scan(self):
		self.state.scan()

	def scan_memorias(self):
		self.state.scan_memorias()
#*---------------------

if __name__ == "__main__":
	os.system("clear")
	print("\nCrea un objeto radio y almacena las siguientes acciones")
	radio = Radio()
	# En cada barrido realiza 3 scan sintonizando radios AM o FM, luego cambia de frecuencia, realiza nuevamente 3 scan en la frecuencia a la
	# que se acaba de cambiar, luego hace 2 scan sintonizando las mamorias, luego cambia de frecuencia y finalmente realiza 2 scan mas en
	# memorias pero de la frecuencia que se acaba de cambiar. 
	actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3 + [radio.scan_memorias] * 2 + [radio.toggle_amfm] + [radio.scan_memorias] * 2
	actions *= 2

#*---- Recorre las acciones ejecutando la acción

	print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
	for action in actions:
		action()

