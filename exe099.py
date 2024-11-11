def maior(*valores):
    big = 0
    print("Analisando os valores passados...")

    for c in range(0, len(valores)):
        print(f"{valores[c]}", end=" ")
    print(f"Foram informados {len(valores)} valores ao todo")

    for c in range(0, len(valores)):
        if big < valores[c]:
            big = valores[c]
    print(f"O maior valor informado foi {big}")

    print(30 * "=-")


print(30 * "=-")
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
