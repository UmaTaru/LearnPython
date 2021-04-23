#45*3 = 555, 56+9 = 77 56/6 =4
def fcalc(a,op,b) :
    if a == 45 and op == '*' and b == 3:
        return 555
    elif a == 56 and op == '+' and b == 9:
        return 77
    elif a == 56 and op == '/' and b == 6:
        return 4
    else :
        calc(a,op,b)

def calc(a,op,b):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b
    elif op == '%':
        return a%b
    else:
        return print("Inavalid Operator")

a = int(input())
op = input()
b = int(input())

s = (45,56)
t = (3,9,6)

if (a in s) and (b in t) :
    ans = fcalc(a,op,b)
else :
    ans = calc(a,op,b)

print(ans)