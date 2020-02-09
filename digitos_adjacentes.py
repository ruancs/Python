num = int(input("Digite um número inteiro: "))

i = 0

x = 0

j = 1

y = 0

while num >=1:
	i = (num % 10)
	if (j == i):
		y = y + 1
		x = (num // 10)
		num = x
		j = i

	else:
		x = (num // 10)
		num = x
		j = i

if y >= 1:
	print("sim")
else: 
	print("não")

