import random
nome_1 = input("Digite o nome do primeiro aluno: ")
nome_2 = input("Digite o nome do segundo aluno: ")
nome_3 = input("Digite o nome do terceiro aluno: ")
nome_4 = input("Digite o nome do quarto aluno: ")
lista_alunos = [nome_1, nome_2, nome_3, nome_4]
aluno_escolhido = random.choice(lista_alunos)
print("O aluno escolhido é: {}".format(aluno_escolhido))
