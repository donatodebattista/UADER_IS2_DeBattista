# Patron decorator

# Clase original
class Numero_original:

	def __init__(self, valor):
		self._valor = valor

	def render(self):
		return self._valor



# Decorator A (suma)
class Adicion_2(Numero_original):

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return self._wrapped.render() + 2

# Decorator B (multiplicacion)
class Multiplicacion_2(Numero_original):

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return self._wrapped.render() * 2

# Decorator C (Division)
class Division_3(Numero_original):

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return self._wrapped.render() / 3


# Main
if __name__ == '__main__':

    numero_original = Numero_original(43)
    numero_sumado = Adicion_2(numero_original)
    numero_multiplicado = Multiplicacion_2(numero_original)
    numero_dividido = Division_3(numero_original)

    
    print(numero_original.render())
    

    # Decoraciones anidadas
    numero_completamente_decorado = Division_3(Multiplicacion_2(Adicion_2(numero_original)))


    print(numero_completamente_decorado.render())
    
