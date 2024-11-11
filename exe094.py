lista_dados = list()
while True:
    dados = dict()
    dados["nome"] = str(input("Digite o nome do jogador: ").strip())
    partidas = int(input(f"Quantas partidas {dados['nome']} jogou: "))
    gols = list()
    for c in range(0, partidas):
        gols.append(int(input(f"Quantos gols na partida {c}? ")))
    dados["gols"] = gols[:]
    dados["total"] = sum(gols)
    while True:
        para = str(input("Deseja continuar? [S/N]: ").strip().upper())
        if para in "SN":
            break
        print("Erro! Digite novamente!")
    lista_dados.append(dados)
    del gols
    del dados
    if para == "N":
        break
# Impressão
print("")
print("cod nome       gols         total")
for c in range(0, len(lista_dados)):
    print(f"{c}   {lista_dados[c]['nome']}    {lista_dados[c]['gols']}   {lista_dados[c]['total']}")
while True:
    continuar = int(input("Mostrar dados de qual jogador? (999 para parar)"))
    if continuar == 999:
        break
    print(f"Levantamento do jogador {lista_dados[continuar]['nome']}")
    for p in range(0, len(lista_dados[continuar]['gols'])):
        print(f"=> Na partida {p}, fez {lista_dados[continuar]['gols'][p]}")
