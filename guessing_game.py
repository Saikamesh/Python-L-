import random

secret_number = random.randint(0, 9)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    user_guess = int(input("Enter Your Guess : "))
    guess_count += 1
    if user_guess == secret_number:
        print("Congrats! You Won.")
        break
else:
    print("ouch!! You are out of guesses")
    print("Better luck next time")
    print("The answer is {}".format(secret_number))
