import random

print("-=-"*20)
print("Vou pensar em um número entre 0 e 10. Tente adivinhar...")
print("-=-"*20)
g = random.randint(0, 10)
tentativas = 0
while 1:
    tentativas += 1
    n = int(input("Em que número eu pensei? "))
    if g == n:
        break
    elif g > n:
        print("O número que pensei é maior")
    else:
        print("O número que eu pensei é menor")
print("\033[31m", "-=-"*20)
print("Acertou com {} tentativas. Parabens!!".format(tentativas))
print("-=-"*20, "\033[30m")
