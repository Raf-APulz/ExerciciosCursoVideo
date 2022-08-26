altura = float(input('Qual é a altura da sua parede: '))
largura = float(input('Qual é a largura da sua parede da sua parede: '))
area = altura*largura
q_tinta = area/2
print('Para você pintar a area dá parede que é de {}M², será necessarios {}L de tinta' .format(area, q_tinta))