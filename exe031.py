dist = float(input("Qual é a distância de sua viagem?"))
print("Você está prestes a começar uma viagem de {}km".format(dist))

if dist >= 200:
    print("O valor da passagem é: R${:.2f}".format(dist*0.45))
else:
    print("O valor da passagem é: R${:.2f}".format(dist*0.5))
