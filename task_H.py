def f(x, C):
  return x**2 + x ** 0.5 - C

def binary_approximation(C):

  l, h = 0, C ** 0.5
  eps = 1e-7
  while h - l > eps:
    m = (l + h) / 2
    if f(m, C) < 0:
      l = m
    else:
      h = m
  return round(l, 6)
print(binary_approximation(float(input())))