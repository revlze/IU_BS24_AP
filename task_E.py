L, R = map(int, input().split())
n = int(input())
d = list(map(int, input().split()))

pref_sum = [0] * (n+1)
for i in range(1, n+1):
  pref_sum[i] = pref_sum[i-1] + d[i-1]
l, r = 0,1
while l < n + 1 and r < n + 1:
  s = pref_sum[r] - pref_sum[l]
  if l >= r:
    r += 1
    continue
  elif s > R:
    l += 1
  elif s < L:
    r += 1
  else:
    print(pref_sum[l], pref_sum[r])
    exit()
print(-1, -1)
