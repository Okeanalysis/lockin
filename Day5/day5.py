import random
alp= ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num= ['0','1', '2', '3', '4', '5', '6', '7', '9']
symbol= ['!', '@', '#', '$', '%', '^', '&', '*', '()', ')']
print("Welcome to the pypassword generator")
num1 = int(input("How many alphabet do you wnat in your password: "))
alpha= int(input("how many symbols do you want in your password: "))
sym=int(input("how many numbers do you want in your password: "))


password_list= []

for n in range(1, num1+1):
    password_list.append(random.choice(alp))
for n in range(1, alpha+1):
    password_list.append(random.choice(symbol))
for n in range(1, sym+1):
    password_list.append(random.choice(num))

random.shuffle(password_list)

password=""

for char in password_list:
    password+=char

print(f"your passowrd is: {password}")