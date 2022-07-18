# Prova 2 (Exercicio 5) - Programação Científica
# 
# Aluno: Lucas Bertoni Scarton
# Matrícula: 2018.1.08.009

# Trecho de código para limpar o terminal sempre que executar o arquivo.
import os
os.system('cls' if os.name == 'nt' else 'clear')

lista1 = []
lista2 = []

# Adicionando valores na lista
for i in range(8):
  while(True):
    try:
      valor = int(input('Digite o {}º número da sua lista de 8 posições: '.format(i+1)))
    except:
      print('Erro! Valor inválido! Por favor, digite um número.')
    else:
      lista1.append(valor)
      break

# Clonando a lista 1 para uma lista 2 que será usada no futuro.
lista2 = lista1[:]

print('Agora, digite dois valores correspondentes a duas posições da lista!')
print('**OBS: Lembre-se que as posições variam de 0 a 7 (1º e 8º elementos inseridos, respectivamente)')

# Pegando o valor de A
while(True):
  try:
    pos_a = int(input('Digite o valor da 1ª posição (A): '))
  except:
    print('Erro! Valor inválido! Por favor, digite um número.')
  else:
    if pos_a < 0 or pos_a > 7:
      print('Erro! Posição inválida!')
    else:
      # Confirmando o número escolhido e a posição do mesmo.
      print('Você escolheu o número que está na {}ª posição, ou seja, o número {}!'.format(pos_a, lista1[pos_a]))
      break

# Pegando o valor de B
while(True):
  try:
    pos_b = int(input('Digite o valor da 2ª posição (B): '))
  except:
    print('Erro! Valor inválido! Por favor, digite um número.')
  else:
    if pos_b < 0 or pos_b > 7:
      print('Erro! Posição inválida!')
    else:
      # Confirmando o número escolhido e a posição do mesmo.
      print('Você escolheu o número que está na {}ª posição, ou seja, o número {}!'.format(pos_b, lista1[pos_b]))
      break

# Somando os valores das respectivas posições e adicionando na lista 2.
soma = (lista1[pos_a] + lista1[pos_b])
lista2[pos_a] = soma
lista2[pos_b] = soma

print('Resposta do exercício:')
print('Primeira Lista {}   A = {} e B = {}'.format(lista1, pos_a, pos_b))
print('Segunda Lista {}'.format(lista2))