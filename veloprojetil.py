# Ler a distância em quilômetros
distancia_km = float(input("Digite a distância percorrida pelo projétil (em quilômetros): "))

# Ler o tempo em minutos
tempo_min = float(input("Digite o tempo decorrido (em minutos): "))

# Converter o tempo de minutos para horas
tempo_horas = tempo_min / 60

# Calcular a velocidade em metros por segundo
velocidade_ms = (distancia_km * 1000) / (tempo_horas * 60)

# Apresentar o resultado
print("A velocidade do projétil é de", velocidade_ms, "metros por segundo.")
