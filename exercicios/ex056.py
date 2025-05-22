# Desafio 056
# Inicializando as variáveis
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
mulher_menor_20 = 0
# ‘Loop’ para coletar dados de 4 pessoas
for p in range(1, 5):
    print(f'~~~~~~~ {p}ª PESSOA ~~~~~~~~')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    # Soma de todas as idades para calcular a média depois
    soma_idade += idade
    # Verifica se é o primeiro homem ou se é o mais velho até agora
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome

        # Conta quantas mulheres têm menos de 20 anos
        if sexo in 'Ff' and idade < 20:
            mulher_menor_20 += 1
# Calcula a média de idade do grupo
media_idade += soma_idade / 4
# Exibe os resultados
print(f'\nA média de idade do grupo de pessoas é de {media_idade} anos.')
print(f'O homem mais velho do grupo tem {maior_idade_homem} anos e se chama {nome_velho}.')
print(f'No grupo temos {mulher_menor_20} mulheres com menos de 20 anos.')
