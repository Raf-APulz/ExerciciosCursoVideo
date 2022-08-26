preço = float(input('===Caculador de Desconto \n Qual é o preço do produto: '))
desconto = int(input('Qual é porcentagem de desconto do produto: '))
conversão = preço*desconto/100
novo_preço = preço - conversão
print(f'De acordo com o desconto de {desconto}% aplicado, o valor atual do produto é de R${novo_preço}, contudo você economizou R${conversão}')