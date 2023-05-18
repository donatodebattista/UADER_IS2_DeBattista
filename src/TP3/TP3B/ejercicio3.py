# Patron Composite

# La clase pieza corresponde al ultimo nivel de jerarquía (hojas)
class Pieza:

	def __init__(self, *args):
		self.position = args[0]


	def showDetails(self):
		print("\t", end ="")
		print(self.position)


# Representa a los objetos compuestos en cualquier nivel de jerarquía excepto el último(piezas -> hojas)
class Conjunto:

	def __init__(self, *args):

		self.position = args[0]
		self.children = []


	# Metodo para agregar hijos a los conjuntos creados
	def add(self, child):
		self.children.append(child)

	# Metodo para eliminar hijos de los conjuntos creados
	def remove(self, child):

		self.children.remove(child)

	# Muestra detalles incluyendo todos los niveles inferiores
	def showDetails(self):
		print(self.position)
		for child in self.children:
			print("\t", end ="")
			child.showDetails()


# Main
if __name__ == "__main__":

	# Primero se crea el producto principal (nivel mas alto de jerarquía -> Raíz)
	ensamblado = Conjunto("Ensamblado principal")

# -------------------SUBCONJUNTO 1--------------------------------

# Se crea el primer subconjunto de piezas
	subconjunto1 = Conjunto("Subconjunto1")

# Se crean 4 piezas para el subconjunto 1
	pieza1_sub1 = Pieza("pieza a del subconjunto 1")
	pieza2_sub1 = Pieza("pieza b del subconjunto 1")
	pieza3_sub1 = Pieza("pieza c del subconjunto 1")
	pieza4_sub1 = Pieza("pieza d del subconjunto 1")

# Se agregan las piezas creadas al subconjunto 1 (piezas (child) -> subconjunto1 (parent))
	subconjunto1.add(pieza1_sub1)
	subconjunto1.add(pieza2_sub1)
	subconjunto1.add(pieza3_sub1)
	subconjunto1.add(pieza4_sub1)

# -------------------SUBCONJUNTO 2--------------------------------

# Se repite el procedimiento del subconjunto 1
	subconjunto2 = Conjunto("Subconjunto2")

	pieza1_sub2 = Pieza("pieza a del subconjunto 2")
	pieza2_sub2 = Pieza("pieza b del subconjunto 2")
	pieza3_sub2 = Pieza("pieza c del subconjunto 2")
	pieza4_sub2 = Pieza("pieza d del subconjunto 2")

	subconjunto2.add(pieza1_sub2)
	subconjunto2.add(pieza2_sub2)
	subconjunto2.add(pieza3_sub2)
	subconjunto2.add(pieza4_sub2)


# -------------------SUBCONJUNTO 3--------------------------------

	subconjunto3 = Conjunto("Subconjunto3")

	pieza1_sub3 = Pieza("pieza a del subconjunto 3")
	pieza2_sub3 = Pieza("pieza b del subconjunto 3")
	pieza3_sub3 = Pieza("pieza c del subconjunto 3")
	pieza4_sub3 = Pieza("pieza d del subconjunto 3")

	subconjunto3.add(pieza1_sub3)
	subconjunto3.add(pieza2_sub3)
	subconjunto3.add(pieza3_sub3)
	subconjunto3.add(pieza4_sub3)

# -------------------SUBCONJUNTO opcional--------------------------------

	subconjunto_opcional = Conjunto("Subconjunto opcional")

	pieza1_opcional = Pieza("pieza a del subconjunto opcional")
	pieza2_opcional = Pieza("pieza b del subconjunto opcional")
	pieza3_opcional = Pieza("pieza c del subconjunto opcional")
	pieza4_opcional = Pieza("pieza d del subconjunto opcional")

	subconjunto_opcional.add(pieza1_opcional)
	subconjunto_opcional.add(pieza2_opcional)
	subconjunto_opcional.add(pieza3_opcional)
	subconjunto_opcional.add(pieza4_opcional)


# -------------------ENSAMBLADO FINAL--------------------------------

	# Se agregan al conjunto principal (raiz) los subconjuntos 1, 2 y 3.
	ensamblado.add(subconjunto1)
	ensamblado.add(subconjunto2)
	ensamblado.add(subconjunto3)

# Si el usuario lo requiere se agrega el subconjunto opcional
	o = input("desea incorporar el subconjunto opcional? (s/n) ")
	try:
		if (o == "s"):
			ensamblado.add(subconjunto_opcional)
		elif (o == "n"):
			print("El subconjunto opcional no se incluirá")
		else:
			raise ValueError("Caracter invalido")
	except ValueError as err:
		print(f"ERROR: {err}")


# Muestra toda la composicion del componente principal
	ensamblado.showDetails()

# Tambien se puede ver la jerarquia de un subconjunto ya que son objetos de la clase conjunto
#	subconjunto2.showDetails()

