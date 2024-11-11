lista = list()
quant = 0

while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    quant += 1
    while True:
        c = str(input("Deseja continuar [S/N]: ").strip().upper())
        if c in "NnSs":
            break
        else:
            print("Valor inválido! ", end="")
    if(c in "Nn"):
        break
    else:
        continue

lista.sort(reverse = True)

print(f"Quantidade de números digitados: {quant}")
print(f"A lista em ordem decrescente é {lista}")

if 5 in lista:
    print("O valor 5 se encontra na lista")
else:
    print("O valor 5 não se encontra na lista")
