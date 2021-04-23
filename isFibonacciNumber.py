import math
#A number is Fibonacci if and only if one or both of (5*n^2 + 4) or (5*n^2 – 4) is a perfect square
n = int(input("Enter a number to check if it is a fibonacci number : "))
a = 5*n*n + 4
b = 5*n*n - 4
c = math.sqrt(a)
d = math.sqrt(b)


if c.is_integer() or d.is_integer():
    print("Fibonacci Number ")
else :
    print("Not a Fibonacci number ")