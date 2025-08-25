# Desafio 069
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
# a) Quantas pessoas tem mais de 18 anos.
# b) Quando homens foram cadastrados.
# c) Quantas mulheres tem menos de 20 anos.

print('=' * 40)
print('CADASTRO DE PESSOAS'.center(40))
print('=' * 40)

maior_18 = 0
homens = 0
mulheres_20_menos = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()
    if idade > 18:
        maior_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_20_menos += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
            break
    print('=' * 40)

print('=' * 40)
print('FIM DO CADASTRO'.center(40))
print('=' * 40)
print(f'Total de pessoas com mais de 18 anos: {maior_18}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres_20_menos}')
