def fx(x):
    return x*x*x-x-1


a = int(input("lower value: "))
b = int(input("higher value: "))
acc = 0.0001
i = 1

if(a < b and fx(a)*fx(b) < 0):
    while(1):
        c = a-(fx(a)*((b-a)/(fx(b)-fx(a))))
        print(i)
        if(abs(fx(c)) <= acc):
            print('Root: ', c)
            break
        elif(i == 100):
            print('Root: ', c)
            break
        else:
            a = b
            b = c
            i += 1
else:
    print("invalid values of a and b")
