import math

rRoot = 1.324717957


def func(x):
    return x**3-x-1


def muller():
    x2 = 1
    x0 = 1.5
    x1 = 2
    error = .00005
    count = 1
    while(count > 0):
        f2 = func(x2)
        f0 = func(x0)
        f1 = func(x1)
        h1 = x1-x0
        h2 = x0-x2
        gama = h2/h1
        c = f0
        a = ((gama*f1)-(f0*(1+gama))+f2)/(gama*(h1**2)*(1+gama))
        b = (f1-f0-(a*(h1**2)))/h1
        if(b > 0):
            signbit = 1
        else:
            signbit = -1
        abcd = (b**2)-(4*a*c)
        efgh = math.sqrt(abcd)
        ans = x0-(2*c/(b+(signbit*(efgh))))
        pError = abs((ans-x0)/ans)*100
        if((pError == 0) or (pError < abs(error))):
            root = ans
            print("Root = ", root, " ", "Count = ", count)
            break
        elif(ans > x0):
            x2 = x0
            x0 = ans
        else:
            x1 = x0
            x0 = ans
        count = count+1


muller()
