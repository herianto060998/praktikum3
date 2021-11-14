import random
n = int(input("masukkan nilai;"))
a = 0

for c in range (n):
   a+= 1
   b = random.uniform(.0,.5)
   print('data ke:', a, '==>', b)