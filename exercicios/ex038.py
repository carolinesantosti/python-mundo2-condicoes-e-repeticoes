# Desafio 038
print('=' * 40)
print('\033[1:30:46m           COMPARANDO NÚMEROS           \033[m')
print('=' * 40)

# Pede ao usuário para digitar dois números inteiros
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

# Comparando os dois números que o usuário digitou
if num1 > num2:
    print(f'O primeiro número [{num1}] é maior do que o segundo número [{num2}]!')
elif num2 > num1:
    print(f'O segundo número [{num2}] é maior do que o primeiro [{num1}]!')
else:
    print(f'Os números digitados são iguais!')
