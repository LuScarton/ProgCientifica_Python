# Prova 2 (Exercicio 2) - Programação Científica
# 
# Aluno: Lucas Bertoni Scarton
# Matrícula: 2018.1.08.009

# Trecho de código para limpar o terminal sempre que executar o arquivo.
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Setando as variáveis com valores iniciais
pobres = 0
nro_filhos = 0
total_salario = 0
maior_salario = 0
end_program = 0
populacao = []

print('Por favor, insira os dados sobre salário e número de filhos dos habitantes.')
print('OBS: Para encerrar a inserção, digite um valor de salário negativo.')

while(True):

  # Resetando o valor de Habitantes a cada iteração
  habitante = []

  while(True):
    try:
      salario = float(input('Digite o salário: R$'))
    except:
      print('Erro! Valor inválido! Por favor, tente novamente.')
    else:
      if salario < 0:
        end_program = 1
        break

      # Foi necessário adicionar um teste para verificar se o 150 era o maior salário
      elif salario < 150:
        habitante.append(salario)
        pobres = pobres + 1
        if salario > maior_salario:
          maior_salario = salario
        break

      elif salario > maior_salario:
        habitante.append(salario)
        maior_salario = salario
        break
      
      else:
        habitante.append(salario)
        break

  # Se o salário for negativo, end_program já vai ter trocado pra 1 e o resto do programa nem roda mais
  if end_program == 1:
    break

  total_salario = total_salario + salario

  while(True):
    try:
      filhos = int(input('Digite o número de filhos: '))
    except:
      print('Erro! Valor inválido! Por favor, tente novamente.')
    else:
      if filhos < 0:
        print('Erro! Valor inválido! Por favor, tente novamente.')
      else:
        nro_filhos = nro_filhos + filhos
        habitante.append(filhos)
        break

  # Adicionando um habitante "(salario, filhos)" em uma populacao (afinal, populacao nada mais é do que um conjunto de habitantes)
  populacao.append(habitante)

# Calculando alguns resultados
media_salario = (total_salario/len(populacao))
media_filhos = (nro_filhos/len(populacao))
media_pobres = ((pobres/len(populacao))*100)

print('A média de salário da população é: {:.2f}'.format(media_salario))
print('A média do número de filhos é: {:.2f}'.format(media_filhos))
print('O maior salário dos habitantes é: {:.2f}'.format(maior_salario))
print('O percentual de pessoas com salário menor que R$150,00 é: {:.2f}%'.format(media_pobres))