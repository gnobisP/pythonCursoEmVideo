n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = float(input("Digite o terceiro valor: "))

# Encontrando o menor número:
menor = n1
if n2 <= n1 and n2 <= n3:
    menor = n2
if n3 <= n1 and n3 <= n2:
    menor = n3
print("O menor número é {}".format(menor))

# Encontrando o maior número:   
maior = n2
if n1 >= n3 and n1 >= n2:
    maior = n1
if n3 >= n1 and n3 >= n2:
    maior = n3
print("O maior número é {}".format(maior))
