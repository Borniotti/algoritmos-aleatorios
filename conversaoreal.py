# Solicitar a cotação do dólar
cotacao_dolar = float(input("Digite a cotação do dólar em reais (R$): "))

# Solicitar a quantidade de dólares disponíveis
quantidade_dolares = float(input("Digite a quantidade de dólares disponíveis: "))

# Calcular o valor da conversão em reais
valor_conversao = cotacao_dolar * quantidade_dolares

# Apresentar o valor da conversão
print("O valor da conversão em reais é: R$", valor_conversao)