n = int(input("Digite um número inteiro: "))

i = 0

primo = 0

while i < n:
	i = i + 1
	if n % i == 0:
		primo = primo + 1
if primo == 2:
	print("primo")
else:
	print("não primo")
