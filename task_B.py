n = int(input())
k = 1
a = int(input())
if n == 1:
  print(1, a)
for i in range(n-1):
  b = int(input())
  if a == b: k += 1
  else: print(k, a); k = 1
  if i == n-2: print(k, b)
  a = b