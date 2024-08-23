import random
# Teste de números aleatórios

cont = 0
while True:
    sequence = random.sample(range(1,61), 6)
    sequence.sort()
    cont += 1
    #print(sequence)
    if sequence == [2, 3, 5, 15, 21, 39]:
        break
print(f'Ganhou na Mega Sena com {cont} jogadas! Gastou R$ {3.5*cont:.2f}')
