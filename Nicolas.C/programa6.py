from math import factorial
i=0
respuesta=0
array=[i]
while respuesta!=1:
	numero=int(input("Ingrese un numero: "))
	array[i]=numero
	respuesta=input("SI usteed quiere seguir ingresando numeros ingrese el numero 1 : ")
	i=i+1
for a in range(1,i):
	prod=1
		for c in range(1,array[a]+1)
		prod=prod*c
		return prod
	print("El factorial de ",str(array[a])," es ",str(prod))
	