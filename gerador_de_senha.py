from random import choice
print('Bem-vindo ao gerador de senhas!')
caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&1234567890*'
print('-*' * 15)
numero = input('Digite a quantidades de senhas que deseja: ')
if numero.isdigit:
    numero = int(numero)
else:
    print('Digite um número válido')

tamanho = input('Digite o número de caracteres que você que na sua senha: ')
if tamanho.isdigit:
    tamanho = int(tamanho)
else:
    print('Digite um número válido')

for pwd in range(int(numero)):
    senhas = ''
    for c in range(int(tamanho)):
        senhas = senhas + choice(caracteres)
    print(senhas)
    