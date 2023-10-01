import random
import os

print("============================================")
print("Bem vindo ao jogo de Pedra, Papel ou Tesoura")
print("============================================")

while True:
    voce = 0
    computador = 0

    def placar():
        print("\nPlacar:")
        print(f'Você: {voce}')
        print(f'Computador: {computador}')

    lista = ["pedra", "papel", "tesoura"]

    def pc():
        inimigo = random.randint(0, 2)
        return lista[inimigo]

    def jogador():
        print("Escolha o seu movimento:")
        print("0 - pedra | 1 - papel | 2 - tesoura")
        try:
            escolha = int(input())
            if escolha not in [0, 1, 2]:
                raise ValueError ("Escolha inválida")
            return lista[escolha]
        except Exception as e:
            print(e)

    def vitoria(voce, computador):
        if sua_escolha == "papel" and escolha_computador == "pedra":
            return "Você venceu!"
        elif sua_escolha == "tesoura" and escolha_computador == "papel":
            return "Você venceu!"
        elif sua_escolha == "pedra" and escolha_computador == "tesoura":
            return "Você venceu!"
        elif sua_escolha == escolha_computador:
            return "Empate!"
        else:
            return "Você perdeu!"
    
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        clear_screen ()
        sua_escolha = jogador()
        escolha_computador = pc()
        print(f'Você escolheu: {sua_escolha}')
        print(f'O computador escolheu: {escolha_computador}')

        resultado = vitoria(sua_escolha, escolha_computador)
        print(resultado)

        if resultado == "Você venceu!":
            voce += 1
        elif resultado == "Você perdeu!":
            computador += 1

        placar()

        print ("Deseja jogar novamente? (s/n)")
        jogar_novamente = input ().strip().lower()
        
        if jogar_novamente == "n":
            break