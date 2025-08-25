# Desafio 070
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# a) Qual é o TOTAL GASTO na compra.
# b) Quantos produtos custam MAIS de R$1000.
# c) Qual é o NOME do produto MAIS BARATO.

# Cabeçalho visual
print('=' * 40)
print('CAIXA'.center(40))
print('=' * 40)

# Inicializa as variáveis de controle
total_gasto = 0     # Soma total dos produtos
acima_mil = 0       # Contador de produtos que custam mais de R$1000
nome_mais_barato = ''       # Nome do produto mais barato
preco_mais_barato = 0       # Preço do produto mais barato
cont = 0    # Contador de produtos cadastrados

# 'Loop' principal do programa
while True:
    produto = str(input('Produto: '))       # Solicita o nome do produto
    valor = float(input('Valor: R$'))       # Solicita o valor do produto
    total_gasto += valor        # Soma o valor ao total gasto
    cont += 1   #Incrementa o número de produtos cadastrados
    if valor > 1000:
        acima_mil += 1      # Conta se o produto custa mais de R$1000
    if cont == 1 or valor < preco_mais_barato:
        preco_mais_barato = valor       # Atualiza o menor valor
        nome_mais_barato = produto      # Atualiza o nome do produto mais barato
    continuar = ' '     # Inicializa a variável com espaço vazio
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]        # Valida resposta do usuário
    if continuar == 'N':
        break       # Encerra o 'loop' se a resposta for 'N'
    print('=' * 40)     # Linha de separação entre os cadastros
# Exibe o resumo final da compra
print(f'\nO total gasto na compra foi R${total_gasto:.2f}.')
print(f'Temos {acima_mil} produto(s) custando mais de R$1000.00.')
print(f'O produto mais barato foi {nome_mais_barato}, custando R${preco_mais_barato:.2f}.')
# Rodapé visual
print('=' * 40)
print('NOTA ENCERRADA'.center(40))
print('=' * 40)
