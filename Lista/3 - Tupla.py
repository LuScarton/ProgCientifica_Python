#Lista de Exercicios Python - Programação Científica
# 
# Aluno: Lucas Bertoni Scarton
# Matrícula: 2018.1.08.009

# Trecho de código para limpar o terminal sempre que executar o arquivo.
import os
os.system('cls' if os.name == 'nt' else 'clear')

tupla = ()
pos = []
number9 = 0
pares = 0

for i in range(10):
  while(True):
    try:
      valor = int(input('Digite o {}º valor: '.format(i+1)))
    except:
      print('Valor inválido! Por favor, digite o número corretamente.')
    else:
      if valor == 9:
        number9 = number9 + 1
      elif valor == 3:
        pos.append(i)

      par = valor % 2

      if par == 0:
        pares = pares + 1

      tupla = tupla + (valor, )
      break

print('Printando a tupla para ajudar na comparação:')
print(tupla)

media = sum(tupla)/len(tupla)

print('O número 9 aparece {} vezes'.format(number9))
print('O número 3 aparece nas seguintes posições {}'.format(pos))
print('A média dos valores é {}.'.format(media))
print('A quantidade de números pares é {}.'.format(pares))