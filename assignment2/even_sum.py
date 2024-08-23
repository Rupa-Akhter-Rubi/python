#16. Write a program that finds the sum of all even numbers between 1 and `n`.
n=int(input("enter the n number: "))
i=0
sum=0
while i<=n:
    sum+=i
    i=i+2
print("Sum even number between 1 and ",n,"= ",sum)