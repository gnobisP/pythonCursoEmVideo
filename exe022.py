nome = input("Digite o seu nome completo: ").strip()
print("Seu nome em maiusculo é: ", nome.upper())
print("Seu nome em minuscilo é: ", nome.lower())
print("Seu nome tem ao todos {} letras".format((len(nome))-(nome.count(' '))))
frase = nome.split()
print("Seu primeiro nome é: ", frase[0])
print("Seu primeiro nome possui {} letras".format(len(frase[0])))
