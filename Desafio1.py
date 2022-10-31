# O número de testes necessários (no pior caso) é precisamente a quantidade de vezes que preciso dividir o vetor por dois até que ele tenha apenas um elemento

count, ntent = 0, 0 #Contador de execuções
k = int(input("Insira o valor de k: "))
n = int(input("Insira o valor de n: "))
helio = list(range(1, n + 1))

q = (len(helio) + 1)//2

while len(helio) > 1 and k > 0:
  helio = helio[:q] #O Vetor recebe o novo vetor dividido
  q = (len(helio) + 1)//2 #Calcula exatamente o meio, arredondando se o tamanho do vetor for ímpar
  print(helio)
  count += 1 #Sempre que executar vai adicionar ao contador
ntent += 1  
print(" ")
print("Entrada\n", n, k, sep = " ")

if n%2 == 0:
  print("Saída\n", count+1)
elif n%2 != 0:
  print("Saída\n", count)
