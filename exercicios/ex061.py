# Desafio: Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

# O programa inicializa com uma mensagem e pedindo ao usuário o primeiro termo e a razão
print('======Gerador de PA======')
pt = int(input('Qual é o primeiro termo: '))
r = int(input('Qual é a razão: '))
# Inicializa o contador em 1 e também o termo como valor do primeiro termo
contador = 1
termo = pt
# Enquanto o contador for menor ou igual a 10
while contador <= 10:
    print(f'{termo}', end=' -> ') # Mostra o termo atual
    termo += r # Soma a razão ao termo (gera o próximo)
    contador += 1 # Incrementa o contador em +1
print('FIM!')














