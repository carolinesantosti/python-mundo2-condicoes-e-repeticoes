# Desafio 041

print('=' * 40)
print('\033[1:30:42m         CLASSIFICANDO ATLETAS          \033[m')
print('=' * 40)

# Importando o módulo date
from datetime import date

# O atleta informa o nome e ano do seu nascimento
nome = str(input('Olá, informe seu nome: '))
ano = int(input(f'{nome}, informe o ano de seu nascimento: '))

# Pega o ano atual automaticamente
ano_atual = date.today().year

# Calcula a idade do atleta
idade = ano_atual - ano

# Verifica as condições para categoria conforme a idade do atleta
if idade <= 9:
    print(f'Você tem {idade} anos e sua categoria é a MIRIM!')
elif idade <= 14:
    print(f'Você tem {idade} anos e sua categoria é INFANTIL!')
elif idade <= 19:
    print(f'Você tem {idade} anos e sua categoria é JUNIOR!')
elif idade == 20:
    print(f'Você tem {idade} anos e sua categoria é SÊNIOR!')
else:
    print(f'Você tem {idade} anos e sua categoria é MASTER!')



