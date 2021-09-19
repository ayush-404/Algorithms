def gcd(a, b):
  while b != 0:
    a = a%b
    temp = b
    b = a
    a = temp

  return a


