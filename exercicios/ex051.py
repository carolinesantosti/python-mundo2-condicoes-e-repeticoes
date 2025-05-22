# Desafio 051

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
print('Os 10 primeiros termos são: ')
for i in range(10):
    termo = primeiro + i * razao
    print(f'{termo}', end=' → ')
print('FIM!')