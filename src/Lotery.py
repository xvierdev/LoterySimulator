import random
# Teste de números aleatórios
# Este programa sorteia uma sequencia de números como no Jogo da Mega Sena e determina quantas jogadas foi necessário até o número ser sorteado e o valor gasto em reais

valor_jogo = 0
sequence = []
num = 0

max_range = int(input('Quantos números serão sorteados: '))
max_numbers = int(input('Quantos números são possíveis: '))
valor_jogo = float(input('Valor do jogo: '))
premio = float(input('Valor do prêmio: '))

def num_input (i):
    return int(input(f'Digite o {i}° número entre [1 e {max_numbers}]: '))

for i in range (1, max_range + 1):
    num = num_input(i)
    while True:
        if num in sequence:
            print(f'{num} já foi escolhido!')
            num = num_input(i)
        elif num < 1 or num > max_numbers:
            print(f'Deve estar no intervalo [1..{max_numbers}]!')
            num = num_input(i)
        else:
            break
    sequence.append(num)

sequence.sort()
print(sequence)

input('Pressione enter para iniciar o sorteio...')
    
cont = 0

while True:
    sorted = random.sample(range(1, max_numbers+1), max_range)
    sorted.sort()
    cont += 1
    #print(f'\rjogos feitos: {cont}', end='')
    # print(sorted)
    # Sequência predefinida
    if sorted == sequence:
        print()
        break

print(f'Ganhou na loteria com {cont} jogadas! Gastou R$ {valor_jogo*cont:.2f}')
print(f'O valor líquido do prêmio é {premio - valor_jogo*cont}')
input('Press enter to quit ')
