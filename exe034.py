salary = float(input("Funcionário, digite o seu salário: R$"))
# Calculando o salario:
if salary > 1250.0:
    salary = salary*1.10
else:
    salary = salary*1.15
# Exibindo
print("O salário novo é: R${:.2f}".format(salary))
