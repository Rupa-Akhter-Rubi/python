#20. Write a program that finds the greatest common divisor (GCD) of two numbers.
first_num=int(input("enter the first number: "))
second_num=int(input("enter the Second number: "))
a=first_num
b=second_num
while b !=0:
    rem=a%b
    a=b
    b=rem
gcd=a
print("GCD :: ",gcd )

