"""Ternary Search for find max point."""
EPSILON = 0.0001
def tern(a, b):
  # within episilon, return midpoint
  if abs(f(a) - f(b)) < EPSILON:
    return (a + b) / 2.0
  
  m1 = a + (b - a) / 3.0
  m2 = a + (b - 2) * 2.0 / 3.0
  
  # in range of m1 - b
  if f(m1) < f(m2):
    return tern(m1, b)
  # in range a - m2
  return tern(a, m2)