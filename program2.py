print("Please Fill Below Details\n")
fname = input("Enter Your Name: ")
if(len(fname) >0 and fname.isalpha() ):
    email=input("Enter your email: ")
    if(len(email)>0):
        address=input("Enter your address: ")
        if(len(address)>0):
            phone=input("Enter your contact number: ")
            if(len(phone)>0):
                if(len(phone)==10 and phone.isnumeric()):
                    age=int(input("Enter Your Age: "))
                    if(age>=20):
                        salary=int(input("Enter your salary: "))
                        if(salary>0):
                            dependents=input("Enter number of dependents: ")
                            print("\n-----Employee Details-----")
                            print("Employee Name: ",fname)
                            print("Employee age: ",age)
                            print("Employee Contact Number: ",phone)
                            print("Employee Email id: ",email)
                            print("Employee Address: ",address)
                            print("Employee Salary: ",salary)
                            print("No. of people depending on employee: ",dependents)

                        else:
                            print("Enter valid amount")
                    else:
                        print("Enter valid age")
                else:
                    print("Enter valid phone")
            else:
                print("Enter valid phone")


        else:
            print("Please Enter valid address")

    else:
        print("Please Enter valid email")
        
else:
    print("Please Enter valid name")





