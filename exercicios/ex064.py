# Desafio: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o 999).

contador = 0    # Conta quantos números válidos foram digitados
soma = 0        # Acumula a soma dos números digitados
while True:     # Loop infinito que só para com o break
    num = int(input('Digite um número qualquer: '))
    if num == 999:  # 999 é a "flag" (sentinela) de parada
        break       # Interrompe o ‘loop’ quando o usuário digitar 999
    contador += 1  # Incrementa o contador de números válidos
    soma += num  # Soma acumulada dos números
# Mostra o resultado
print(f'Você digitou {contador} números e a soma de todos eles foi de {soma}.')
print('\n-------FIM DO PROGRAMA--------')
