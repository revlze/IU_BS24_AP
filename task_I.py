def isHeap(n, a):
  i = 0
  while 2 * i + 1 < n:
    if 2 * i + 2 < n:
      if a[i] > a[2 * i + 2]:
        return "NO"
    if 2 * i + 1 < n:
      if a[i] > a[2 * i + 1]:
        return "NO"
    i += 1
  return "YES"
n = int(input())
a = list(map(int, input().split()))
print(isHeap(n, a))

