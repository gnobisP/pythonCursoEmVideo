cp1 = float(input("Digite o 1° tamanho:"))
cp2 = float(input("Digite o 2° tamanho:"))
cp3 = float(input("Digite o 3° tamanho:"))

if(cp1 + cp2 > cp3) and (cp3 + cp2 > cp1) and (cp3 + cp1 > cp2):
    print("As retas formam um triângulo")
else:
    print("As retas não formam um triângulo")
