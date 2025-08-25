# Desafio 067
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

print('=' * 40)
print('TABUADA v3.0'.center(40))
print('=' * 40)
# Início de um 'Loop' infinito — só será interrompido quando o usuário digitar um número negativo
while True:
    # Solicita ao usuário o número para gerar a tabuada
    num = int(input('Qual valor você quer mostrar na sua tabuada?'))
    print('=' * 40)
    # Se o número for negativo, o programa encerra o 'loop' com 'break'
    if num < 0:
        break

    # Se o número for 0 ou positivo, gera a tabuada de 1 a 10
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')

    # Exibe um separador visual e uma mensagem de finalização da tabuada atual
    print('='* 40)

# Mensagem final após o usuário digitar um número negativo
print('TABUADA ENCERRADA! VOLTE SEMPRE!')
