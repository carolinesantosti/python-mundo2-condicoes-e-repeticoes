# Desafio 048

soma = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        print(c, end=' ')
        soma += c

print(f'\nA soma de todos os múltiplos de 3 que são ímpares é igual a {soma}.')