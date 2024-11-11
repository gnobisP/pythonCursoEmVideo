from math import sqrt
cat_op = float(input("Digite o valor do cateto oposto: "))
cat_adj = float(input("Digite o valor do cateto adjacente: "))
hip = sqrt(cat_op**2+cat_adj**2)
print("O valor da hipotenusa é: {}".format(hip))
