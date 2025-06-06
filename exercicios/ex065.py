# Desafio: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
# e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

# Inicializa as variáveis para a soma dos números e o contador de quantos foram digitados
soma = 0
contador = 0
# Variáveis que vão armazenar o maior e menor número digitado
# Serão definidas dentro do Laço na primeira execução
maior = menor = 0
# Início do Laço infinito: só termina com um break
while True:
    num = int(input('Digite um número: '))      # Lê um número do usuário
    soma += num     # Atualiza a soma e o contador
    contador += 1
    if contador == 1:       # Na primeira execução, define o número como maior e menor
        maior = menor = num
    else:
        if num > maior:     # Compara para atualizar o maior e o menor
            maior = num
        if menor < num:
            menor = num
    # Pergunta se o usuário quer continuar, já tratando espaços e letras maiúsculas
    continuar = int(input('Você quer continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':    # Se a resposta for N, sai do laço
        break
media = soma / contador     # Calcula a média dos números digitados
# Exibe os resultados finais formatados
print(f'A media dos números digitados foi {media:.2f}.')
print(f'O maior valor digitado foi {maior:.2f} e o menor valor digitado foi {menor:.2f}.')
