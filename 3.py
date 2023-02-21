from math import factorial
n = 144
k = 70
p = 0.5
q = 1 - p
a = factorial(n) / (factorial(k) * factorial(n - k))
p = a * p ** k * q ** (n - k)
print("p =", p)