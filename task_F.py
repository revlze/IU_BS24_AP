def InvCount(l: int, r: int) -> int:
  if r <= l + 1:
    return 0
  m = (l + r) // 2
  count = InvCount(l, m) + InvCount(m, r)
  i, j, k = l, m, l
  while i < m and j < r:
    if a[i] <= a[j]:
      t[k] = a[i]
      i += 1
    else:
      t[k] = a[j]
      count += m - i
      j += 1
    k += 1
  a[l:r] = t[l:k] + a[i:m] + a[j:r]
  return count

n = int(input())
a = list(map(int, input().split()))
t = [0] * n
print(InvCount(0, n))