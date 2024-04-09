def calcular_score(palavra):
    # Definir pontuações das letras
    pontuacoes = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
        'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
        'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
        'y': 4, 'z': 10
    }
    
    # Converter a palavra para minúsculas e remover espaços vazios
    palavra = palavra.lower().replace(" ", "")
    
    # Calcular o score
    score = 0
    for letra in palavra:
        if letra in pontuacoes:
            score += pontuacoes[letra]
    
    return score

# Ler a palavra do usuário
palavra = input("Digite uma palavra: ")

# Calcular e imprimir o score
score = calcular_score(palavra)
print("O score da palavra é:", score)
