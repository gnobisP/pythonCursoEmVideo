import random
import time
print("Suas opções")
print("[0] Pedra")
print("[1] Papel")
print("[2] Tesoura")

n1 = int(input("Qual é a sua jogada? "))
n2 = random.randint(0, 2)

lista = ["pedra", "papel", "tesoura"]
text = ["\033[30m", "\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m",
        "\033[36m", "\033[37m"]
if 2 >= n1 >= 0:
    print("{}JO".format(text[3]))
    time.sleep(0.5)
    print("KEN")
    time.sleep(0.5)
    print("PO!!!\n", 10*"{}-=-".format(text[2]))
    print(" O computador jogou  {}".format(lista[n2]))
    print(" O jogador jogou  {}\n".format(lista[n1]), 10*"-=-")

    if n1 == n2:
        print("{}EMPATE!{}".format(text[1], text[0]))
    elif (n1 == 0 and n2 == 2) or (n1 == 1 and n2 == 0) or (n1 == 2 and n2 == 1):
        print("{}O JOGADOR GANHOU!{}".format(text[1], text[0]))
    else:
        print("{}O COMPUTADOR VENCEU!{}".format(text[1], text[0]))
else:
    print("{}JOGADA INVÁLIDA!{}".format(text[1], text[0]))
