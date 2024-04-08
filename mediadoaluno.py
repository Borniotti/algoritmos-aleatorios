# Ler as quatro notas bimestrais
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Calcular a média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Verificar se o aluno foi aprovado ou reprovado
if media >= 5:
    print("Aprovado")
else:
    print("Reprovado")

# Apresentar o valor da média
print("Média obtida pelo aluno:", media)
