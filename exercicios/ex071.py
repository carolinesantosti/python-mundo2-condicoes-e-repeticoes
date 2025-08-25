# Desafio 071
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS.: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$2.

print('=' * 40)
print('BANCO CAROL DEV'.center(40))
print('=' * 40)

valor = int(input('Quanto você quer sacar? R$: '))
print('-' * 40)
cedula = 50
total_cedulas = 0

while True:
    if valor >= cedula:
        valor -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print( f'Total de {total_cedulas} cédulas de R${cedula}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 2
        total_cedulas = 0
        if valor == 0:
            break

print('=' * 40)
print('VOLTE SEMPRE AO BANCO CAROL DEV'.center(40))
print('=' * 40)

