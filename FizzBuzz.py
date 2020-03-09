num = int(input("Digite um número: "))
resto1 = int(num) % 3 
resto2 = int(num) % 5

if resto1 ==0 and resto2 == 0:
	print("FizzBuzz")
else:
	print(num)
