import random
lista_aleatorio = (random.randint(0, 20), random.randint(0, 20), random.randint(0, 20),
                   random.randint(0, 20), random.randint(0, 20))
print(f"Os valores sorteados foram: {lista_aleatorio}")

menor = lista_aleatorio[0]
for n in range(1, 5):
    if menor > lista_aleatorio[n]:
        menor = lista_aleatorio[n]

maior = lista_aleatorio[0]
for n in range(1, 5):
    if maior < lista_aleatorio[n]:
        maior = lista_aleatorio[n]

print(f"O menor é {menor} e o maior é {maior}")
