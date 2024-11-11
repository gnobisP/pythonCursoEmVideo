lista = str(input("Digite uma expressão: ").strip())
quant_1 = 0
quant_2 = 0
for c in range(0, len(lista)):
    if lista[c] == '(':
        quant_1 += 1
    elif lista[c] == ')':
        quant_2 += 1

if quant_1 == quant_2:
    print("Expressão válida!")
else:
    print("Expressão inválida!")

