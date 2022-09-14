num=100
name=input("Enter your name: ")
days=int(input("Enter Number of class you have attended: "))
min=75
attended=(days/num)*100
print("Your percentage: ",attended)
if attended>75:
    print("You have eligibility")
else:
    print("You don't have eligibility")
