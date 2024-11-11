soma_idade = 0
idade_mais_velho = 0
quant_mulher = 0
nome_mais_velho = "Não cadastrado"

for contador in range(1, 5):
    print("-----{} pessoa-----".format(contador))
    nome = str(input("Nome: ").strip())
    idade = int(input("Idade: "))
    sexo = str((input("Sexo [M/F]: ").strip().upper()))

    soma_idade = soma_idade + idade

    if (idade > idade_mais_velho) and ("M" in sexo):
        nome_mais_velho = nome
        idade_mais_velho = idade

    if(idade <= 20) and ("F" in sexo):
        quant_mulher = quant_mulher+1

media = soma_idade/4

print("A média de idade do grupo é de {} anos".format(media))
print("O homem mais velho tem {} anos e se chama ".format(idade_mais_velho), nome_mais_velho)
print("Ao todo são {} mulheres abaixo de 20 anos".format(quant_mulher))
