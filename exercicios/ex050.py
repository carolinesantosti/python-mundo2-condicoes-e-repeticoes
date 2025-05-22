# Desafio 050

soma = 0
cont = 0
for i in range(1,7):
    num = int(input(f'Digite o {i}º número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'A soma dos números pares digitados é {soma}.')
print(f'Você digitou {cont} números PARES.')