def crear_personaje(nombre="Jugador",ataque=10,salud=10):
	personaje={
		"nombre":nombre,
		"ataque":ataque,
		"salud":salud
	}
	return personaje

def atacar(atacante,atacado):
	recibir_ataque(atacado,atacante["ataque"])

def recibir_ataque(personaje,ataque):
	personaje["salud"]-=ataque

def probar():
	p1=crear_personaje(nombre="Pocho",ataque=100,salud=2000)
	p2=crear_personaje(nombre="IronaMan",salud=1000)
	print(p2)
	atacar(p1,p2)
	print(p2)

def jugar():
	p1=crear_personaje(nombre="Pocho",ataque=100,salud=2000)
	p2=crear_personaje(nombre="IronaMan",salud=1000)
	turno=True
	jugadores=(p1,p2)
	while p1["salud"]>0 and p2["salud"]>0:
		atacante=jugadores[int(turno)]
		atacado=jugadores[int(not turno)]
		atacar(atacante,atacado)
		print(p1)
		print(p2)
		turno=not turno
	print ("Ganador {nombre} ({salud})".format(
		nombre=atacante["nombre"],
		salud=atacante["salud"]
		))

if __name__=="__main__":
	jugar()