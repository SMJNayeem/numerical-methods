appval = float(input("approximate value: "))
trueval = float(input("true value: "))

abserr = trueval-appval
print("Absolute error = ", abserr)
print("Relative error = ", abserr/trueval)
print("Percentage error = ", 100*(abserr/trueval))
