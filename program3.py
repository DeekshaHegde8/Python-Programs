c=0
while c!=7:
    fname = input("Enter Your Name: ")
    c=c+1
    if(len(fname) >0 and fname.isalpha()):
        lname=input("Enter your surname: ")
        c=c+1
        if(len(lname)>0 and lname.isalpha()):
            phone=input("Enter contact number: ")
            c=c+1
            if(len(phone)>0):
                if(len(phone)>9 and phone.isnumeric()):
                    age=int(input("Enter your age: "))
                    c=c+1
                    if(age>=20 and age<=101):
                            city=input("Enter your city: ")
                            c=c+1
                            if(len(city)>0):
                                salary=int(input("Enter your salary: "))
                                c=c+1
                                if( salary>0):
                                    dep=input("Enter department name: ")
                                    c=c+1
                                    if(len(dep)>0):
                                            print("Name: ",fname)
                                            print("Surname: ",lname)
                                            print("phone : ",phone)
                                            print("age : ",age)
                                            print("city: ",city)
                                            print("salary: ",salary)
                                            print("dep. name: ",dep)
                                            break
                                    else:
                                        print("Enter valid department name")
                                else:
                                    print("Enter valid salary amount")
                                    
                            else:
                                print("Enter valid city")
                                
                    else:
                            print("Enter valid age")
                            
                    

                else:
                    print("Enter valid phone")
                    
            else:
                print("Enter valid phone")
                
        else:
            print("Enter valid surname")
            
    else:
        print("Enter Valid name")
        
