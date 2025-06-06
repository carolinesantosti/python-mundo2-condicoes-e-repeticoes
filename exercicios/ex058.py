# Desafio 058

from random import randint  # Importa apenas a função randint do módulo random para gerar números inteiros aleatórios
from time import sleep      # Importa a função sleep do módulo time para criar uma pausa (delay) no programa

# O computador "pensa" em um número aleatório entre 0 e 10
computador = randint(0, 10)
print('Vou pensar em um número. TENTE ADIVINHAR...')     # Mensagem para o jogador saber que o jogo começou

jogador = int(input('Digite um número de 0 a 10: '))   # Jogador tenta adivinhar o número
palpites = 1 # Conta o primeiro palpite

print('PROCESSANDO...')     # Cria suspense antes de mostrar o resultado
sleep(2)  # Aguarda 3 segundos antes de continuar

while jogador != computador:    # Enquanto não acertar...
    print('VOCÊ ERROU, TENTE NOVAMENTE!')

    if jogador < computador:
        print('DICA: Mais... Tente um número maior.')
    elif jogador > computador:
        print('DICA: Menos... Tente um número menor.')

    jogador = int(input('Digite um número de 0 a 10: '))
    print('PROCESSANDO...')
    sleep(2)
    palpites += 1

print('PARABÉNS!! VOCÊ GANHOU!!')
print(f'O computador escolheu o número {computador} e foram feitas {palpites} tentativas.')


