sexo = str(input("Digite o sexo [M/F]: ").strip().upper())

while sexo not in "MF":
    print("Erro! Digite novamente!")
    sexo = str(input("Digite o sexo [M/F]: ").strip().upper())
