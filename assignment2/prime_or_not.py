#14. Write a program that checks if a given number is prime or not.
num=int(input("enter any positive   number: "))
for i in range(2,num):
    if num% i ==0:
        print("Not Prime.")
        break
else:
        print("\nprime")