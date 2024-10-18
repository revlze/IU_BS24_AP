def sort(a, n):
  t = [0] * n
  def sum_string(a):
    return sum(map(int, str(a)))
  def merge(l, h):
    if h <= l + 1 :
      return a
    m = (l + h) // 2
    merge(l, m)
    merge(m, h)
    i, k, j = l, l, m
    while i < m and j < h:
      if sum_string(a[i]) < sum_string(a[j]):
        t[k] = a[i]
        i += 1
      elif sum_string(a[i]) == sum_string(a[j]) and a[i] <= a[j]:
        t[k] = a[i]
        i += 1
      else:
        t[k] = a[j]
        j += 1
      k += 1
    a[l:h] = t[l:k] + a[i:m] + a[j:h]
    return a
  return merge(0, n)

n = int(input())
a = list(map(int,input().split()))
print(*sort(a, n))
