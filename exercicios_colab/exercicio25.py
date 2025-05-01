n = int(input('Quantos números da sequência de Fibonacci você quer ver? '))

a, b = 0, 1
for x in range(0,n):
  print(a)
  a, b = b, a +b