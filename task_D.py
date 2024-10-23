n = int(input())
a = list(map(int, input().split()))

ansP, ans0, M, cnt1, cnt2, pos = 0, 0, 0, 0, 0, -1
for i in range(n):
  if a[i] == 0:pos = i
  if pos != -1: ans0 += pos + 1
for i in range(n):
  if a[i] == 0:
    cnt1, cnt2, M = 0, 0, 0
    continue
  if M % 2 == 0:cnt1 += 1
  else:cnt2 += 1
  if a[i] < 0: M += 1
  if M % 2 == 0:ansP += cnt1
  else:ansP += cnt2
print((n * n + n) // 2 - ans0 - ansP, ans0, ansP)
