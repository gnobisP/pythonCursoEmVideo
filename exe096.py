def area(a, b):
    print("-="*20)
    print("Controle de Terrenos")
    print("-="*20)
    print(f"A área de um terreno de {a}x{b} é {a * b} m²")


comprimento = float(input("comprimento (m): "))
largura = float(input("largura (m): "))
area(comprimento, largura)
