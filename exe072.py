numeros = ("zero", "um", "dois", 'três', "quatro", "cinco", "seis", "sete", "oito",
           "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis",
           "dezessete", "dezoito", "dezenove", "vinte")

n = int(input("Digite um número: "))

while 1:
    if n > 21 or n < 0:
        print("Número inválido! Digite um número de 0 a 20")
        n = int(input("Digite um número: "))
    else:
        break

print(f"Você digitou o número {numeros[n]}")
