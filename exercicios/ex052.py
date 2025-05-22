# Desafio 052

num = int(input('Digite um número inteiro: '))
total = 0
for i in range(1, num + 1):
    if num % i == 0:
       total += 1
if total == 2:
    print('É primo!')
else:
    print(f'Não é primo.')
