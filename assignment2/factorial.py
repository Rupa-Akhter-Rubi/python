#12. Write a program that calculates the factorial of a number.
num=int(input("enter any positive   number: "))
fact=1
for i in range (1,num+1,1):
    fact=fact*i
print("The factorial of",num,"is  : ",fact)
