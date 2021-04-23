def fiboR(n):
    f = [0,1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        for i in range(2,n+1):
            a = f[i-1] + f[i-2]
            f.append(a)
    #print(f[n])
    print("Iterative  ",f)

def fiboI(n):
    fI = []
    a,b = 0,1
    for i in range(0,n):
        a,b = b,(a+b)
        fI.append(a)
    #print(a)
    print("Recursive  ",fI)

#fibonacci using arrays
def fiboArray(n):
    a = [0] * (n+1)
    a[1] = 1
    for i in range(2,n+1):
        a[i] = a[i-1] + a[i-2]
    print("Array  ",a)

fiboR(9)
fiboI(9)
fiboArray(9)
x = int(input("Enter a number to check if it is a fibonacci number : "))
n = x
a = (0,1)
while i <= n:
    for j in range(0,i):
        a[j] = a[j-1] + a[j-2]
        

