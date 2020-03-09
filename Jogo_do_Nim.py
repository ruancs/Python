def computador_escolhe_jogada(n,m):
	if n <= m:
		return n
	else:
		y = n % (m+1)
		
		if y > 0:
			return y
		else:
			return m
			




def usuario_escolhe_jogada(n,m):
	x = 0
	while x == 0:
		x = int(input("Quantas peças você vai tirar?"))
		if x > m or x == 0:
			print("Opção inválida\n")
			x = 0
		else:
			return x
		
		
	
	


# partida -----------------------------------------------------------

def partida():

	n=int(input("Quantas peças?"))
	m= int(input("Limite de peças por jogada?"))
	
	if n %(m+1) == 0:
		vezPlayer = True
		print("Você começa!")
		valor = usuario_escolhe_jogada(n,m)
		print("\nVocê retirou",valor,"peças")
		n = n - valor
		print("Agora restam",n,"peças no tabuleiro\n")
		vezPlayer = False
		vezPC = True
		
		
	else:
		vezPC = True
		print("Computador começa!")		
		valor = computador_escolhe_jogada(n,m)
		print("O Computador retirou",valor,"peças")
		n = n - valor
		print("Agora restam",n,"peças no tabuleiro\n")
		vezPC = False
		vezPlayer = True
	
	while n > 0:

		if vezPlayer == True:
			valor = usuario_escolhe_jogada(n,m)
			vezPlayer = False
			print("\nVocê retirou",valor,"peças")
			n = n - valor
			print("Agora restam",n,"peças no tabuleiro\n")
			vezPC = True
		else:
			if vezPC == True:
				valor = computador_escolhe_jogada(n,m)
				vezPC = False
				print("O Computador retirou",valor,"peças")
				n = n - valor
				print("Agora restam",n,"peças no tabuleiro\n")
				vezPlayer = True


	if vezPC == True:

		print("Fim de jogo! Você ganhou!")
		return 1
	else:
		print("Fim de jogo! O computador ganhou!")
		return 0	
				
				
# /partida-------------------------------------------------------------------

# campeonato-----------------------------------------------------------------

def campeonato():
	
	player = 0
	pc = 0
	
	for i in range(3):
		print("\n**** Rodada",(i+1),"****\n")
		ganhou = partida()
		
		if ganhou == 1:

			player = player + 1

		else:

			pc = pc + 1
	
	print("\n**** Final do Campeonato! ****\n")
	print("Placar: Você",player,"X",pc,"Computador")


#menu-selecao -------------------------------------------------------------

vezPc = False
vezPlayer = False
tipo = 0
valor = 0
while tipo == 0:
	print("Bem vindo ao jogo do NIM! Escolha:\n")
	print("1 para jogar uma partida isolada")
	print("2 para jogar um campeonato")
	tipo = int(input("->"))

	if tipo == 1:
		print("\nVocê escolheu partida isolada!")
		print("******************************")
		partida()	
		
	else:
		if tipo == 2:
			print("Você escolheu campeonato!\n")
			campeonato()
			
		else:
			print("Opção inválida!\n")
						
			tipo = 0

# /menu-selecao-----------------------------------------------------------------

			
	

