import random

word_list= ["jesus", "car", "jae5", "prime", "baboon", "bobo", "adekunle", "gold", "neymar", "kdb"]

wya= random.choice(word_list)
length= len(wya)
print(f"the guessed word is {wya}")

list=[]
for i in range(length):
    list += "_"

end= False 
while not end:
    result= input("Guess a letter in the word: ").lower()

    for position in range(length):
        letter= wya[position]
        print(f"current position: {position}\n current lettter: {letter}\n guessed letter: {result}")

        if letter== result:
            list[position]= letter

    print(list)



