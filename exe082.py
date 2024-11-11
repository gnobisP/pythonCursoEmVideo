lista = list()

while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    while True:
        c = str(input("Deseja continuar [S/N]: ").strip().upper())
        if c in "NnSs":
            break
        else:
            print("Valor inválido! ", end="")
    if c in "Nn":
        break
    else:
        continue

lista_par = list()
lista_impar = list()

for a in range(0, len(lista)):
    if (lista[a] % 2) == 0:
        lista_par.append(lista[a])
    else:
        lista_impar.append(lista[a])

print(f"Lista total{lista}")
print(f"Lista impar{lista_impar}")
print(f"Lista par{lista_par}")
