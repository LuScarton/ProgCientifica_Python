print('Seja bem vindo! Vamos as compras?!')

menorValor = 9999999999999999
cont = 0
total = 0
aux2 = 0

while (aux2 == 0):
  item = input('Digite o nome do produto: ')
  valor = int(input('Digite o valor do produto: '))

  if (valor < menorValor):
    maisBarato = item
    menorValor = valor

  if (valor > 1000):
    cont = cont + 1

  total = total + valor

  aux = 0

  while (aux == 0):
    resp = input('Você tem mais produtos que deseja inserir? [S/N]')

    if (resp == 'S'):
      print('Muito bem então! Vamos continuar!')
      aux = 1

    elif (resp == 'N'):
      print('Muito bem! O seu pedido foi encerrado e aqui estão algumas informações!')
      aux = 1
      aux2 = 1

    else:
      print('Por favor, digite S ou N para continuarmos!')

print('O total gasto em produtos foi de: R${}'.format(total))
print('A quantidade de produtos com o valor acima de R$1000 foi de: {}'.format(cont))
print('Seu produto mais barato foi: {}'.format(maisBarato))