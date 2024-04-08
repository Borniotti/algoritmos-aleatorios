# Leitura da quantidade de votos válidos para cada candidato
votos_validos_candidato_a = int(input("Digite a quantidade de votos válidos para o candidato A: "))
votos_validos_candidato_b = int(input("Digite a quantidade de votos válidos para o candidato B: "))
votos_validos_candidato_c = int(input("Digite a quantidade de votos válidos para o candidato C: "))

# Leitura da quantidade de votos nulos e em branco
votos_nulos = int(input("Digite a quantidade de votos nulos: "))
votos_branco = int(input("Digite a quantidade de votos em branco: "))

# Cálculo do número total de eleitores
total_eleitores = votos_validos_candidato_a + votos_validos_candidato_b + votos_validos_candidato_c + votos_nulos + votos_branco

# Cálculo do percentual de votos válidos em relação ao total de eleitores
percentual_votos_validos = ((votos_validos_candidato_a + votos_validos_candidato_b + votos_validos_candidato_c) / total_eleitores) * 100

# Cálculo dos percentuais de votos válidos para cada candidato em relação ao total de eleitores
percentual_candidato_a = (votos_validos_candidato_a / total_eleitores) * 100
percentual_candidato_b = (votos_validos_candidato_b / total_eleitores) * 100
percentual_candidato_c = (votos_validos_candidato_c / total_eleitores) * 100

# Cálculo dos percentuais de votos nulos e em branco em relação ao total de eleitores
percentual_votos_nulos = (votos_nulos / total_eleitores) * 100
percentual_votos_branco = (votos_branco / total_eleitores) * 100

# Apresentação dos resultados
print("Número total de eleitores:", total_eleitores)
print("Percentual de votos válidos em relação ao total de eleitores:", percentual_votos_validos, "%")
print("Percentual de votos válidos para o candidato A:", percentual_candidato_a, "%")
print("Percentual de votos válidos para o candidato B:", percentual_candidato_b, "%")
print("Percentual de votos válidos para o candidato C:", percentual_candidato_c, "%")
print("Percentual de votos nulos em relação ao total de eleitores:", percentual_votos_nulos, "%")
print("Percentual de votos em branco em relação ao total de eleitores:", percentual_votos_branco, "%")
