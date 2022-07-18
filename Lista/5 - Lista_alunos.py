#Lista de Exercicios Python - Programação Científica
# 
# Aluno: Lucas Bertoni Scarton
# Matrícula: 2018.1.08.009

# Trecho de código para limpar o terminal sempre que executar o arquivo.
import os
os.system('cls' if os.name == 'nt' else 'clear')

def funcMedia(notas):
  res = sum(notas)/len(notas)
  return res

aluno = []
notas = []
turma = []

# Escolha inicial. O usuário precisa digitar sim ou nao.
while (True):
  querContinuar = input('Deseja adicionar outro aluno? [S/N]: ').lower()

# Caso o usuário opte por "sim", um novo aluno poderá ser inserido
  if querContinuar == 's':
    aluno = []
    while(True):
      try:
        nome = str(input('Digite o nome do aluno: '))
      except:
        print('Por favor, digite um nome válido')
      else:
        aluno.append(nome)
        break

    notas = []
    for i in range(2):
      while(True):
        try:
          nota = float(input('Digite a {}ª nota: '.format(i+1)))
        except:
          print('Valor inválido! Por favor, digite o número corretamente.')
        else:
          if nota < 0:
            print('Valor inválido! Nota negativa!')
          else:
            notas.append(nota)
            media = funcMedia(notas)
            break
    
    aluno.append(media)
    turma.append(aluno)

# Caso o usuário opte por "nao", seus dados serão apresentados e a aplicação encerrada
  elif querContinuar == 'n':
    print(turma)
    break

# Caso o usupario não digite corretamente, o computador dirá que não entendeu e perguntará novamente até entender.
  else:
    print('Erro! Valor inválido! Digite S para Sim e N para Não. Vamos tentar novamente.')