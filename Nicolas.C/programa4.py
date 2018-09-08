from math import sqrt
"QRT= Calcula la potencia de 2"
catetoA=float(input("Ingrese el cateto del triangulo: "))
catetoB=float(input("Ingrese el otro cateto: "))
hipotenusa=sqrt((catetoA**2)+(catetoB**2))
print("La hipotenusa del triangulo es "+str(hipotenusa))
