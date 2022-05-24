def f(x, y):
    return x+y


x0 = float(input('x0='))
y0 = float(input('y0='))
xn = float(input('xn='))
n = int(input('n='))

h = (xn-x0)/n

for i in range(0, n, 1):
    yn = y0+(h*f(x0, y0))
    print(x0, y0, f(x0, y0), yn)
    y0 = yn
    x0 = x0+h

print("value of y is "+str(yn)+" at x= "+str(xn))
