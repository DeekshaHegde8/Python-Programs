sal1=0
def take_salary():
    global sal1
    print("Enter your basic salary salary: ")
    sal1=int(input())
    return sal1
    

def hra():
    global sal1
    hra1=((10/100)*sal1)
    return hra1
def da():
    global sal1
    da1=((30/100)*sal1)
    return da1
def bonus():
    global sal1
    bonus1=((10/100)*sal1)
    return bonus1
