from datetime import datetime
carteira = dict()
carteira["nome"] = str(input("Nome: "))
idade = (int(input("Ano de Nascimento: ")) )
carteira["idade"] = datetime.now().year - idade
carteira["ctps"] = int(input("Carteira de trabalho (0 não tem): "))

if carteira["ctps"] != 0:
    carteira["contratação"] = int(input("Ano de contratação: "))
    carteira["salário"] = int(input("Salário: R$"))
    carteira["aposentadoria"] = (35 + carteira["contratação"])- idade

# Impressão
print(20*"-=")

for c, n in carteira.items():
    print(f"{c} tem o valor de {n}")


