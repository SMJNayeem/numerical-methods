def f(x):
    return 1/(1+x)


a = float(input("lower value: "))
b = float(input("higher value: "))

h = (b-a)/2
ans = f(a)+f(b)
i = a+h


while(i <= (b-h)):
    ans += (2*f(i))
    i += h

x1 = ans*(h/2)

h /= 2
ans = f(a)+f(b)
i = a+h


while(i <= (b-h)):
    ans += (2*f(i))
    i += h

x2 = ans*(h/2)

h /= 2
ans = f(a)+f(b)
i = a+h


while(i <= (b-h)):
    ans += (2*f(i))
    i += h

x3 = ans*(h/2)

x1 = x2+(x2-x1)/3
x2 = x3+(x3-x2)/3
x1 = x2+(x2-x1)

print("Answer: ", x1)
