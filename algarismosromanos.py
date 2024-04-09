def roman_to_integer(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    inteiro = 0
    i = 0
    
    while i < len(romano):
        # Se o valor do próximo caractere é maior que o atual, subtrai o valor atual
        if i+1 < len(romano) and valores[romano[i]] < valores[romano[i+1]]:
            inteiro += valores[romano[i+1]] - valores[romano[i]]
            i += 2
        else:
            inteiro += valores[romano[i]]
            i += 1
    
    return inteiro

# Ler o número romano do usuário
numero_romano = input("Digite um número romano: ")

# Converter e imprimir o número inteiro correspondente
numero_inteiro = roman_to_integer(numero_romano.upper())
print("O número inteiro correspondente é:", numero_inteiro)
