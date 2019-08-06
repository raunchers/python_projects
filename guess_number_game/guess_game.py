# Game to guess a number that is randomly generated between 0 and 20
# Player has 6 tries before the player loses
import random
print("Hello, what is your name?")
playerName = input()
print("Hello, " + playerName + " can you guess which number I am thinking of between 0 and 20?")
print("Be careful, you will only have 6 tries to get the right answer!")
randomNumber = random.randint(0,20)

# Ask for the players guess
for numGuesses in range(0,6):
    print("Take a guess")
    playerGuess = input()

    # If the guess is too low
    if int(playerGuess) < randomNumber:
        print("Your guess is too low.")
    # If the guess is too high
    elif int(playerGuess) > randomNumber:
        print("Your guess is too high")
    # If the guess is correct
    else:
        break

if int(playerGuess) == randomNumber:
    print("Congrats, " + playerName + " you guessed the right number!")
else:
    print("Sorry, the correct number was: " + str(randomNumber))
    
