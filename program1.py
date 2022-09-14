from datetime import date
todays_date = date.today()
print("Please Fill Below Details\n")
fname = input("Enter Your First Name: ")
sname = input("Enter your Last Name: ")
dob=int(input("Enter Your Birth Year: "))
email=input("Enter your email: ")
phone=input("Enter your contact number: ")
address=input("Enter your address: ")
pincode=input("Enter your pincode: ")
job=input("Enter your job name: ")
salary=input("Enter your salary: ")
dependents=input("Enter your no. of dependents: ")

print("\n-----Employee Details-----")

print("Employee Name: ",fname,sname,sep=" ")
print("Employee Birth Year: ",dob)
print("Employee age: ",todays_date.year-dob)
print("Employee Contact Number: ",phone)
print("Employee Email id: ",email)
print("Employee Address: ",address)
print("Employee Pincode: ",pincode)
print("Employee Job Name: ",job)
print("Employee Salary: ",salary)
print("No. of people depending on employee: ",dependents)






