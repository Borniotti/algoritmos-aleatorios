# Solicitar a cotação do dólar
cotacao_dolar = float(input("Digite a cotação do dólar em reais (R$): "))

# Solicitar a quantidade de reais disponíveis
quantidade_reais = float(input("Digite a quantidade de reais disponíveis: "))

# Calcular o valor da conversão em dólares
valor_conversao = quantidade_reais / cotacao_dolar

# Armazenar o valor da conversão em uma variável
valor_conversao_em_dolar = valor_conversao

# Apresentar o valor da conversão
print("O valor da conversão em dólares é: US$", valor_conversao)
