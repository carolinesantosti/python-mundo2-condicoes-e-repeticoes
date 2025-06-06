# Desafio: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex.: 5! = 5x4x3x2x1=120

num = int(input('Digite um número: '))      # Solicita ao usuário que digite um número para calcular o fatorial
contador = num                              # Inicializa o contador com o mesmo valor do número digitado
fatorial = 1                                # Inicializa o fatorial com 1 (neutro da multiplicação)
print(f'{num}! = ', end='')                 # Mostra o início da expressão fatorial na tela (ex: "5! = ")
while contador > 0:                         # Enquanto o número atual seguido de ' x ' (ou ' = ' se for o último)
    print(f'{contador}', end=' x ' if contador > 1 else ' = ')
    fatorial *= contador                    # Multiplica o fatorial pelo valor atual do contador
    contador -= 1                           # Diminui o contador para seguir a sequência decrescente
                                            # Exibe o resultado final do fatorial
print(f'{fatorial}')
print(f'O fatorial de {num} é {fatorial}.')
