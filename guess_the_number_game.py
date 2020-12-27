import random
number = random.randint(1,10)
for i in range(0, 3):
    user = int(input("guess the number"))
    if user == number:
        print("hurry!!")
        print(f"you guessed the number right it's{number}")
        break
if user != number:
    print(f"your guess is incorrect the numbe ris {number}")