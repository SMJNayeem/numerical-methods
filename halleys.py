def f(x):
    return x*x*x-x-1


def fx(x):
    return 3*(x**2)-1


def fxx(x):
    return 6*x


a = int(input("lower value: "))
b = int(input("higher value: "))
c = (a+b)/2
acc = 0.0001
i = 1


if(a < b and (f(a)*f(b)) < 0):
    while(1):
        x1 = abs(c-((2*f(c)*fx(c))/((2*(fx(c)**2))-(f(c)*fxx(c)))))
        print(i, x1)
        if(fx(x1) == 0 or fx(x1) <= acc):
            print("Root: ", x1)
            break
        elif(i == 100 or c == x1):
            print('Root: ', x1)
            break
        else:
            c = x1
            i += 1
else:
    print("invalid values of a and b")
