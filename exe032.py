from datetime import date
n = int(input("Digite um ano ou 0 para o ano atual do PC: "))

if n == 0:
    n = date.today().year

if (n % 4) == 0 and ((n % 100 != 0) or (n % 100 + n % 400 == 0)):
    print("The year {} is leap year".format(n))
else:
    print("The year {} is not a leap year".format(n))
