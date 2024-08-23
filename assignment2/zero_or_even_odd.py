#9. Write a program that determines if a number is positive, negative, or zero.

num=int(input("enter the  number: "))
if num == 0:
    print("The number is Zero.")
elif num % 2 == 0:
    print("the number is even.")
else:
    print("The number is odd.")