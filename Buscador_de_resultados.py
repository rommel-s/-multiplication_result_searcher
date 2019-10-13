#BUSCADOR DE RESULTADOS V.0.2

val = int(input('Digite o valor a ser pesquisado: '))
for a in range(0, 2000):
  for h in range(0, 2000):
    valor = a * h
    if valor == val:
      print(f'{a} x {h} = {valor}')