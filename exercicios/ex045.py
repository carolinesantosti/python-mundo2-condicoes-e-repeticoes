# Desafio 045
from random import choice
from time import sleep

print('*' * 40)
print('\033[1:30:45m      GAME: PEDRA, PAPEL E TESOURA      \033[m')
print('*' * 40)

# Opções disponíveis
opcoes = ['pedra', 'papel', 'tesoura']

# Jogador escolhe
jogador = input('Escolha entre pedra, papel ou tesoura: '). strip().lower()

# Validação básica
if jogador not in opcoes:
    print('Jogada inválida! Tente novamente.')
else:
    computador = choice(opcoes) # Computador escolhe

    # Draminha
    print('JO...')
    sleep(0.5)
    print('KEN...')
    sleep(0.5)
    print('PÔ!!!')
    sleep(0.5)
    print('=~' * 15)
    print(f'Você jogou {jogador}!\nE o computador jogou {computador}.')
    print('=~' * 15)
    # Condições vitórias
    if jogador == computador:
        print('EMPATE!')
    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'papel' and computador == 'pedra') or \
         (jogador == 'tesoura' and computador == 'papel'):
        print('Você VENCEU! 🎉')
    else:
        print('Você PERDEU! 😢')
