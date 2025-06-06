# Desafio: Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

# O programa inicializa com uma mensagem e pedindo ao usuário o primeiro termo e a razão
print('======Gerador de PA======')
pt = int(input('Qual é o primeiro termo: '))
r = int(input('Qual é a razão: '))

termo = pt       # Termo atual da PA
contador = 1     # Conta quantos termos foram mostrados
total = 0       # Soma o total de termos exibidos até agora
mais = 10       # Começa exibindo 10 termos

while mais != 0:        # Enquanto o usuário não digitar 0, o programa continua
    total += mais   # Soma os novos termos pedidos ao total exibido
    while contador <= total:
        print(f'{termo}', end=' -> ') # Mostra o termo atual
        termo += r # Soma a razão ao termo (gera o próximo)
        contador += 1 # Incrementa o contador em +1
    print('PAUSA')
    # Pergunta ao usuário se deseja ver mais termos
    mais = int(input('\nQuantos termos a mais você quer ver: '))
print(f'Progressão finalizada com {total} termos mostrados.')




