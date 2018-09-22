from persona2 import Personaje
from random import randint
def crear_personaje():
    cp1=Personaje("Policia",100,10)
    cp2=Personaje("MotoChorro",145,30)
    personaje=(cp1,cp2)
    return personaje

def serializar_personaje(personaje):
    formato = "{nombre} (salud: {salud} / ataque: {ataque})"

    return formato.format(**personaje)

def jugar():
    p1 = crear_personaje(nombre='El hijo de Cuca', ataque=10, salud=5000)
    p2 = crear_personaje('IronMan', ataque=100, salud=500)
    personajes = p1, p2

    print("{personaje1} vs. {personaje2})".format(
        personaje1=serializar_personaje(p1),
        personaje2=serializar_personaje(p2)
    ))

    turno = True
    while personajes[0]['salud'] > 0 and personajes[1]['salud'] > 0:
        atacante = personajes[int(turno)]
        atacado = personajes[int(not turno)]
        atacar(atacante, atacado)
        print("{p1}: {salud1} | {p2}: {salud2}".format(
            p1=personajes[0]['nombre'], salud1=personajes[0]['salud'],
            p2=personajes[1]['nombre'], salud2=personajes[1]['salud']
        ))
        turno = not turno

    print('El ganador es {}'.format(atacante['nombre']))


def probar():
    p1 = crear_personaje(nombre='El hijo de Cuca', ataque=100, salud=2000)
    p2 = crear_personaje('IronMan', ataque=500, salud=500)
    print(p2)
    atacar(p1, p2)
    print(p2)


if __name__ == '__main__':
    jugar()