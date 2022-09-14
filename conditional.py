n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))
if n1>n2 and n1>n3:
    print("n1 is the greatest")
elif n2>n1 and n2>n3:
    print("n2 is the largest")
elif n1==n2 and n2==n3 and n3==n1:
    print("All Numbers Are Identical")
else:
    print("n3 is the largest")