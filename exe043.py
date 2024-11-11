kg = float(input("Digite o peso em kg: "))
m = float(input("Digite a altura em metros: "))

imc = kg/m**2

print("O IMC dessa pessoa é de {:.1f}".format(imc))

if imc < 18.5:
    print("Abaixo do peso")
elif imc <= 25:
    print("Peso ideal")
elif imc <= 30:
    print("Sobrepeso")
elif imc <= 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")

