import random
from operator import itemgetter
from time import sleep
rpg = {"jogador_1": random.randint(1, 6),
       "jogador_2": random.randint(1, 6),
       "jogador_3": random.randint(1, 6),
       "jogador_4": random.randint(1, 6)}

for c, n in rpg.items():
    print(f"{c} tirou {n} no dado.")
    sleep(1)

ordem = sorted(rpg.items(), key=itemgetter(1), reverse=True)

print(40*"*")
print("==RANKING DOS JOGADORES==  ")
for a, b in enumerate(ordem):
    print(f"{a+1}º lugar: {b[0]} com {b[1]}")
