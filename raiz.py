import math

a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))

delta = b **2 - 4 * a * c

if delta == 0:
	raiz1 = (-b+ math.sqrt(delta)) / (2 * a)
	print("a raiz desta equação é: ", raiz1)
else:
	if delta < 0:
		print(" Esta equação não possui raízes reais")
	else:
		raiz1 = (-b+ math.sqrt(delta)) / (2 * a)
		raiz2 = (-b- math.sqrt(delta)) / (2 * a)

		if (raiz1)>(raiz2):

			print("As raízes da equação são",raiz2,"e",raiz1)
		else:
			print("As raízes da equação são",raiz1,"e",raiz2)



