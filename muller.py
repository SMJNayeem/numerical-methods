import math


def f(x):
    return x**3-x-1


x0 = int(input("lower value: "))
x1 = int(input("higher value: "))
x2 = (x0+x1)/2
error = .01
count = 1
while(count > 0):
    h1 = x1-x0
    h2 = x2-x1
    delta1 = (f(x1)-f(x0))/h1
    delta2 = (f(x2)-f(x1))/h2
    gama = h2/h1
    c = f(x2)
    a = (delta2-delta1)/(h1+h2)
    b = (a*h2)+delta2
    if(b > 0):
        signbit = 1
    else:
        signbit = -1
    det = (b**2)-(4*a*c)
    rdet = math.sqrt(det)
    ans = x2-(2*c/(b+(signbit*(rdet))))
    pError = abs((ans-x2)/ans)*100
    print(count, ans)
    if((pError == 0) or (pError < abs(error))):
        print("Root: ", ans)
        break
    else:
        x0 = x1
        x1 = x2
        x2 = ans

    count += 1
