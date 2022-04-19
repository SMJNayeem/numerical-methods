def f(x):
    return x*x*x-x-1


def g(x):
    return (1+x)**(1/3)


a = 1
b = 2
c = (a+b)/2
acc = 0.0001
i = 1

if(a < b and f(a)*f(b) < 0):
    while(1):
        x = g(c)
        print(i)
        if(abs(x-c) <= acc):
            print(x)
            break
        elif(i == 100):
            print(x)
            break
        else:
            c = x
            i += 1
else:
    print("invalid values of a and b")
