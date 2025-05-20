# Desafio 043

print('*' * 40)
print(f'\033[1:40m{'ÍNDICE DE MASSA CORPORAL':=^40}\033[m')
print('*' * 40)

# Usuário informa o seu nome, sua altura e peso.
nome = str(input('Olá, informe seu nome: '))
altura = float(input(f'{nome}, informe a sua altura: '))
peso = float(input('E o seu peso: '))

#Cálculo para saber o IMC
imc = peso / (altura ** 2)

# Verifica se o IMC está abaixo, normal ou acima do peso
if imc <= 18.5:
    print(f'{nome}, seu IMC é {imc:.2f}.Você está abaixo do peso. Que tal conversar com um nutricionista?')
elif imc <= 25:
    print(f'{nome}, seu IMC é {imc:.2f}. Você está com o peso normal. Continue assim!')
elif imc <=30:
    print( f'{nome}, seu IMC é {imc:.2f}. Você está com sobrepeso. Que tal fazer alguns exercícios?')
elif imc <= 40:
    print(f'{nome}, seu IMC é {imc:.2f}. Você está obeso(a). Sugiro que procure um nutricionista!')
else:
    print(f'{nome}, seu IMC é {imc:.2f}. Você está com obesidade mórbida. Precisamos URGENTE procurar um profissional!')
