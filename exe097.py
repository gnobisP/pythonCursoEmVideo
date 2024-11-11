def escreva(txt):
    tam = len(txt)
    print((tam+2) * "~")
    print(f" {txt}")
    print((tam+2) * "~")


palavra = str(input("Digite algo: ").strip())
escreva(palavra)
