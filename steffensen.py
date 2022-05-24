def fx(x):
    return x*x*x-x-1


a = int(input("lower value: "))
b = int(input("higher value: "))
c = (a+b)/2
acc = 0.0001
i = 1

if(a < b and fx(a)*fx(b) < 0):
    while(1):
        y = fx(c)
        x1 = c-((y*y)/(fx(c+y)-y))
        print(i, x1)
        if(abs(fx(x1) <= acc)):
            print('Root: ', x1)
            break
        elif(i == 100):
            print('Root: ', x1)
            break
        else:
            c = x1
            i += 1
else:
    print("invalid values of a and b")
