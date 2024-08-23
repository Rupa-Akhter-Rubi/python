#8. Write a program that determines if a year is a leap year or not.

year=int(input("enter the year: "))
if year %4==0:
    print("Leap year.")
elif year %100==0:
    print("Leap year.")
elif year % 400==0:
    print("Leap year.")

else:
    print("Not leap year.")