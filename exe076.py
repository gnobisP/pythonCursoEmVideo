listagem = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00,
            "Transferidor", 4.20)
print(40*"-")
print("{:^40}".format("Listagem de Preços"))
print(40*"-")
for n in range(0, len(listagem)):
    if (n % 2) == 0:
        print(f"{listagem[n]:.<33}", end="")
    else:
        print(f"R${listagem[n]:>5.2f}")
print(40*"-")
