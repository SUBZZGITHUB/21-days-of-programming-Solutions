
import cmath
a=int(input("enter the coff. a"))
b=int(input("enter the coff. b"))
c=int(input("enter the coff. c"))
d=(b**2)-(4*a*c)
root1 = (-b - cmath.sqrt(d)) / (2 * a)
root2 = (-b + cmath.sqrt(d)) / (2 * a)
print(d)
print(root1)
print(root2)
