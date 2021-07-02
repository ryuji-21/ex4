import random
name = input("Please write your name ->")
print("Hello,",name,"!")
print("Rolling the dice...")
Die1 = random.randint(1,6)
Die2 = random.randint(1,6)
A = Die1 + Die2
print("Die 1:",Die1)
print("Die 2:",Die2)
print("Total value:",A)

if(A >= 7):
    print(name,"won!")
else:
    print(name,"lose...")