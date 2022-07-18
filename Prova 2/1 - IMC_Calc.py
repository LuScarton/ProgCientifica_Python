# Prova 2 (Exercicio 1) - Programação Científica
# 
# Aluno: Lucas Bertoni Scarton
# Matrícula: 2018.1.08.009

# Trecho de código para limpar o terminal sempre que executar o arquivo.
import os
os.system('cls' if os.name == 'nt' else 'clear')

print('Olá! Vamos calcular o seu IMC? Para isso, por favor insira o seu peso e sua altura!')

# Inserindo peso
while (True):
  try:
    peso = float(input('Por favor, digite seu peso (em KG): '))

  except:
    print('Erro! Valor inválido! Vamos tentar novamente?')

  else:
    # Levando em conta que, de acordo com o Guiness, a pessoa mais leve do mundo pesava 2kg e a mais pesada por volta de 600/650kg, os valores válidos estão entre 0kg e 800kg (margem de erro)
    if peso >= 0 and peso <= 800:
      print('Muito bem, então você está pesando {:.1f}kg! Registrei no meu banco de dados!'.format(peso)) # Confirmando que pegou o valor correto
      break
    else:
      print('Erro! Valor inválido! Vamos tentar novamente?')

# Inserindo altura
while (True):
  try:
    altura = float(input('Agora, por favor, digite sua altura (em Metros): '))

  except:
    print('Erro! Valor inválido! Vamos tentar novamente?')
    
  else:
    # Levando em conta que, de acordo com o Guiness, a menor pessoa do mundo mede 63cm e a mais alta do mundo mede 2.51m, os valores válidos estão entre 50cm e 3m (margem de erro)
    if altura >= 0.50 and altura <= 3.0:
      print('Muito bem, sua altura é {:.2f}m! Registrei no meu banco de dados!'.format(altura)) # Confirmando que pegou o valor correto
      break
    else:
      print('Erro! Valor inválido! Vamos tentar novamente?')

imc = peso / (altura * altura)

print('Analisando seus dados, consegui calcular que o seu IMC atualmente é {:.1f}.'.format(imc))

# Verificando faixas
if imc < 18.5:
  print("Com isso, você se encaixa na seguinte faixa: Abaixo do peso!")

elif imc <= 25:
  print("Com isso, você se encaixa na seguinte faixa: Peso ideal!")

elif imc <= 30:
  print("Com isso, você se encaixa na seguinte faixa: Sobrepeso!")

elif imc <= 40:
  print("Com isso, você se encaixa na seguinte faixa: Obesidade!")

else:
  print("Com isso, você se encaixa na seguinte faixa: Obesidade Mórbida!")