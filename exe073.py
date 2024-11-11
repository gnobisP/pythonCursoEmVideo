tabela = ("Atlético-MG", "Flamengo", "Palmeiras", "Fortaleza", "Corinthians", "Bragantino",
          "Fluminense", "América-MG", "Atlético-GO", "Santos", "Ceará", "Internacional",
          "São Paulo", "Atlético-PR", "Cuiabá", "Juventude", "Grêmio", "Bahia", "Sport",
          "Chapecoense")
print(f"Os cinco primeiros são {tabela[0:5]}")
print(f"Os quatro últimos são {tabela[-4:]}")
print(f"Os times em ordem alfabetica são {sorted(tabela)}")
print("A Chapecoense está na", 1+ tabela.index("Chapecoense"),"posição")
