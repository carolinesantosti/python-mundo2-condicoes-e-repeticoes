# Desafio: Escreva um programa que leia um número n inteiro e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.

n = int(input('Quantos termos você quer ver?: '))
termo1 = 0
termo2 = 1
contador = 3
print(f'{termo1} -> {termo2} ', end='')

while contador <= n:
    resultado = termo1 + termo2
    print(f' -> {resultado}', end='')
    termo1 = termo2
    termo2 = resultado
    contador += 1
print(' -> Fim!')




