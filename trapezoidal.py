def f(x):
    return 1/(1+x*x)


a = float(input("lower value: "))
b = float(input("higher value: "))
n = int(input("step: "))

h = (b-a)/n
ans = f(a)+f(b)
i = a+h


while(i <= (b-h)):
    ans += (2*f(i))
    i += h

ans = ans*(h/2)
print("Area: ", ans)
