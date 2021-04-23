def armstrong(n):
    sum = 0
    y = n
    while y > 0:
        x = y % 10
        sum = sum + pow(x,n)
        y = y // 10
    if sum == n :
        print("Armstrong number")
    else :
        print("Not a armstrong number ")

def order(n):
    x = n
    digits = 0
    while x > 0:
        x = x // 10
        digits += 1
    return digits

def pow(x,n):
    n = order(n)
    z = 1
    while n > 0 :
        z = z * x
        n = n - 1
    return z


armstrong(157)
armstrong(1634)