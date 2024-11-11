list_1 = list()
menor = 0
maior = 0

for n in range(0, 5):
    a = int(input(f"Digite um valor para a posição {n}: "))
    list_1.append(a)
    if n == 0:
        menor = a
        maior = a
    elif (not n == 0) and (menor >= a):
        menor = a
    elif (not n == 0) and (maior <= a):
        maior = a

print(f"O menor valor é {menor} nas posições ", end="")
for c in range(0, 5):
    if menor == list_1[c]:
        print(f"{c}... ", end="")

print(f"\nO maior valor é {maior} nas posições ", end="")
for c in range(0, 5):
    if maior == list_1[c]:
        print(f"{c}... ", end="")
