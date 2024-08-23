#17. Write a program that reverses a given number.
num=int(input("enter the number: "))
temp=num
sum=0
while temp !=0:
    rem=temp%10  #rem =reminder
    sum=sum*10+rem
    temp=temp //10
print(" Reverse of number ",sum)