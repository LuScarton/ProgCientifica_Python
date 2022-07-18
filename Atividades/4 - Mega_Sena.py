# Mega Sena
# 
# Aluno: Lucas Bertoni Scarton
# Matrícula: 2018.1.08.009

# Trecho de código para limpar o terminal sempre que executar o arquivo.
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Importando Random para o sorteio dos números e Time para usar a função "Sleep" e dar a sensação de que o computador está sorteando os números fisicamente.
import random
from time import sleep

# Dicionário de cores.
cores = {'limpa': '\033[m',
         'ciano': '\033[1;36m',
         'negrito': '\033[;1m',
         'magenta': '\033[1;95m',
         'vermelho': '\033[1;91m',
         'verde': '\033[1;92m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;94m',
        }

# Mensagem inicial.
print('Olá! Seja bem vindo à {}Mega Sena{}! Vamos jogar?!'.format(cores['verde'], cores['limpa']))
sleep(1)

# Escolha inicial. O jogador precisa digitar sim ou nao.
while (True):
  print('')
  querJogar = input('Para jogar, por favor digite {}SIM{} ou {}NAO{}: '.format(cores['verde'], cores['limpa'], cores['vermelho'], cores['limpa'])).lower()

# Caso o jogador opte por "sim", o jogo irá iniciar.
  if querJogar == 'sim':

    # Laço para verificar quantos jogos ele deseja tentar.
    while (True):
      try:
        print('')
        nro_jogadas = int(input('Quantos jogos você deseja fazer? {}(Limite: 5 jogadas){} '.format(cores['negrito'], cores['limpa'])))

      # Caso o usuário tente inserir uma string:
      except:
        print('')
        print('{}Erro! Você não inseriu um número!{}'.format(cores['vermelho'], cores['limpa']))

      else:
        if nro_jogadas > 0 and nro_jogadas < 6:
          print('')
          print('Muito bem então, você irá realizar {}{} jogos{}!'.format(cores['verde'], nro_jogadas, cores['limpa']))
          break

        # Caso o número seja negativo ou superior a 5:
        else:
          print('')
          print('{}Erro! Valor inválido!{} Certifique-se de que você está inserindo o valor corretamente e não está fazendo muitas jogadas. {}(Limite: 5 jogadas){}'.format(cores['vermelho'], cores['limpa'], cores['negrito'], cores['limpa']))

    # Inserindo as combinações diferentes
    total = []
    for x in range(nro_jogadas):
      jogo = []
      print('')
      print('Esta será a sua {}{}ª combinação!{}'.format(cores['verde'], x+1, cores['limpa']))

      # Inserindo os valores das combinações
      for i in range(6):
        while (True):
          try:
            num = int(input('Digite o {}{}º número{} que deseja jogar: '.format(cores['verde'], i+1, cores['limpa'])))

          # Caso o usuário tente inserir uma string:
          except:
            print('')
            print('{}Erro! Você não inseriu um número!{}'.format(cores['vermelho'], cores['limpa']))
            print('')
          else:

            # Caso o número seja repetido:
            if num in jogo:
              print('')
              print('{}Este valor já foi inserido!{}'.format(cores['vermelho'], cores['limpa']))
              print('')
              
            elif num > 0 and num < 61:
              jogo.append(num)
              jogo.sort()
              break

            # Caso o número não esteja entre 1 e 60:
            else:
              print('')
              print('{}Erro! Valor inválido!{} O número deve estar entre {}1 e 60{}!'.format(cores['vermelho'], cores['limpa'], cores['negrito'], cores['limpa']))
              print('')

      # Criando a lista das jogadas
      total.append(jogo)

    # Pausa dramática
    print('')
    sleep(3)
    print('Agora que você fez as suas jogadas, vamos ao {}grande sorteio{}!! Preparado?!'.format(cores['verde'], cores['limpa']))
    sleep(2)
    final = []

    # Sorteando os 6 números premiados
    for x in range(6):
      print('')
      print('O {}º número sorteado foi...'.format(x+1))

      sleep(2)

      # Sorteia um valor aleatório e verifica se é repetido
      while (True):

        sorteio = random.randint(1,60)

        if sorteio not in final:
          final.append(sorteio)
          break
      
      print('{}{}{}!'.format(cores['verde'], sorteio, cores['limpa']))
      sleep(2)

    # Printando o resultado final:
    sleep(3)
    print('')
    print('Todos os números foram sorteados, e esse é o {}resultado final da Mega Sena{}!!'.format(cores['verde'], cores['limpa']))
    print('')
    final.sort()
    print('{}Números da Mega Sena: {}{}'.format(cores['verde'], final, cores['limpa']))

    # Printando suas jogadas para poder comparar com o resultado do sorteio:
    print('')
    sleep(3)
    print('Seus jogos: ')
    for x in range(nro_jogadas):
      print('Jogo {}: {}{}{}'.format(x+1, cores['verde'], total[x], cores['limpa']))
    print('')
    sleep(5)
    print('Caso você tenha {}ganhado{}, parabéns! Dirija-se à {}lotérica{} mais próxima de você para receber o seu prêmio!'.format(cores['verde'], cores['limpa'], cores['negrito'], cores['limpa']))
    print('Caso contrário, não desista! {}O próximo pode ser você{}!!'.format(cores['azul'], cores['limpa']))
    print('')

    break

# Caso o jogador opte por "nao", o jogo irá fechar.
  elif querJogar == 'nao':

    sleep(1)
    print('')
    print('{}Óh.. que pena!{} Quem sabe da próxima vez? Até mais!!'.format(cores['vermelho'], cores['limpa']))
    print('')
    break

# Caso o jogador não digite corretamente, o computador dirá que não entendeu e perguntará novamente até entender.
  else:
    sleep(1)
    print('')
    print('Pera... não entendi. Você {}quer jogar{} ou {}não{}?'.format(cores['verde'], cores['limpa'], cores['vermelho'], cores['limpa']))
    sleep(1)