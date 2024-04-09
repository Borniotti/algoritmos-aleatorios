def jokenpo(jogador1, jogador2):
    if jogador1 == jogador2:
        return "Empate"
    elif (jogador1 == "Pedra" and jogador2 == "Tesoura") or \
         (jogador1 == "Tesoura" and jogador2 == "Papel") or \
         (jogador1 == "Papel" and jogador2 == "Pedra"):
        return "Jogador 1 vence"
    else:
        return "Jogador 2 vence"

# Ler as jogadas dos jogadores
jogador1 = input("Jogador 1, escolha Pedra, Papel ou Tesoura: ").capitalize()
jogador2 = input("Jogador 2, escolha Pedra, Papel ou Tesoura: ").capitalize()

# Verificar e imprimir o resultado
resultado = jokenpo(jogador1, jogador2)
print("Resultado:", resultado)
