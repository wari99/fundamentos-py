#Faça um programa que leia cinco pares de valores (a,b), todos inteiros e positivos , um da cada vez. Mostre os números inteiros pares de a até b (inclusive).

i = 1
a = b = j = 0

for i in range(i, 6):
  a = int(input("%d. a: " % i))  
  b = int(input("%d. b: " % i))
  
  for j in range(a, b+1):
    if(j % 2 == 0):
      print(j)
      
  print("----------")
