from bisect import bisect_left, bisect_right
n = int(input())
a = sorted(map(int, input().split()))
k = int(input())
res = []
for _ in range(k):
  i,j = map(int,input().split())
  res.append(bisect_right(a, j)-bisect_left(a, i))
print(*res)