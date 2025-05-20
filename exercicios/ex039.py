# Desafio 039

from datetime import date

print('~' * 40)
print('\033[1:30:41m           ALISTAMENTO MILITAR          \033[m')
print('~' * 40)

# Usuário informa o ano de nascimento
ano = int(input('Qual o ano que você nasceu?  '))

# Pega o ano atual automaticamente
ano_atual = date.today().year

# Calcula a idade da pessoa
idade = ano_atual - ano

# Verifica as condições de alistamento
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano_alistamento = ano_atual + saldo
    print(f'Você ainda vai se alistar. Faltam {saldo} ano(s).')
    print(f'Seu alistamento será em {ano_alistamento}.')
else:
    saldo =  idade - 18
    ano_alistamento = ano_atual - saldo
    print(f'Você já deveria ter se alistado há {saldo} ano(s).')
    print(f'Seu alistamento foi em {ano_alistamento}.')





