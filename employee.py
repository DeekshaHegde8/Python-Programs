sal=int(input("Enter your salary: "))
exp=int(input("Enter your no. of experience: "))
if exp>=10:
    print("Your bonus ammount: ",(15/100) * sal)
    print("Your total salary: ",sal+((15/100) * sal))
elif exp>=5 and exp<10:
    print("Your bonus ammount: ",(10/100) * sal)
    print("Your total salary: ",sal+((10/100) * sal))
elif exp>=3 and exp<5:
    print("Your bonus ammount: ",(5/100) * sal)
    print("Your total salary: ",sal+((5/100) * sal))
else:
    print("You are not eligible for bonus")
