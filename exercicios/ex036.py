# Desafio 036
print('=' * 40)
print('           ANÁLISE DE CRÉDITO         ')
print('=' * 40)
print('SEJA BEM-VINDO AO BANCO PYTHON')

# Pede ao usuário digitar as informações
comprador = str(input('Qual o seu nome?\n')).title()
valor_casa = float(input('Qual o valor da casa que você quer comprar?\nR$'))
salário = float(input('E qual o seu salário?\nR$'))
anos = int(input('Em quantos anos você quer pagar a casa?\n'))

# Cálculos
total_meses = anos * 12
prestacao = valor_casa / total_meses
limite = salário * 0.30

print(f'\n{comprador}, para pagar uma casa de R${valor_casa:.2f} em {anos} anos,')
print(f'a prestação será de R${prestacao:.2f} por mês.')

# Resultados
if prestacao <= limite:
    print('✅ Seu empréstimo foi APROVADO! Parabéns!')
else:
    print('❌ Empréstimo NEGADO: a prestação excede 30$ do seu salário.')

