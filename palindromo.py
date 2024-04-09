def verifica_palindromo(texto):
    # Remover espaços em branco e transformar tudo em minúsculas
    texto = texto.replace(" ", "").lower()
    # Verificar se o texto é igual ao seu reverso
    if texto == texto[::-1]:
        return True
    else:
        return False

# Função para formatar a saída
def formatar_saida(palavra, resultado):
    if resultado:
        print(f"A palavra/frase/número '{palavra}' é um palíndromo.")
    else:
        print(f"A palavra/frase/número '{palavra}' não é um palíndromo.")

# Ler a entrada do usuário
entrada = input("Digite uma palavra, frase ou número: ")

# Verificar se a entrada é um palíndromo
resultado = verifica_palindromo(entrada)

# Apresentar o resultado
formatar_saida(entrada, resultado)