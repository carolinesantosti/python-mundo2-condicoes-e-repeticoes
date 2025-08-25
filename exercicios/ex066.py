# Desafio 066: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

contador = 0    # Inicializa o contador de números digitados
soma = 0        # Inicializa a variável que vai somar todos os valores digitados

while True:     # Laço infinito controlado manualmente com break
    num = int(input('Digite um número: '))      # Pede um número ao usuário
    if num == 999:      # Verifica se o número é o código de parada
        break       # Encerra o Loop imediatamente
    contador += 1  # Incrementa o número de entradas válidas
    soma += num     # Adiciona o número à soma total

# Exibe o resultado final após o break
print(f'Você digitou {contador} números e a soma de todos eles foi: {soma}.')
