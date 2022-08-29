#Calculo da hipotenusa de um triangulo retângulo
import math
cateto_adjacente = float(input('Digite o cateto adjacente desse triangulo: '))
cateto_oposto = float(input('Digite o cateto oposto desse triangulo: '))
print(f'A hipotenusa desse triangulo é {math.hypot(cateto_oposto, cateto_adjacente)}')
