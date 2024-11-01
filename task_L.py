import itertools

n = int(input())
lst = [''.join(p) for p in itertools.product('01', repeat=n) if '11' not in ''.join(p)]
print(len(lst))
for p in lst:
  print(p)
