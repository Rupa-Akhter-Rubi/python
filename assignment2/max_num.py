#7.Write a program that finds the maximum of three numbers.
a=int(input("Enter the 1st value : "))
b=int(input("Enter the second value: "))
c=int(input("Enter the 3rd value: "))
if a>b and a>c:
    print("the max number is ",a)
elif b>a and b>c:
    print("the maximum number is : ",b)
else:
    print("The maximum number is : ",c)