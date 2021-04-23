def prime(n):
    count = 0
    for i in range(2,n-1):
        if n % i == 0:
            count += 1
    if count > 0:
        print("Not a prime number ")
    else:
        print("Prime number !")

def prime_in_interval(a,b) :
    num = []
    for i in range(a,b+1):
        if i > 1:
            for j in range(2,i):
                if i % j == 0:
                    break
            else :
                num.append(i)
    print(num)

#prime(15)
prime_in_interval(1,160)