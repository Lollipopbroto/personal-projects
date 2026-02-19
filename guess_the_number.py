# A small guess the number game that will give the player higher/lower and hot/cold clues
import random

# Gets the random number and gives the player's first guess
rand_num = random.randint(1, 100)
attempts = 0
guesses = 5

print("WELCOME to Higher or Lower!!!")
guess = int(input("Guess a number from 1 to 100. You have " + str(guesses) + " guesses: "))
attempts += 1

# Allows player to guess a number until they guess the correct one
while guess != rand_num and guesses != 0:
	if guess < rand_num:
		print("too low!")
	else:
		print("too high!")

	# Determines and displays how close the user is to the actual number
	if abs(guess - rand_num) >= 80:
		print("You're freezing!")
	elif abs(guess - rand_num) >= 55 and abs(guess - rand_num) > 80:
		print("You're ice cold!")
	elif abs(guess - rand_num) >= 25 and abs(guess - rand_num) < 55:
		print("You're cold!")
	elif abs(guess - rand_num) >= 10 and abs(guess - rand_num) < 25:
		print("You're warm!")
	elif abs(guess - rand_num) >= 5 and abs(guess - rand_num) < 10:
		print("You're hot!")
	elif abs(guess - rand_num) >= 2 and abs(guess - rand_num) < 5:
		print("You're burning!")
	else:
		print("You're in lava!")

	attempts += 1
	guesses -= 1
	print("You have " + str(guesses) + " guesses left")
	print(" ")
	guess = int(input("Guess again: "))

print(" ")

# Congratualtory line & Failure line
if guesses != 0:
	print("You guessed the number!")
	print ("It took you " + str(attempts) + " guesses.")
else:
	print("You ran out of guesses :(")

print(" ")

input("Press Enter to terminate...")
