#!/usr/bin/env python3

#questão1
q1a = 2
q1b = 4
q1c = 8
q1d = q1b - q1a * q1c
print("Questão 1")
print(f"valor de d: {q1d}")

#questão 2
print("Questão 2")
q2a = int(input("Digite um número: ")) #é importante fazer isso pois por padrão o input é string
if(q2a < 5):
  q2b = q2a *2
elif(q2a >= 5 and q2a < 7):
  q2b = 10
else:
  q2b = 100 - q2a
print(f"Valor de b: {q2b}")

#questão 3
print("Questão 3")
q3a = int(input("Digite um número: "))
q3b = 1
while(q3a > 1):
  q3b = q3b + q3b * q3a
  print(q3b)
  q3a = q3a - 1
  print(q3a)
print(f"Valor de b: {q3b}")

#questão 4
print("Questão 4")
def calcula(num):
  if(num == 1):
    print("retorna 1")
    return 1;
  else:
    print("Não retorna 1")
    print(num)
    return num*calcula(num-1)
n = int(input("Digite um número: "))
calcula(n)

#questões 5 e 6
print("Questão 5 e 6")
def busca(e, d, x, list):
  print(f"Valor de d: {d}")
  if(e <= d):
    pivo = (e + d)//2 #se usar apenas / será float, como a intenção é ser int então usar // 
    print(f"Valor de pivo: {pivo}")
    if(x == list[pivo]):
      print(f"retorna pivo: {list[pivo]}")
      return pivo
    elif(x < list[pivo]):
      print(f"Valor que está em list[pivo]: {list[pivo]}")
      print("retorna a função busca com parâmetros e, pivo -1, x, list")
      return busca(e, pivo -1, x, list)
    else:
      print(f"Valor que está em list[pivo]: {list[pivo]}")
      print("retorna a função busca com parâmetros pivo + 1, d, x, list")
      return busca(pivo + 1, d, x, list)
  print("Retorna -1")
  return -1

lista = [0, 1, 3, 6, 8, 10, 12, 15, 20, 26, 30, 44, 66, 80]
print(f"Tamanho da lista: {len(lista)}")
alvo = 1
esquerda = 10
#direita = tamanho(lista)-1
direita = len(lista)-1
busca(esquerda, direita, alvo, lista)


#questões 7, 8 e 9
print("Questões 7, 8 e 9")
q789lista = [29, 72, 98, 13, 87, 66, 52, 51, 36]
tamanho_lista = len(q789lista)

for valor_i in range((len(q789lista))-1):
  min = valor_i
  for (valor_j = valor_i+1) in range(len(q789lista)):
    if q789lista[valor_j] < q789lista[min]:
      q789lista[min] < q789lista[valor_i]
  if (valor_1 != min):
    troca = q789lista[valor_i]
    q789lista[valor_i] = q789lista[min]
    q789lista[min] = troca

