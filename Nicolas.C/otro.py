numero=int(input("Ingrese un numero: "))
a=0
for i in range(1,numero+1):
    numero=int((i*(i+1))/2)
    print(i,"-",numero)