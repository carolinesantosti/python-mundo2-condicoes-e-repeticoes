# Desafio 040

print('~' * 40)
print('\033[1:30:43m            CLÁSSICO DA MÉDIA           \033[m')
print('~' * 40)

# O aluno digita suas notas
nota1 = float(input('Informe sua primeira nota: '))
nota2 = float(input('Informe sua segunda nota: '))

# Cálculo da média
media = (nota1 + nota2) / 2

# Verifica as condições das médias
if media < 5.0:
    print(f'Sua média foi {media:.1f}. Você está REPROVADO!')
elif 5.0 <= media < 7.0:
    print(f'Sua média foi {media:.1f}. Você está de RECUPERAÇÃO!')
else:
    print(f'Sua média foi {media:.1f}. Você está APROVADO!')
