# Caixa Eletrônico
# 
# Aluno: Lucas Bertoni Scarton
# Matrícula: 2018.1.08.009

# Trecho de código para limpar o terminal sempre que executar o arquivo.
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Importando Time para usar a função "Sleep" e dar a sensação de que o computador está contando as cédulas.
from time import sleep

# Dicionário de cores.
cores = {'limpa': '\033[m',
         'negrito': '\033[;1m',
         'ciano': '\033[1;36m',
         'amarelo': '\033[1;33m',
         'amarelito': '\033[1;93m',
         'vermelho': '\033[1;91m',
         'magenta': '\033[1;95m',
         'azul': '\033[1;94m',
         'verde': '\033[1;92m',
        }

# Lendo o valor que o cliente deseja sacar.
while (True):
  try:
    print('')
    numero = int(input('Por favor, digite o valor que você deseja {}sacar{}: '.format(cores['verde'], cores['limpa'])))
  except:
    print('')
    print('{}Erro!! Você não inseriu um número!!{}'.format(cores['vermelho'], cores['limpa']))
  else:
    if numero >= 0:
      break
    else:
      print('')
      print('{}Erro! Valor negativo inserido!{}'.format(cores['vermelho'], cores['limpa']))
print('')

# Notas de 200
notas200 = numero // 200
numero -= notas200*200

# Notas de 100
notas100 = numero // 100
numero -= notas100*100

# Notas de 50
notas50 = numero // 50
numero -= notas50*50

# Notas de 20
notas20 = numero // 20
numero -= notas20*20

# Notas de 10
notas10 = numero // 10
numero -= notas10*10

# Notas de 5
notas5 = numero // 5
numero -= notas5*5

# Notas de 2
notas2 = numero // 2
numero -= notas2*2

# Notas de 1
notas1 = numero

print('Contando seu {}dinheiro{}...'.format(cores['verde'], cores['limpa']))
sleep(2)
print('')
print('{}Verificando disponibilidade de notas...{}'.format(cores['verde'], cores['limpa']))
sleep(2)
print('')
print('Você irá {}receber{}:'.format(cores['verde'], cores['limpa']))
if notas200 > 0:
  print('{} cédulas de {}R$200{}'.format(notas200, cores['negrito'], cores['limpa']))

if notas100 > 0:
  print('{} cédulas de {}R$100{}'.format(notas100, cores['ciano'], cores['limpa']))

if notas50 > 0:
  print('{} cédulas de {}R$50{}'.format(notas50, cores['amarelo'], cores['limpa']))

if notas20 > 0:
  print('{} cédulas de {}R$20{}'.format(notas20, cores['amarelito'], cores['limpa']))

if notas10 > 0:
  print('{} cédulas de {}R$10{}'.format(notas10, cores['vermelho'], cores['limpa']))

if notas5 > 0:
  print('{} cédulas de {}R$5{}'.format(notas5, cores['magenta'], cores['limpa']))

if notas2 > 0:
  print('{} cédulas de {}R$2{}'.format(notas2, cores['azul'], cores['limpa']))

if notas1 > 0:
  print('{} cédulas de {}R$1{}'.format(notas1, cores['verde'], cores['limpa']))

print('')