#1. Write a program that swaps the values of two variables.
a=int(input("Enter  1st value : "))
b=int(input("Enter 2nd value : "))

a,b=b,a
print("\n After swap : \nfirst value = ",a)
print("\n second value : ",b)