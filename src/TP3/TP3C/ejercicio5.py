
import os
#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo

#*-------------------------------------------------------------------
class Memento:
	def __init__(self, file, content):
		self.file = file
		self.content = content


class FileWriterUtility:

	def __init__(self, file):

		self.file = file
		self.content = ""
		# Se almacenará la version actual y 4 estados en el pasado 
		self.versions = [None, None, None, None, None]

	def write(self, string):
		self.content += string


	def save(self):
		""" Este metodo añade objetos de la clase memento al array versions """

		# Siempre se elimina el de la posicion 0 y se van agregando nuevas versiones al final
		self.versions.pop(0)
		self.versions.append(Memento(self.file, self.content))


		# Modo de guardado de versiones
		"""
		None | None | None | None | None    => inicio
		None | None | None | None | 0    	=> Se agrega una version (0)
		None | None | None | 0    | 1    	=> Se agrega una version (1)
		None | None | 0    | 1    | 2    	=> Se agrega una version (2)
		None | 0    | 1    | 2    | 3    	=> Se agrega una version (3)
		0    | 1    | 2    | 3    | 4    	=> Se agrega una version (4)
		1    | 2    | 3    | 4    | 5    	=> Se agrega una version (5). La version 0 se elimina ya que
																		  solo se guardan las 4 previas
		"""

	def undo(self, version):
		v = self.versions[len(self.versions)-2-version]
		if (v is not None):
			self.file = v.file
			self.content = v.content
		
		# Esto sucederia cuando se quiere recuperar una version determinada que no existe
		# Por ejemplo que de un archivo solo exista una version previa (solo 1 save) y se quiera  
		# retroceder 3 versiones. 
		else: 
			print("Version inexistente")


class FileWriterCaretaker:

	def save(self, writer):
		self.obj = writer.save()

	def undo(self, writer, version):
		# El parametro ingresado debe estar entre 0 y 3 ambos incluidos
		if(version <= 3 and version >= 0):
			writer.undo(version)
		else:
			print("No es posible accdeder a esta version (máximo almacena 4 versionesn anteriores)")
		


if __name__ == '__main__':

	os.system("clear")
	# Objeto cuyo estado se quiere preservar
	writer = FileWriterUtility("GFG.txt")
	#Objeto que gestiona la version anterior
	caretaker = FileWriterCaretaker()


	writer.write("(0)\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	writer.write("(1)\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	writer.write("(2)\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	writer.write("(3)\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	writer.write("(4)\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	writer.write("(5)\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	writer.write("(6)\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)



	print("se invoca al <undo> con parametro 0 para mostrar el inmediato anterior")
	caretaker.undo(writer, 0)
	print("Se muestra el estado actual")
	print(writer.content + "\n\n")

	print("se invoca al <undo> con parametro 3 para mostrar la 4ta version anterior")
	caretaker.undo(writer, 3)
	print("Se muestra el estado actual")
	print(writer.content + "\n\n")

	print("Se intenta recuperar un estado previo al 4to")
	caretaker.undo(writer, 5)

	print("Se muestra el estado actual")
	print(writer.content + "\n\n")
