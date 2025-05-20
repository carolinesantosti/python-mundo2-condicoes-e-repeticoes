# Desafio 37

print('\033[1:32:40mConversor de Bases Númericas\033[m')

# Usuário vai digitar um número inteiro
num = int(input('Digite um número: '))

# Faz as conversões antes da escolha
binario = bin(num)[2:]
octal = oct(num)[2:]
hexadecimal = hex(num)[2:]

# Escolhendo o tipo de conversão
print('Escolha uma base de conversão: ')
print('[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal')
opcao = int(input('Sua opção de conversão: '))

#
if opcao == 1:
    print(f'O número {num} convertido para Binário é: {binario}\n')
elif opcao == 2:
    print(f'O número {num} convertido para OCTAL é: {octal}\n')
elif opcao == 3:
    print(f'O número {num} convertido para HEXADECIMAL é: {hexadecimal}\n')
else:
    print('Opção inválida!')

print('=' * 30, '\033[1:30:41mFIM DO PROGRAMA\033[m', '=' * 30)




