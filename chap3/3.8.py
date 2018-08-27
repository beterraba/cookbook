# Calculating with Fractions

from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)
print(a * b)

# Getting numerator / denominator
c = a * b
c.numerator
c.denominator

# Converting to a float
float(c)

# Limiting the denominator of a value
print(c.limit_denominator(8))

# Converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
y