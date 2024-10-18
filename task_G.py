def bin_search(a,x):
  l, r = -1, len(a)
  while l < r-1:
    m = (l+r)//2
    if x < a[m]:
      r = m
    else:
      l = m
  if len(a) == r:
    return a[l]
  if abs(a[l]-x) == abs(a[r]-x):
    return a[l]
  return a[l] if abs(a[l]-x) < abs(a[r]-x) else a[r]
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in b:
  print(bin_search(a, i))