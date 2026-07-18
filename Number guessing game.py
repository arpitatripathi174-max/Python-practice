import random

number = random.randint(1, 10)
print("random no is",number)

while True:
    guess = int(input("Guess a number between 1 to 10: "))

    if guess == number:
        print("Congratulations!,you have guessed the correct no")
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high")
