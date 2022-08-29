#Um professor quer sortear ebtre seus 4 alunos para apagar a lousa, faça um programa que leia isso
import random
nome1 = str(input('escreva o nome do aluno: '))
nome2 = str(input('escreva o nome do aluno: '))
nome3 = str(input('escreva o nome do aluno: '))
nome4 = str(input('escreva o nome do aluno: '))
print(f'O aluno que foi o azarado é o/a {random.choice(nome1, nome2, nome3, nome4)}')
