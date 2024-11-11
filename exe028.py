import random
import time

print("-=-"*20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-"*20)
n = int(input("Em que número eu pensei? "))
g = random.randint(0, 5)
print("PROCESSANDO...")
time.sleep(3)

if g == n:
    print("Parabens! Você conseguiu me vencer!")
else:
    print("Ganhei! Eu pense no número {} e não no {}".format(g, n))
