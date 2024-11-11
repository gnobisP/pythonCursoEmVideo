cp1 = float(input("Digite o 1° tamanho:"))
cp2 = float(input("Digite o 2° tamanho:"))
cp3 = float(input("Digite o 3° tamanho:"))

# É um triângulo:
if(cp1 + cp2 > cp3) and (cp3 + cp2 > cp1) and (cp3 + cp1 > cp2):
    print("As retas formam um triângulo")

# Verificando o tipo de triângulo:
    if cp1 == cp2 == cp3:
        print("É um triângulo equilátero")
    elif cp1 == cp2 or cp1 == cp3 or cp2 == cp3:
        print("É um triângulo isósceles")
    else:
        print("É um triângulo escaleno")

# Não é um triângulo:
else:
    print("As retas não formam um triângulo")


