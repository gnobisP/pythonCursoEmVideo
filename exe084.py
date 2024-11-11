pessoa = list()
galera = list()

while True:
    n = str(input("Digite o nome: ").strip())
    i = int(input("Digite o peso: "))
    pessoa.append(n)
    pessoa.append(i)
    galera.append(pessoa[:])
    pessoa.clear()

    while True:
        continuar = str(input("Deseja continuar [S/N]? ").strip().upper())
        if continuar in "SN":
            break
        else:
            print("Expressão inválida!")
            continue

    if "N" in continuar:
        break

print(f"Quantidade de pessoas cadastradas {len(galera)}")

mais_pesadas = 0
mais_leves = 99999

for a in range(0, len(galera)):
    if (galera[a][1]) >= mais_pesadas:
        mais_pesadas = galera[a][1]

    if(galera[a][1]) <= mais_leves:
        mais_leves = galera[a][1]

print(f"O maior peso foi de {mais_pesadas}. Peso de", end="")
for t in range(0, len(galera)):
    if galera[t][1] == mais_pesadas:
        print("", galera[t][0], end=",")

print(f"\nO menor peso foi de {mais_leves}. Peso de", end="")
for t in range(0, len(galera)):
    if galera[t][1] == mais_leves:
        print("", galera[t][0], end=",")
