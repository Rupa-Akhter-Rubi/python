#18. Write a program that checks if a given string, is a palindrome.
num=int(input("enter the number: "))
temp=num
sum=0
while temp !=0:
    rem=temp%10  #rem =reminder
    sum=sum*10+rem
    temp=temp //10
print(" Reverse of number ",sum)
if num==sum:
    print("It's Palindrome number.")
else:
    print("It's not Palindrome number")