rRoot=1.324717957
a=1
b=2
error=.00005

def func(x):
    return x**3-x-1

def inverseFunc1(x):
    return 3*(x**2)-1

def inverseFunc2(x):
    return 6*x

def halleys():
    count=1    
    c=(a+b)/2
    while(count>0):
        d=func(c)
        e=inverseFunc1(c)
        f=inverseFunc2(c)
        g=c-((2*d*e)/((2*(e**2))-(d*f)))
        if((func(g)==0)or (abs(func(g))<abs(error))):
            root=g
            print("Root = ", root," ", "Count = ", count)
            break
        else:
            c=g
        count=count+1

halleys()