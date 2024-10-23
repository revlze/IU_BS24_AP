m,n = map(int, input().split())
a = list(map(int, input().split()))
ps = [0]*(m+1)
for i in range(m):
  ps[i+1] = ps[i] + a[i]
for i in range(n):
  l,r=map(int, input().split())
  print(ps[r+1] - ps[l])