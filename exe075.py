numeros = ()
for n in range(0, 5):
    n1 = (int(input("Digite um número: ")),)
    numeros = numeros + n1
print(f"{numeros}")
print(f"O valor 9 apareceu {numeros.count(9)}")
