# Jokenpô | Pedra, Papel e Tesoura
# 
# Aluno: Lucas Bertoni Scarton
# Matrícula: 2018.1.08.009

# Trecho de código para limpar o terminal sempre que executar o arquivo. Copiei da internet e funcionou.
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Importando Random para pegar um valor aleatório para o computador e Time para usar a função "Sleep" e dar a sensação de que o computador está pensando
import random
from time import sleep

# Pintando o texto com o código direto nas palavras.
jogadas = ["\033[1;36mPedra\033[m", "\033[;1mPapel\033[m", "\033[1;95mTesoura\033[m"]

# Dicionário de cores
cores = {'limpa': '\033[m',
         'ciano': '\033[1;36m',
         'negrito': '\033[;1m',
         'magenta': '\033[1;95m',
         'vermelho': '\033[1;91m',
         'verde': '\033[1;92m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;94m',
        }

# Começando o jogo de fato, e utilizando outro método para pintar o texto (".format" + dicionário de cores).
print('Olá! Vamos jogar {}Jokenpô?{}'.format(cores['azul'], cores['limpa']))
print('')
sleep(1)
print('Para jogar, por favor digite:')
sleep(1)
print('{}1{} para escolher {}Pedra{}'.format(cores['ciano'], cores['limpa'], cores['ciano'], cores['limpa']))
sleep(1)
print('{}2{} para escolher {}Papel{}'.format(cores['negrito'], cores['limpa'], cores['negrito'], cores['limpa']))
sleep(1)
print('{}3{} para escolher {}Tesoura{}'.format(cores['magenta'], cores['limpa'], cores['magenta'], cores['limpa']))
sleep(1)

# Laço de repetição para tratamento de erros. O jogador precisa digitar 1, 2 ou 3.
aux = 0
while aux == 0:
  print('')
  jogador = input('Digite sua escolha: ')
  print('')
  print('Computando jogada...')
  print('')

  if jogador == '1':
    sleep(1)
    print('Muito bem! Você escolheu {}Pedra{}!'.format(cores['ciano'], cores['limpa']))
    aux = 1

  elif jogador == '2':
    sleep(1)
    print('Muito bem! Você escolheu {}Papel{}!'.format(cores['negrito'], cores['limpa']))
    aux = 1

  elif jogador == '3':
    sleep(1)
    print('Muito bem! Você escolheu {}Tesoura{}!'.format(cores['magenta'], cores['limpa']))
    aux = 1

  else:
    sleep(1)
    print('{}Erro! Por favor, digite um valor válido!{}'.format(cores['vermelho'], cores['limpa']))
    sleep(1)
    print('')
    print('{}1{} para escolher {}Pedra{}'.format(cores['ciano'], cores['limpa'], cores['ciano'], cores['limpa']))
    print('{}2{} para escolher {}Papel{}'.format(cores['negrito'], cores['limpa'], cores['negrito'], cores['limpa']))
    print('{}3{} para escolher {}Tesoura{}'.format(cores['magenta'], cores['limpa'], cores['magenta'], cores['limpa']))
    sleep(1)

# Fazendo a jogada do computador de maneira aleatória. Precisei aplicar a cor direto nas palavras lá em cima para elas sempre saírem nas cores certas.
sleep(1)
print('')
print("O computador está pensando...")
print('')
sleep(2)
computador = random.choice(jogadas)
print('O computador jogou {}!'.format(computador))

sleep(1)
print('')
print('Comparando resultados...')
print('')
sleep(2)

# Verificando os resultados. Como apliquei a cor direto nas palavras lá em cima para saírem com a cor certa no terminal, precisei comparar utilizando as cores também.
if computador == '\033[1;36mPedra\033[m' and jogador == '1' or computador == '\033[;1mPapel\033[m' and jogador == '2' or computador == '\033[1;95mTesoura\033[m' and jogador == '3':
  print('{}Ninguém venceu! Houve um EMPATE!{}'.format(cores['amarelo'], cores['limpa']))

elif computador == '\033[1;36mPedra\033[m' and jogador == '3' or computador == '\033[;1mPapel\033[m' and jogador == '1' or computador == '\033[1;95mTesoura\033[m' and jogador == '2':
  print('{}Infelizmente você perdeu! Vitória para o computador!{}'.format(cores['vermelho'], cores['limpa']))

else:
  print('{}Parabéns, você venceu!{}'.format(cores['verde'], cores['limpa']))

print('')