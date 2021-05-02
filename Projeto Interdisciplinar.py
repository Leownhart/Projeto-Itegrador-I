'''
Opção 1 -> Conversão para decimal para as bases binário, hexadecimal e octadecimal .

Grupo : Francisco Leandro Almeida Martins  RGM: 26690951
'''
# Menu com todas as opções disponiveis
print('''\033[32m***************** MENU ********************
\033[33m(1) - Conversão de Decimal para Binário
\033[33m(2) - Conversão de Decimal para Hexadecimal
\033[33m(3) - Conversão de Decimal para Octadecimal
\033[32m*******************************************''')
op = int(input('\033[31mInforme uma das opções disponiveis: '))
número = int(input('\033[35mDigite um número decimal: '))
if op == 1:  # Convertendo o número para base Binária
    print('{} Convertido para Binário é igual a {}'
          .format(número, bin(número)[2:]))

elif op == 2:  # Convertendo o número para base Hexadecimal
    print('\033[35m{} \033[32mconvertido para Hexadecimal é igual a \033[34m{}'
          ''.format(número, hex(número)[2:].upper()))

elif op == 3: # Convertendo o número para base Octadecimal
    print('\033[35m{} \033[32mconvertido para Octadecimal é igual a \033[34m{}'
          .format(número, oct(número)[2:]))

else:  # Opção Invalida
    print('\033[35mA Opção informada é Invalida. Tente Novamente.')

