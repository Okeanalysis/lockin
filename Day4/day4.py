import random
names= input("Give me the name of the people: ")

name= names.split(',')
num= len(name)


randoms= random.randint(0, num-1)
pay= name[randoms]
print(f"{pay} is paying for the food")