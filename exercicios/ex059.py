# Desafio: Crie um programa que leia dois valores e mostre um menu na tela:
# - [1] somar   # - [2] multiplicar     # - [3] maior   # - [4] novos números# - [5] sair do programa
from time import sleep  # Importa a função sleep para similar um tempo de "processamento"
# Solicita dois números ao usuário antes de iniciar o menu
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
while True:  # Inicia um ‘loop’ infinito para manter o menu ativo até o usuário escolher sair
    # Exibe o menu de opções disponíveis
    print('\n---- MENU DE OPÇÕES -----')
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    # Usuário escolhe uma das opções do menu
    opcao = int(input('\nEscolha uma opção: '))
    print('PROCESSANDO...')
    sleep(2)    # Pausa de 2 segundos para criar uma interação mais fluida
    # Verifica qual opção foi escolhida e executa a ação correspondente
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}.')    # Mostra o resultado da soma
    elif opcao == 2:
        produto = n1 * n2
        print(f'O produto entre {n1} e {n2} é {produto}.')  # Mostra o resultado da multiplicação
    elif opcao == 3:
        maior = max(n1, n2)
        print(f'O maior número é {maior}.') # Informa qual dos dois números é maior
    elif opcao == 4:
        # Permite que o usuário digite dois novos números para reiniciar as operações
        print('Digite novos números:')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        # Encerra o programa
        print('Saindo do programa... Até logo!')
        break
    else:
        # Caso o usuário digite uma opção inválida
        print('Opção inválida. Tente novamente.')
