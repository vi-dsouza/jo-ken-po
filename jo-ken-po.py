import random

def menu():
    print("\n-----------------JO KEN PÔ----------------\n")
    print("|1- PEDRA |2- PAPEL |3- TESOURA |4- SAIR |\n")
    return int(input("Faça sua escolha: "))

def placar(count_jogador, count_maquina, count_empate):
    print("\n------------------PLACAR-------------------")
    print(f"| JOGADOR: {count_jogador}  | MÁQUINA: {count_maquina}  | EMPATES: {count_empate}  |")
    print("|_________________________________________|")

def escolhas(escolha_jogador, escolha_maquina):
    if escolha_jogador == 1:
        print("\nJogador: PEDRA")
        print("Máquina: ", escolha_maquina)
    elif escolha_jogador == 2:
        print("\nJogador: PAPEL")
        print("Máquina: ", escolha_maquina)
    elif escolha_jogador == 3: 
        print("\nJogador: TESOURA")
        print("Máquina: ", escolha_maquina)

def rodada(escolha_jogador, count_jogador, count_maquina, count_empate):
    
    maquina = ["PEDRA", "PAPEL", "TESOURA"]
    escolha_maquina = random.choice(maquina)
    escolhas_dos_jogadores = escolhas(escolha_jogador, escolha_maquina)
    
    if escolha_jogador == 1 and escolha_maquina == "PEDRA" or escolha_jogador == 2 and escolha_maquina == "PAPEL" or escolha_jogador == 3 and escolha_maquina == "TESOURA":
        print("\n>> Empate >>")
        count_empate += 1
        
    if escolha_jogador == 1 and escolha_maquina == "TESOURA":
        print("\n>> Jogador ganhou >>")
        count_jogador += 1
        
    elif escolha_jogador == 1 and escolha_maquina == "PAPEL":
        print("\n >> Máquina ganhou >>")
        count_maquina += 1
        
    elif escolha_jogador == 2 and escolha_maquina == "PEDRA":
        print("\n>> Jogador ganhou >>")
        count_jogador += 1
      
    elif escolha_jogador == 2 and escolha_maquina == "TESOURA":
        print("\n>> Máquina ganhou >>")
        count_maquina += 1
        
    elif escolha_jogador == 3 and escolha_maquina == "PEDRA":
        print("\n>> Máquina ganhou >>")
        count_maquina += 1
       
    elif escolha_jogador == 3 and escolha_maquina == "PAPEL":
        print("\n>> Jogador ganhou >>")
        count_jogador += 1
    return count_jogador, count_maquina, count_empate

count_jogador = 0
count_maquina = 0 
count_empate = 0

while True:
    escolha_jogador = menu()
    
    if escolha_jogador == 4:
        print("Saindo...")
        break

    count_jogador, count_maquina, count_empate = rodada(escolha_jogador, count_jogador, count_maquina, count_empate)
    placar_jogo = placar(count_jogador, count_maquina, count_empate)

    



