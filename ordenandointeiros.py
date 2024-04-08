# Lendo os 12 elementos numéricos inteiros
elementos = []
for i in range(12):
    elemento = int(input(f"Digite o {i+1}º elemento: "))
    elementos.append(elemento)

# Ordenando os elementos em ordem decrescente
elementos_ordenados = sorted(elementos, reverse=True)

# Apresentando os elementos ordenados
print("Elementos em ordem decrescente:")
for elemento in elementos_ordenados:
    print(elemento, end=" ")
