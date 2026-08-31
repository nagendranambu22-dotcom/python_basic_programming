#simple calucalator
print("------------- calculator -------------")
a=float(input("Enter the first Number : "))
b=float(input("Enter the second Number : "))
choice=input("choice symbol (+,-,*,%) : ")
if choice == '+':
    print("addition : ",a+b)
elif choice == '-':
    print("subration : ",a-b)
elif choice == '*':
    print("multipication : ",a*b)
elif choice == '%':
    print("division : ",a/b)
else:
    print("invalid symbol")

