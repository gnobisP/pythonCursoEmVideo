aluno = dict()
aluno["nome"] = str(input("Digite o nome: "))
aluno["média"] = float(input(f"Média de {aluno['nome']}: "))
print(20*"=-")
print(f"- Nome é igual a {aluno['nome']}")
print(f"- Média é igual a {aluno['média']}")
if aluno["média"] >= 7:
    print("- Situação é igual a aprovada!")
else:
    print("- Situação é igual a reprovada!")
