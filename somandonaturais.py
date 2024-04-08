# Definindo o intervalo de números naturais (de 1 a 100)
inicio_intervalo = 1
fim_intervalo = 100

# Inicializando a variável de soma
soma = 0

# Imprimindo o intervalo informado
print("Intervalo informado:", inicio_intervalo, "a", fim_intervalo)

# Calculando a soma dos números no intervalo
for num in range(inicio_intervalo, fim_intervalo + 1):
    soma += num

# Imprimindo o resultado da soma
print("A soma dos números no intervalo é:", soma)
