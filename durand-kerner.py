def func(x):
    return x*x*x*x-x-1


initial = [1, -1, complex(0, 1), complex(0, -1)]
initialUpdate = [None]*len(initial)
breakValue = 0

for i in range(10):
    for j in range(len(initial)):
        total = 1
        for k in range(len(initial)):
            if(j == k):
                continue
            dif = initial[j]-initial[k]
            total = total*dif
        initialUpdate[j] = initial[j]-(func(initial[j])/total)

    for i in range(len(initial)):
        if(initial[i].real == initialUpdate[i].real):
            breakValue = 1
            break
    if(breakValue == 1):
        break

    for i in range(len(initial)):
        if(abs(initialUpdate[i].imag) < (10**-10)):
            initial[i] = initialUpdate[i].real
        else:
            initial[i] = initialUpdate[i]
    print(initial)
