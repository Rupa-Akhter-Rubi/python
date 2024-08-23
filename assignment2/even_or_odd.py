num=int(input("enter the positive number: "))
if num <= 0:
    print("Please,enter the positive value.")
elif num % 2 == 0:
    print("the number is even.")
else:
    print("The number is odd.")