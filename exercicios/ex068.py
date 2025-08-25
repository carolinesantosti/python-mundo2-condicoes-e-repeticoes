# Desafio 068
# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint  # Importa função para gerar número aleatório

print('=' * 40)
print('PAR OU ÍMPAR?'.center(40))
print('=' * 40)

vitorias = 0  # Contador de vitórias consecutivas

# 'Loop' principal do jogo
while True:
    usuario = int(input('Digite um valor: '))
    par_impar = str(input('Par ou Ímpar [P/I]? ')).upper().strip()[0]
    comp = randint(1, 10)  # Computador escolhe número aleatório
    total = comp + usuario  # Soma os dois números

    print(f'Você jogou {usuario} e o computador {comp}. Total de {total}.', end=' ')

    # Verifica se o jogador venceu
    if (par_impar == 'P' and total % 2 == 0) or (par_impar == 'I' and total % 2 != 0):
        print('Você ganhou! 🎉')
        vitorias += 1  # Soma mais uma vitória
    else:
        print('Você perdeu! 💥')
        break  # Encerra o jogo se perder

# Mostra o total de vitórias após a derrota
print(f'\n🏁 Fim de jogo! Você teve {vitorias} vitórias consecutivas.')
