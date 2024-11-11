from random import randint


def sorteia(numeros):
    for c in range(0, 6):
        k = randint(0, 10)
        numeros.append(k)
    print(numeros)


def somaPar(numeros):
    soma = 0
    for c in range(0, 6):
        if numeros[c] % 2 == 0:
            soma += numeros[c]
    print(f"A soma é {soma}")


lista = list()
sorteia(lista)
somaPar(lista)
