valor = int(input("entre com um número extenso: "))

ext = str(valor)

print("")
print("o seu numero possui",len(ext),"dígitos.")
print("")

i = 0

x = 0

while valor >= 1:
	i = (valor % 10)+i
	x = (valor // 10)
	valor = x

print ("a soma dos digitos do numero digitado é:",i)
