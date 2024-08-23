#13. Write a program that generates a Fibonacci sequence of length `n`.
n=int(input("enter any positive   number: "))
first_num=0
second_num=1
sum=0
if n<=0:
    print("please enter positive number.")
else:
    for i in range(0,n):
        print(sum, end=' ')
        first_num=second_num
        second_num=sum
        sum=first_num + second_num
