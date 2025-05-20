# Desafio 044

print('^' * 40)
print(f'\033[1:30:43m{'LOJAS CAROL':=^40}\033[m')
print('^' * 40)

# Informa o nome do cliente e o preço do produto que ele vai comprar.
print('Olá, seja muito bem-vindo a LOJAS CAROL!')
nome = str(input('Qual o seu nome?\n'))
preco = float(input(f'{nome}, informe o valor do produto:R$'))

# Menu de opções de pagamento.
print('[1] - À vista no dinheiro/cheque: 10% de desconto.')
print('[2] - À vista no cartão: 5% de desconto.')
print('[3] - Em até 2x no cartão: preço normal.')
print('[4] - 3x ou mais no cartão: 20% de juros.')

# Pede a opção de pagamento
opcao = int(input('Escolha a forma de pagamento: '))

# Condicionais para tratar cada opção escolhida
if opcao == 1:
    valor_final = preco * 0.90 # 10% de desconto
    print(f'O valor do seu produto teve 10% de desconto e saiu por R${valor_final:.2f}.')
elif opcao == 2:
    valor_final = preco * 0.95 # 5% de desconto
    print(f'O valor do seu produto teve 5% de desconto e saiu por R${valor_final:.2f}.')
elif opcao == 3:
    valor_final = preco # Sem desconto
    parcela = valor_final / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}, totalizando R${valor_final:.2f}.')
elif opcao == 4:
    parcelas = int(input('Seriam em quantas parcelas: '))
    if parcelas < 3:
        print('Número inválido! Parcelas devem ser 3 ou mais nessa opção.')
    else:
        valor_final = preco + (preco * 0.20) # Aplica 20% de juros
        valor_parcela =  valor_final / parcelas
        print(f'Sua compra será parcelada em {parcelas}x de R${valor_parcela:.2f}, totalizando R${valor_final:.2f} com juros!')
else:
    print('Opção inválida de pagamento. Tente novamente.')

