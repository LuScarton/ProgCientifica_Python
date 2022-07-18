# Prova 2 (Exercicio 3) - Programação Científica
# 
# Aluno: Lucas Bertoni Scarton
# Matrícula: 2018.1.08.009

# Trecho de código para limpar o terminal sempre que executar o arquivo.
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Setando as variáveis com valores iniciais
valores = []
res = []

# Iterando linhas
for i in range(3):

  # Iniciando nova linha
  linha = []

  # Iterando colunas
  for j in range(3):

    while(True):
      try:
        valor = int(input('Digite o valor do {}º elemento da {}ª linha da sua matriz: '.format(j+1, i+1)))
      except:
        print('Erro! Valor inválido! Por favor, tente novamente.')
      else:
        linha.append(valor)
        break

  valores.append(linha)

# Somando as colunas e colocando o resultado na lista
for i in range(3):
  soma = 0
  for j in range(3):
    soma = soma + valores[j][i]
  res.append(soma)

# Printando a matriz
print('A matriz gerada é:')
for i in range(3):
  print('{}'.format(valores[i]))

# Printando a lista gerada
print('A lista gerada é: {}'.format(res))