def jokenpo(jogador1, jogador2):
    regras = {
        'TesouraPapel': 'Tesoura corta Papel',
        'PapelPedra': 'Papel cobre Pedra',
        'PedraLagarto': 'Pedra esmaga Lagarto',
        'LagartoSpock': 'Lagarto envenena Spock',
        'SpockTesoura': 'Spock esmaga Tesoura',
        'TesouraLagarto': 'Tesoura decapita Lagarto',
        'LagartoPapel': 'Lagarto come Papel',
        'PapelSpock': 'Papel refuta Spock',
        'SpockPedra': 'Spock vaporiza Pedra',
        'PedraTesoura': 'Pedra amassa Tesoura'
    }
    
    if jogador1 == jogador2:
        return "Empate"
    elif jogador1 + jogador2 in regras:
        return "Jogador 1 vence: " + regras[jogador1 + jogador2]
    else:
        return "Jogador 2 vence: " + regras[jogador2 + jogador1]

# Ler as jogadas dos jogadores
jogador1 = input("Jogador 1, escolha entre Pedra, Papel, Tesoura, Lagarto ou Spock: ").capitalize()
jogador2 = input("Jogador 2, escolha entre Pedra, Papel, Tesoura, Lagarto ou Spock: ").capitalize()

# Verificar e imprimir o resultado
resultado = jokenpo(jogador1, jogador2)
print("Resultado:", resultado)
