name = input("Whats is your full name? ").strip()
nome_dividido = name.split()
quant = name.count(" ")
print("Your first name is:", nome_dividido[0])
print("Your last name is:", nome_dividido[quant])
