# Lista de Exercicios Python - Programação Científica
# 
# Aluno: Lucas Bertoni Scarton
# Matrícula: 2018.1.08.009

# Trecho de código para limpar o terminal sempre que executar o arquivo.
import os
os.system('cls' if os.name == 'nt' else 'clear')

print('Por favor, insira os dados a seguir corretamente para que seja feito o reajuste apropriado!')

while(True):
  try:
    salario = int(input('Digite o salário atual do funcionário: R$'))
  except:
    print('Erro! Valor inválido! Por favor, tente novamente.')
  else:
    if salario < 0:
      print('Valor inválido. Salário negativo.')
    else:
      break

while(True):

  genero = input('Digite o gênero do funcionário [M/F]: ').upper()

  if genero == 'M' or genero == 'F':
    break

  else:
    print('Gênero inválido. Favor inserir M para Masculino e F para Feminino.')

while(True):
  try:
    tempo = int(input('A quantos anos esse funcionário trabalha na empresa: '))
  except:
    print('Erro! Valor inválido! Por favor, tente novamente.')
  else:
    if tempo < 0:
      print('Valor inválido. Tempo negativo!')
    else:
      break

if genero == 'F':
  if tempo < 15:
    salario = (salario*1.05)
  elif tempo <= 20:
    salario = (salario*1.12)
  else:
    salario = (salario*1.23)
else:
  if tempo < 20:
    salario = (salario*1.03)
  elif tempo <= 30:
    salario = (salario*1.13)
  else:
    salario = (salario*1.25)

print('Levando em conta os dados fornecidos, o novo salário do funcionário será de R${}.'.format(salario))