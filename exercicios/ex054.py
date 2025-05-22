# Desafio 054

from datetime import date
ano_atual = date.today().year
maiores = 0
menores = 0
for pessoa in range(1, 8):
    nasc = int(input(f'Em que ano a [{pessoa}ª] pessoa nasceu: '))
    idade = ano_atual - nasc
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print(f'{menores} pessoas ainda não atingiram a maioridade.')
print(f'{maiores} pessoas já são maiores de idade.')
