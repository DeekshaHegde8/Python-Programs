import cal
fname=input("Enter Your First Name: ")
lname=input("Enter Your Last Name: ")
sal2=cal.take_salary()
hra2=cal.hra()
da2=cal.da()
bonus2=cal.bonus()
print("Your basic salary: ",sal2)
print("Your HRA: ",hra2)
print("Your DA: ",da2)
print("Your bonus: ",bonus2)
print("Total salary: ",sal2+hra2+da2+bonus2)