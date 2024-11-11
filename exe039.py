import datetime
n = int(input("Digite o ano de nascimento: "))
n_atual = datetime.date.today().year
if(n_atual-n) > 18:
    print("Você ja devia ter se alistado faz {} anos".format((n_atual-n)-18))
    print("Seu ano de alistamento foi {}".format(n+18))
elif(n_atual-n) < 18:
    print("Você deve se alistar daqui a {} anos".format(18-(n_atual-n)))
    print("Seu ano de alistamento é {}".format(n+18))
else:
    print("Você deve se alistar IMEDIATAMENTE!")
