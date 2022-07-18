# Prova 2 (Exercicio 4) - Programação Científica
# 
# Aluno: Lucas Bertoni Scarton
# Matrícula: 2018.1.08.009

# Trecho de código para limpar o terminal sempre que executar o arquivo.
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Importando date pegar o ano atual.
from datetime import date
data = date.today().year

while(True):
  try:
    nasc = int(input('Digite seu ano de nascimento: '))
  except:
    print('Erro! Valor inválido! Por favor, tente novamente.')
  else:
    idade = (data - nasc)

    # Levando em conta que, de acordo com o Guiness, a pessoa mais velha do mundo viveu 119 anos, o valor máximo deve ser 130 (margem de erro).
    if idade > 130 or idade < 0:
      print('Favor digitar um ano de nascimento válido!')
    else:
      break

if idade < 18:
  print('{} anos: Ainda faltam {} anos para você se alistar! Seu alistamento será em {}'.format(idade, (18-idade), (data+18-idade)))

elif idade == 18:
  print('{} anos: Está na hora de se alistar!'.format(idade))

else:
  print('{} anos: Já passou da hora de se alistar! Você está {} anos fora do prazo! Seu alistamento foi em {}'.format(idade, (idade-18), (data-idade+18)))