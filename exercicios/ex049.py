# Desafio 049

print(f'\033[1:30:42m{"Tabuada V.2.0":~^40}\033[m')
from time import sleep

# Usuário digita um número
nome = input('Digite seu nome: ')
num = int(input(f'{nome}, digite um número para exibir a sua tabuada: '))
print(f'A tabuada de {num} é:')
for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')
    sleep(1)
print('\033[1:30:45mTABUADA FEITA\033[m')