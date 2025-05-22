# Desafio 053

frase = str(input('Digite qualquer frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso da frase {junto} é {inverso}.')
if inverso == junto:
    print('Por isso é PALÍNDROMO!')
else:
    print('Essa frase não é PALÍNDROMO.')


