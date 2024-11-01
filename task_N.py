import itertools as it

n,k = map(int, input().split())
for i in it.combinations(range(1,n+1), r=k):
  print(*i)
