veloc = float(input("Qual é a velocidade do carro? "))

if veloc > 80:
    print("""\nMultado, você execedeu o limite de velocidade que é 80km/h!")
Você deve pagar uma multa de {}R$""".format((veloc-80)*7.0))

print("\nTenha um bom dia! Dirija com segurança!")
