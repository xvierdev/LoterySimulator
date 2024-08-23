import random
# Teste de números aleatórios
# Este programa sorteia uma sequencia de números como no Jogo da Mega Sena e determina quantas jogadas foi necessário até o número ser sorteado e o valor gasto em reais

cont = 0
while True:
    sequence = random.sample(range(1,61), 6)
    sequence.sort()
    cont += 1
    # Sequência predefinida
    if sequence == [2, 3, 5, 15, 21, 39]:
        break
print(f'Ganhou na Mega Sena com {cont} jogadas! Gastou R$ {3.5*cont:.2f}')
