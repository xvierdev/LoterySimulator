import random
# Wesley Xavier - 1 ADS 2024 - 2
# Simula o sorteio da Mega Sena e determina quantas jogadas foram necessárias para sair os números escolhidos

sequence = []
for i in range (1,7):
    num = int(input(f'Digite o {i}° número entre 0 e 60: '))
    while num in sequence:
        print('Número já escolhido!')
        num = int(input(f'Digite o {i}° número entre 0 e 60: '))
    sequence.append(num)

sequence.sort()
print('Números escolhidos:', sequence)

cont = 0

while True:
    sorted = random.sample(range(1,61), 6)
    sorted.sort()
    cont += 1
    if sorted == sequence:
        break

print(f'Ganhou na Mega Sena com {cont} jogadas! Gastou R$ {3.5*cont:.2f}')
input('Press enter to quit ')
