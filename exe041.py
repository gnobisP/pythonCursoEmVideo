from datetime import date

n = int(input("Digite o ano de nascimento: "))
n_atual = date.today().year
idade = n_atual - n

print("O atleta tem {} anos\nClassificação: ".format(idade), end=" ")

if idade <= 9:
    print("Mirim")
elif 9 < idade <= 14:
    print("Infantil")
elif 19 >= idade > 14:
    print("Júnior")
elif 25 >= idade > 19:
    print("Sênior")
else:
    print("Master")
