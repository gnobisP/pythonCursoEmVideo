salario = float(input("Digite o salário mensal do comprador: "))
val_casa = float(input("Digite o valor da casa: "))
pres = int(input("Em quantos anos será o financiamento: "))
pres_mens = val_casa / (pres * 12)

print("Para pagar uma casa de R${} em {} a prestação será de R${:.2f}"
      .format(val_casa, pres, pres_mens))

if (salario * 0.3) > pres_mens:
    print("{}Emprestimo aprovado!{}".format('\033[32m', '\033[37m'))
else:
    print("{}Emprestimo negado!{}".format('\033[31m', '\033[37m'))
