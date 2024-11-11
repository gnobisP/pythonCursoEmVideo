phrase = input("Digite uma frase: ").lower()
print("A letra A aparece {} vezes na frase.".format(phrase.count("a")))
print("A letra A apareceu pela primeira vez na posição {}".format(phrase.find("a")+1))
print("A letra A apareceu pela última vez na posição {}".format(phrase.rfind("a")+1))
