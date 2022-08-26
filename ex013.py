salario_atual = float(input('digite seu salario atual: '))
porc_aumento = int(input('Digite sua porcentagem de aumento: '))
conversao = salario_atual*porc_aumento/100
salario_novo = salario_atual + conversao
print(f'devido a um aumento de {porc_aumento}% em seu salário, seu salário atual é de R${salario_novo}')
