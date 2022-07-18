# Par ou Ímpar
# 
# Aluno: Lucas Bertoni Scarton
# Matrícula: 2018.1.08.009

# Trecho de código para limpar o terminal sempre que executar o arquivo.
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Importando Random para as escolhas do computador e Time para usar a função "Sleep" e dar a sensação de que o computador está pensando.
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
print('Olá! Vamos jogar {}Par{} ou {}Ímpar?{} Eu paro de jogar só quando você perder!'.format(cores['azul'], cores['limpa'], cores['magenta'], cores['limpa']))
sleep(1)

# Escolha inicial. O jogador precisa digitar sim ou nao.
while (True):
  print('')
  querJogar = input('Para jogar, por favor digite {}SIM{} ou {}NAO{}: '.format(cores['verde'], cores['limpa'], cores['vermelho'], cores['limpa'])).lower()

# Caso o jogador opte por "sim", o jogo irá iniciar.
  if querJogar == 'sim':
    sleep(1)
    print('')
    print('Muito bem! Então vamos começar! {}Está preparado{}?!'.format(cores['amarelo'], cores['limpa']))
    sleep(1)

    # Laço para verificar se o jogador digitou corretamente par ou impar.
    while (True):
      print('')
      escolha = input('Escolha {}PAR{} ou {}IMPAR{}: '.format(cores['azul'], cores['limpa'], cores['magenta'], cores['limpa'])).lower()
      computador = random.randint(1,10)
      sleep(1)

      # Caso o jogador escolha "par", iremos executar este trecho do código. Note que o computador já fez a sua jogada.
      if escolha == 'par':

        # Trecho de repetição para garantir que o jogador digitou um número em vez de uma string, e este número precisa ser válido.
        # Encontrei alguma documentação falando sobre as funções "try" e "except" na internet (site: w3schools.com) e decidi testar. Funcionaram como o esperado.
        while (True):
          try:
            sleep(1)
            print('')
            numero = int(input('Por favor, escolha um número de {}1 a 10{}: '.format(cores['negrito'], cores['limpa'])))
          except:
            print('')
            print('{}Erro!! Você não inseriu um número!!{}'.format(cores['vermelho'], cores['limpa']))
          else:
            if numero > 0 and numero < 11:
              break
            else:
              print('')
              print('{}Erro! Valor inválido!{}'.format(cores['vermelho'], cores['limpa']))
        
        res = (numero + computador) % 2

        # Verifica o resto do resultado e conclui um veredito ao jogo.
        if res == 0:
          sleep(1)
          print('')
          print('Eu joguei {} e você jogou {}, e como você escolheu {}par{}, logo, você {}venceu{}! Vamos denovo, eu só paro quando {}EU GANHAR{}!'.format(computador, numero, cores['azul'], cores['limpa'], cores['verde'], cores['limpa'], cores['vermelho'], cores['limpa']))
        else:
          sleep(1)
          print('')
          print('Eu joguei {} e você jogou {}, e como você escolheu {}par{}, logo, você {}perdeu{}! {}Hahahah{}!'.format(computador, numero, cores['azul'], cores['limpa'], cores['vermelho'], cores['limpa'], cores['vermelho'], cores['limpa']))
          break

      # Caso o jogador escolha "impar", iremos executar este trecho do código. Note que o computador já fez a sua jogada.
      elif escolha == 'impar':

        # Trecho de repetição para garantir que o jogador digitou um número em vez de uma string, e este número precisa ser válido.
        # Encontrei alguma documentação falando sobre as funções "try" e "except" na internet (site: w3schools.com) e decidi testar. Funcionaram como o esperado.
        while (True):
          try:
            sleep(1)
            print('')
            numero = int(input('Por favor, escolha um número de {}1 a 10{}: '.format(cores['negrito'], cores['limpa'])))
          except:
            print('')
            print('{}Erro!! Você não inseriu um número!!{}'.format(cores['vermelho'], cores['limpa']))
          else:
            if numero > 0 and numero < 11:
              break
            else:
              print('')
              print('{}Erro! Valor inválido!{}'.format(cores['vermelho'], cores['limpa']))

        res = (numero + computador) % 2

        # Verifica o resto do resultado e conclui um veredito ao jogo.
        if res != 0:
          sleep(1)
          print('')
          print('Eu joguei {} e você jogou {}, e como você escolheu {}impar{}, logo, você {}venceu{}! Vamos denovo, eu só paro quando {}EU GANHAR{}!'.format(computador, numero, cores['magenta'], cores['limpa'], cores['verde'], cores['limpa'], cores['vermelho'], cores['limpa']))
        else:
          sleep(1)
          print('')
          print('Eu joguei {} e você jogou {}, e como você escolheu {}impar{}, logo, você {}perdeu{}! {}Hahahah{}!'.format(computador, numero, cores['magenta'], cores['limpa'], cores['vermelho'], cores['limpa'], cores['vermelho'], cores['limpa']))
          break

      # Pergunta novamente caso o jogador digite algo errado.
      else:
        print('')
        print('{}Erro!{} Infelizmente não entendi o que você disse! {}Vamos tentar de novo?{}'.format(cores['vermelho'], cores['limpa'], cores['amarelo'], cores['limpa']))
    
    # Trecho para encerrar o jogo.
    sleep(1)
    print('')
    print('Pois bem! Como eu disse, agora que te venci, nosso jogo está {}oficialmente encerrado{}! {}Obrigado pela diversão!!{}'.format(cores['negrito'], cores['limpa'], cores['verde'], cores['limpa']))
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