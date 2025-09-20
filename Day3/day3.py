print("welcome to the treasure island")
print("your mission is to find the trasure")

task= input('you are at a cross road where do you want to go? type "left" or "right": ')

if task == "left":
    next= input('you came to a lake there is an island in the middle of the lake type "wait" to wait for a boat or "swim" to swim across: ')
    if next== "wait":
        result = input('you got to an house unharmed there are 3 colored doors type "red", "yellow", "blue" to pick a door: ')
        if result == "Yellow":
            print("you win")
        else:
            print("the colour doesn't ")
    else:
        print("Game Over")
else:
    print("Game Over")