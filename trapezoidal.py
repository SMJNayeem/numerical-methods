def f(x):
    return 1/(1+x*x)


a = float(input("lower value: "))
b = float(input("higher value: "))
n = int(input("step: "))

h = (b-a)/n
ans = f(a)+f(n)
ans = 0

for i in range(1, n, 1):
    xx = a+i*h
    ans += (2*f(xx))

ans = ans*(h/2)
print("Area: ", ans)
