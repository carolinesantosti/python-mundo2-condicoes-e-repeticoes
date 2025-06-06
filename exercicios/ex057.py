# Desafio 057
# Programa que valida a entrada do sexo de um usuário (M ou F)
# Não permite seguir adiante até que um valor válido seja digitado

# Início do programa com uma mensagem introdutória
print('Cadastro de Sexo')
print('-' * 20)
# Solicita ao usuário que informe o sexo e já formartar para facilitar a validação
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()
# Enquanto a entrada for inválida, continua a pedir uma nova tentativa
while sexo not in ['M', 'F']:
    print('Valor inválido, tente novamente!')
    sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()
# Mensagem final indicando que a entrada foi aceita com sucesso
print(f'Sexo "{sexo}" registrado com sucesso!')
