def f(x, y):
    return x*x+y


x0 = float(input('x0='))
y0 = float(input('y0='))
xn = float(input('xn='))
h = float(input('h='))
n = int(xn/h)

for i in range(n):
    y1 = y0+(h*f(x0, y0))
    yn = y0+((h/2)*(f(x0, y0)+f(xn, y1)))
    print(i, yn)
    y0 = y1
    x0 = x0+h

print("value of y is "+str(yn)+" at x= "+str(xn))
