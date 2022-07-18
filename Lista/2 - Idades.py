# Lista de Exercicios Python - Programação Científica
# 
# Aluno: Lucas Bertoni Scarton
# Matrícula: 2018.1.08.009

# Trecho de código para limpar o terminal sempre que executar o arquivo.
import os
os.system('cls' if os.name == 'nt' else 'clear')

grupo = []
menos_5 = 0
mais_18 = 0
maior_idade = 0

for i in range(10):
  while(True):
    try:
      idade = int(input('Digite a idade da {}ª pessoa: '.format(i+1)))
    except:
      print('Valor inválido! Por favor, digite o número corretamente.')
    else:
      if idade > maior_idade:
        maior_idade = idade

      if idade < 0:
        print('Valor inválido! Idade negativa.')
      elif idade < 5:
        menos_5 = menos_5 + 1
        grupo.append(idade)
        break
      elif idade > 18:
        mais_18 = mais_18 + 1
        grupo.append(idade)
        break
      else:
        grupo.append(idade)
        break

media = sum(grupo)/len(grupo)

print('A média de idade do grupo é {}.'.format(media))
print('{} pessoas tem acima de 18 anos.'.format(mais_18))
print('{} pessoas tem abaixo de 5 anos.'.format(menos_5))
print('A maior idade lida foi {}.'.format(maior_idade))