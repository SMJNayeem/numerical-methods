def fx(x):
    return x*x*x*x-x-1

def fxx(x):
    return 4*x*x*x-1

a=-0.75
b=1.25
c=(a+b)/2
acc=0.0001
i=1

print(fx(a)*fx(b))

if(a<b and (fx(a)*fx(b))<0):
    while(1):
        x1=abs(c-(fx(c)/fxx(c)))
        print(i,x1)
        if(fx(x1)==0 or fx(x1)<=acc):
            print("Answer: ",x1)
            break
        elif(i==100):
            print(x1)
            break
        else:
            c=x1
            i+=1
else:
    print("invalid values of a and b")
