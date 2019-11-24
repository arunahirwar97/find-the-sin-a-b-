print ("Find the value of sin(a+b)")
from math import sin,cos
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

c = sin(a)*cos(b)+cos(a)*sin(b)
print("The value of sin(a+b): = ",c)
