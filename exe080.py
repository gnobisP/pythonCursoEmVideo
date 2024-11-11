lista = list()
n = int(input("Digite um valor: "))
lista.append(n)
print("Adicionado ao final da lista")

for k in range(1, 4):
    n = int(input("Digite um valor: "))
    for a in range(0, len(lista)):
        if n <= lista[a]:
            lista.insert(a, n)
            print(f"Adicionado na {a} posição")
            break

        elif a == len(lista):
            lista.insert(a, n)
            print("Adicionado ao final da lista")

print(lista)
