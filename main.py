def calcular_novo_salario(salario_atual, percentual_reajuste):
    reajuste = salario_atual + (percentual_reajuste / 100)

    novo_salario = salario_atual + reajuste

    return novo_salario

salario_atual = float(input("digite o valor do salario atual: R$ "))
percentual_reajuste = float(input("digite o percentual de reajuste (%): "))

novo_salario = calcular_novo_salario(salario_atual, percentual_reajuste)

print(f"o novo salario após o reajuste de {percentual_reajuste}% é: R$ {novo_salario: 2f}")