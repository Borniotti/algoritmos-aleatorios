# Estabelecer a leitura das horas trabalhadas no mês
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Estabelecer a leitura do valor da hora aula
valor_hora_aula = float(input("Digite o valor da hora aula: "))

# Estabelecer a leitura do percentual de desconto do INSS
percentual_desconto = float(input("Digite o percentual de desconto do INSS (%): "))

# Calcular o salário bruto
salario_bruto = horas_trabalhadas * valor_hora_aula

# Calcular o valor total do desconto com base no percentual de desconto do INSS
desconto = (percentual_desconto / 100) * salario_bruto

# Calcular o salário líquido, deduzindo o desconto do salário bruto
salario_liquido = salario_bruto - desconto

# Apresentar os valores do salário bruto e líquido
print("Salário Bruto: R$", salario_bruto)
print("Salário Líquido: R$", salario_liquido)
