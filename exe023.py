number = int(input("write a number: "))
unity = number % 10
ten = number//10 % 10
hundred = number//100 % 10
thousand = number//1000 % 10
print("Analisando o número {}".format(number))
print("Milhar: {}".format(thousand))
print("Centena: {}".format(hundred))
print("Dezena: {}".format(ten))
print("Unidade: {}".format(unity))



