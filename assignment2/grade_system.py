#10. Write a program that calculates the grade based on a given percentage.

marks=int(input("Enter percentage :"))
if marks>100 | marks<0:
    print("Invalid marks.")
elif marks>=80 and marks<=100:
    print("A+")
elif marks>=70 and marks<=79:
    print("A")
elif marks>=60 and marks<=69:
    print("B")
elif marks>=50 and marks<=59:
    print("C")
elif marks>=40 and marks<=49:
    print("D")
else:
    print("F")