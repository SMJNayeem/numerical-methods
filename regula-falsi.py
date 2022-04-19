def fx(x):
    return x*x*x-x-1

a=1
b=2
acc=0.0001
i=1

if(a<b and fx(a)*fx(b)<0):
    while(1):
        c=a-(fx(a)*((b-a)/(fx(b)-fx(a))))
        print(i)
        if(abs(fx(c))<=acc):
            print(c)
            break
        elif(fx(a)*fx(c)<0):
            b=c
            i+=1
        elif(i==100):
            print(c)
            break
        else:
            a=c
            i+=1
else:
    print("invalid values of a and b")
