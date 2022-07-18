#Lista de Exercicios Python - Programação Científica
# 
# Aluno: Lucas Bertoni Scarton
# Matrícula: 2018.1.08.009

# Trecho de código para limpar o terminal sempre que executar o arquivo.
import os
os.system('cls' if os.name == 'nt' else 'clear')

lista = []
pos = []
i = 0

# Escolha inicial. O usuário precisa digitar sim ou nao.
while (True):
  querContinuar = input('Deseja adicionar outro número? [S/N]: ').lower()

# Caso o usuário opte por "sim", um novo valor será inserido
  if querContinuar == 's':
    while(True):
      try:
        valor = int(input('Digite um valor: '))
      except:
        print('Valor inválido! Por favor, digite o número corretamente.')
      else:
        if valor == 5:
          pos.append(i)
        lista.append(valor)
        i = i + 1
        break

# Caso o usuário opte por "nao", seus dados serão apresentados e a aplicação encerrada
  elif querContinuar == 'n':

    desce = sorted(lista, reverse = True)

    print('Seus dados foram:')
    print('Quantidade de Números Digitados: {}'.format(len(lista)))
    print('Lista em ordem decrescente: {}'.format(desce))
    print('O número 5 aparece nas seguintes posições: {}'.format(pos))

    break

# Caso o usupario não digite corretamente, o computador dirá que não entendeu e perguntará novamente até entender.
  else:
    print('Erro! Valor inválido! Digite S para Sim e N para Não. Vamos tentar novamente.')