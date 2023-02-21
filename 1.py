from math import factorial
n = 100
k = 85
p = 0.8
q = 0.2

a = factorial(n) / (factorial(k) * factorial(n - k))
p = a * p ** k * q ** (n - k)
print("p =", p)