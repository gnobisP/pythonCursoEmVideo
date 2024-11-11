print(41*"=")
print("{:^40}".format("Banco GPC"))
print(41*"=")

nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_1 = 0

valor = int(input("Digite o valor que você quer sacar: "))

while valor > 10:
    if valor >= 50:
        valor -= 50
        nota_50 += 1
    elif valor >= 20:
        valor -= 20
        nota_20 += 1
    elif valor >= 10:
        valor -= 10
        nota_10 += 1
nota_1 = valor

if not nota_50 == 0:
    print("Total de {} células de R$50".format(nota_50))
if not nota_20 == 0:
    print("Total de {} células de R$20".format(nota_20))
if not nota_10 == 0:
    print("Total de {} células de R$10".format(nota_10))
if not nota_1 == 0:
    print("Total de {} células de R$1".format(nota_1))
print(41*"=")
print("Volte sempre ao banco GPC! Tenha um bom dia!")

