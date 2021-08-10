import random
loop = "y"
while loop.lower() == "y":
    top = input("Enter a number great than 0: ")
    print()
    if top.isdigit():
        top = int(top)
        if top <= 0:
            print("Please enter a larger number.")
            print()
            continue

    else:
        print("That is not a number.")
        print()
        continue
    random_num = random.randint(1,top)
    while True:
        guess = input("Guess a number from (1 - " + str(top) + "): ")
        if guess.isdigit():
            guess = int(guess)
            if guess > top:
                print("Your guess was out of the range of possibility.")
                continue
            elif guess < 1:
                print("Your guess was out of the range of possibility.")
                continue
        else:
            print("This is not a number.")
        if guess != random_num:
            if guess > random_num:
                print("TOO HIGH.")
                print()
                continue
            elif guess < random_num:
                print("TOO LOW")
                print()
                continue
        else:
            print()
            print("****************************************")
            print("You guessed the number! Congratulations!")
            print("****************************************")
            print()

            break
    loop = input("Would you like to play again? (Y or N): ")
    print()