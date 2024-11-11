n = int(input("Digite um número inteiro: "))
choice = int(input("""[1] converter para BINÁRIO
      \n[2] converter para OCTAL
      \n[3] converter para HEXADECIMAL
      \nEscolha uma das opções para conversão: """))

if choice == 1 or choice == 2 or choice == 3:
    if choice == 1:
        n_conv = bin(n)
        choice = "BINÁRIO"
    elif choice == 2:
        n_conv = oct(n)
        choice = "OCTAL"
    else:
        n_conv = hex(n)
        choice = "HEXADECIMAL"
    print("{} convertido em {} é igual a {}".format(n, choice,  n_conv[2:]))
else:
    print("Nenhuma opção correta foi digitada!")
