import random
# Teste de números aleatórios
# Este programa sorteia uma sequencia de números como no Jogo da Mega Sena e determina quantas jogadas foi necessário até o número ser sorteado e o valor gasto em reais

valor_jogo = 0
sequence = []
num = 0

# função valida os inputs do usuário
def validNumber (number, integer):
    if integer == True:
        if number.isnumeric():
            return number
        else:
            print('Entrada inválida!')
            return False
    else:
        c1 = number.count(',') == 1
        c2 = number.count('.') == 1
        c3 = number.count(',') < 2
        c4 = number.count('.') < 2
        cp1 = (c1 and not c2) or (c2 and not c1)    # implementação do xor
        cp2 = c3 and c4                             # condicional composta
        if cp1 and cp2 == True:
            return number.replace(',', '.')
        else:
            print('Entrada inválida!')
            return False

# funcão de input de cada número do sorteio
def num_input (i):
    return int(input(f'Digite o {i}° número entre [1 e {max_numbers}]: '))

def inputSequence (max_range):
    global max_numbers
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

while True:
    max_numbers = validNumber(input('Entre com a quantidade de números possíveis: '), True)
    if not max_numbers: continue
    break
while True:
    max_range = validNumber(input('Quantidade de números de um jogo: '), True)
    if not max_range: continue
    break
while True:
    valor_jogo = validNumber(input('Preço do jogo: '), False)
    if not valor_jogo: continue
    break
while True:
    premio = validNumber(input('Valor do prêmio: '), False)
    if not premio: continue
    break

print(max_range)
inputSequence(max_range)
sequence.sort()
print(sequence)

input('Pressione enter para iniciar o sorteio...')
    
cont = 0

while True:
    sorted = random.sample(range(1, max_numbers+1), max_range)
    sorted.sort()
    cont += 1
    if sorted == sequence:
        print()
        break

print(f'Ganhou na loteria com {cont} jogadas! Gastou R$ {valor_jogo*cont:.2f}')
print(f'O valor líquido do prêmio é R$ {premio - valor_jogo*cont:.2f}')
input('Press enter to quit ')
