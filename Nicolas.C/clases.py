palabra=input("Ingrese una cadena de carateres: ")
print("Presione la tecla A para que imprima los dos primeros caracteres")
print("Presione la tecla B para que imprima los dos ultimos caracteres")
print("Presione la tecla C para que imprima cada dos caracteres")
print("Presione la tecla D para que imprima la cadena de caracteres al inversa")
print("Presione cualquier tecla Fpara que imprima la cadena en un sentido y en sentido inverso")
opcion=input("Ingrese una opcion: ")
if opcion=="A"||opcion=="a":
	print(palabra[:2])
	else if opcion=="B"||opcion=="b" :
		print(palabra[-2])
		else if opcion=="C"||opcion=="c"
			print(palabra[::2])
			else if opcion=="D"||opcion=="d"
				print(palabra[-1])
					else
						print(palabra[::],palabra[-1])
