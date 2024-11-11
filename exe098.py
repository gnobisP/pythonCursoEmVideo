from time import sleep


def contagem(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1

    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if inicio > fim:
        for c in range(inicio, fim - 1, -passo):
            print(f" {c}", end="")
            sleep(0.5)

    else:
        for c in range(inicio, fim + 1, passo):
            print(f" {c}", end="")
            sleep(0.5)
    print(" FIM!")

contagem(1, 10, 1)
contagem(10, 0, 2)
print("Agora é sua vez de personalizar a contagem!")
comeco = int(input("Inicío: "))
final = int(input("Fim: "))
decremento = int(input("passo: "))
contagem(comeco, final, decremento)
