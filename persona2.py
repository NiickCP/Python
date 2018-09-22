class Personaje:
	__nombre=None
	__salud=None
	__ataque=None

	def __init__(self,nombre="Personaje",salud=1000,ataque=100):
		self.__nombre=nombre
		self.__ataque=ataque
		self.__salud=salud
		
	def recibir_ataque(self,ataque):
		self.__salud-=ataque

	def __generar_ataque(self):
		return randint(0,self.__ataque)

	def atacar(self,enemigo):
		ataque=self.__generar_ataque()
		enemigo.recibir_ataque(ataque)
		
	@property		""decorator""
	def salud(self):
		return self.__salud

	def __str__(self)""Para poder ver mas que la direccion de donde esta el personaje""
		plantilla="{nombre} salud={salud} ataque={ataque}"
		return plantilla.format(
			nombre=self.__nombre,
			salud=self.__salud,
			ataque=self.__ataque
			)
