# Desafio 042

print('~' * 40)
print('\033[1:30:41m       ANALISANDO TRIÂNGULOS v2.0       \033[m')
print('~' * 40)

# Usuário informa três valores
a = int(input('Digite o valor da reta 1: '))
b = int(input('Digite o valor da reta 2: '))
c = int(input('Digite o valor da reta 3: '))

# Verifica se as três retas podem formar um triângulo
if a < b + c and b < a + c and c < a + b:
    print(f'\nAs retas {a}, {b} e {c} formam um triângulo!')

# Agora verifica o tipo
    if a == b == c:
        print(f'As retas {a}, {b} e {c} formam o tipo: EQUILÁTERO.')
    elif a == b or b == c or a == c:
        print(f'As retas {a}, {b} e {c} formam o tipo: ISÓSCELES.')
    else:
        print(f'As retas {a}, {b} e {c} formam o tipo: ESCALENO.')
else:
    print(f'\nAs retas {a,b,c} NÂO formam um triângulo')
