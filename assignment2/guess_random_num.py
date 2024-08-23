#19. Write a program that generates a random number and allows the user to guess it.

import random
num=random.randrange(1,50)# computer generate a random rumber
user=int(input("guess number:"))#user guess
if num>user:
    print("It's not Correct.\n The correct number is ",num)
elif num<user:
    print("It's not Correct.\n The correct number is ", num)
else:
    print("Your guess is Correct.")