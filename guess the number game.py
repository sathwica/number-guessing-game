import random  
import time  

def intro():
    print("Welcome to the Guessing Game!")
    print("------------------------------")
    name = input("May I ask you for your name? ")
    print("\nHello, " + name + "! Let's play a game.")
    print("I am thinking of a number between 1 and 200.")
    time.sleep(1)
    print("Take a guess and see if you can guess it!")

def pick():
    number = random.randint(1, 200)  # Randomly select a number between 1 and 200
    guessesTaken = 0  # Initialize the number of guesses taken

    while guessesTaken < 6:  # Allow up to 6 guesses
        time.sleep(0.5)
        guess = input("\nEnter your guess: ")

        try:
            guess = int(guess)  # Convert the guess to an integer

            if 1 <= guess <= 200:  # Check if the guess is within the valid range
                guessesTaken += 1

                if guess < number:
                    print("Too low! Try a higher number.")
                elif guess > number:
                    print("Too high! Try a lower number.")
                else:
                    break  # Correct guess, exit the loop

                if guessesTaken < 6:
                    print("You have " + str(6 - guessesTaken) + " guesses left.")
            else:
                print("Oops! Please enter a number between 1 and 200.")
        except ValueError:
            print("Oops! That doesn't look like a number.")

    if guess == number:
        print("\nCongratulations, " + name + "!")
        print("You guessed my number in " + str(guessesTaken) + " guesses!")
    else:
        print("\nSorry, you've run out of guesses!")
        print("The number I was thinking of was:", number)

play_again = "yes"  # Initialize the play again variable

while play_again.lower() in ["yes", "y"]:  # Allow the player to play multiple times
    intro()  # Start the game
    pick()  # Play the game
    play_again = input("\nDo you want to play again? (yes/no): ")  # Prompt to play again
