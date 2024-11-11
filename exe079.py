lista = list()
while True:
    a = int(input("Digite um número: "))

    if a not in lista:
        lista.append(a)
    else:
        print("Valor duplicado, não vou adicionar!")

    while True:
        ciclo = str(input("Quer continuar? [S/N]: ").strip().upper())
        if ciclo in "SN":
            break
        else:
            print("Erro! Digire S ou N!")

    if ciclo in "N":
        print(20 * "=-=")
        break
    else:
        continue
lista.sort()
print(lista)
