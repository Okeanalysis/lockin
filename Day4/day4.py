import random
user= int(input("what do you choose type 0 for rock, 1 for paper, 2 for scissors: "))

computer= random.randint(0,2)
print(f"Computer choice is {computer}")

if user >=3 and user<0:
    print("you lose invalid number")
elif user == 0 and computer ==2 :
    print("you win")
elif computer== 0 and user ==2:
    print("you lose")
elif computer>user:
    print("you lose")
elif computer==user:
    print("its a draw")
elif user>computer:
    print("you win")