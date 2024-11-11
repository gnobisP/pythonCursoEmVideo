dados = dict()
dados["nome"] = str(input("Digite o nome do jogador: ").strip())
partidas = int(input(f"Quantas partidas {dados['nome']} jogou: "))
gols = list()
for c in range(0, partidas):
    gols.append(int(input(f"Quantos gols na partida {c}? ")))
dados["gols"] = gols[:]
dados["total"] = sum(gols)
del gols
# Primeira formatação
print(20*"=-")
print(dados)
# Segunda formatação
print(20*"=-")
for m, k in dados.items():
    print(f"O campo {m} tem o valor {k}")
print(20*"=-")
# Terceira formatação
print(f"O jogador {dados['nome']} jogou {partidas} partidas")
for p in range(0, len(dados["gols"])):
    print(f"=> Na partida {p}, fez {dados['gols'][p]}")
print(f"Foi um total de {dados['total']}")
print(20*"=-")
