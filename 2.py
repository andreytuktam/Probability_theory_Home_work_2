from math import factorial
l = 5000 * 0.0004
m = 0
e = 2.718
p1 = (l ** m / factorial(m)) * e ** (-l)
print("p1 =", p1)

m = 2
p2 = (l ** m / factorial(m)) * e ** (-l)
print("p2 =", p2)
