#programa que lê o um angulo e mostre o valor de seu seno, cosseno e sua tangente
import math

angulo = int(input('Digite aqui o angulo a ser calculado: '))
print(f'Os respectivos valor para o angulo °{angulo} são, Seno = {math.sin(angulo)}, Cosseno = {math.cos(angulo)}, Tangente = {math.tan(angulo)}')