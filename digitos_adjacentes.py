num = int(input("Digite um número inteiro: "))

i = ("0")

x = 0

j = ("0")

y = 0

adj = False

while num >=1 or (adj == True):
	i = (num % 10)
	if (j == i):
		adj = True
		y = y + 1			
		x = (num // 10)
		num = x
		j = i
	
	else:
		adj = False
		x = (num // 10)
		num = x
		j = i

if y >= 1:
	print("sim")
else: 
	print("não")

