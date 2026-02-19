# A group of tools made & used entirely for fun
import random

# setup for later
restart = True

# Rock, Paper, Scissors setup
rps_score = 0
rps_streak = 0
rps_high = 0
# Tag setup
tag_monster = False

advice_list = (
	"Fart in class and they'll forget in a few days. Poop and they'll remember it for years to come. Leave a big impact.",
	"It's okay, it's alright. I got something that you gon' like.",
	"When life gives you lemons, trade them for apples and make applejuice, it's better.",
	"If you're too scared to fail, you already have.",
	"Don't look behind you.",
	"You are loved.",
	"Live, Laugh, Love",
	"The floor is lava only if you believe it is.",
	"A silent fart is still a fart. Don’t underestimate quiet power.",
	"Don’t put spaghetti in your pocket. Just… don’t.",
	"Homework is just brain exercise. Flex those noodles.",
	"If you lose the game, you lost the game. (You just lost the game.)",
	"Sleep is free, naps are deluxe DLC.",
	"A broken pencil is pointless.",
	"Don’t lick frozen metal poles.",
	"Take life one nacho at a time.",
	"Even the microwave beeps in victory when it's done. You should too.",
	"Never argue with a goose.",
	"If you want to run fast, don’t wear flip-flops.",
	"The grass is greener where you water it… unless it’s fake.",
	"If you forget what you were gonna say, fart loudly. Everyone will forget you were even gonna say anything at all.",
	"Confidence is 60% posture, 30% deodorant, 10% knowing where the bathroom is.",
	"Don’t bite the hand that fingers you",
	"Even a chicken nugget can dream of being a dinosaur.",
	"The WiFi may be weak, but so are your excuses.",
	"Never trust a goose.",
	"Your GPA isn’t tattooed on your forehead, but your forehead is.",
	"Don’t chase people. Chase ice cream trucks.",
	"Every great idea was once called ‘weird.’",
	"If the shoe fits, wear it. If it doesn’t, maybe it’s not your shoe.",
	"Walk a mile in someone's shoes... Then run a mile because the cops are after you for shoe theft."
	"A fart denied is a fart multiplied.",
	"If the road is closed, make a sidewalk.",
	"Never take criticism from someone who can’t parallel park.",
	"The early bird gets the worm, but the second mouse gets the cheese.",
	"Cereal at night counts as self-care.",
	"Being kind is free. Being mean is just bad manners.",
	"Even your socks deserve respect.",
	"Don’t compare your chapter 1 to someone else’s chapter 20.",
	"Remember: raccoons wash their food before eating. Be like raccoons.",
	"I invented Mondays just to ruin your vibe. #staytoxic",
	"When in doubt, moo loudly.",
	"Pizza backwards is azzip. Remember that."
	"Farts are temporary, but laughter is eternal.",
	"If you spill milk, don’t cry. Just get cookies.",
	"Sometimes the bravest thing you can do is order extra fries.",
	"Toaster strudels are just pop-tarts with a degree.",
	"Stay away from the geese.",
	"DO NOT FEED THE GEESE.",
	"A cactus is a plant with trust issues.",
	"Smile at a stranger today. Unless they look like a goose.",
	"Eat spaghetti to forgetti your regretti.",
	"The best time to nap was 20 minutes ago. The second best time is now.",
	"Always leave them wondering why you smelled like glue.",
	"You don’t have to run fast, just faster than the slowest person near the bear.",
	"Keep your friends close, and your snacks closer.",
	"A fart shared is a friendship strengthened.",
	"Don’t knock on the fridge at midnight. The salad is sleeping.",
	"Respect your teachers. They control the Wi-Fi password of life.",
	"Sometimes success is just microwaving the goose without burning your tongue.",
	"If the elevator is broken, take the stairs. Or just live on that floor now.",
	"A nap a day is all it takes.",
	"If you dance like nobody’s watching, film it and prove it.",
	"Don’t let anyone tell you you can’t juggle bananas.",
	"Confidence is eating tacos on a first date.",
	"If your pen runs out of ink, maybe it’s telling you to stop writing cringe.",
	"Life’s too short to skip sprinkles.",
	"Don’t text your ex. Text your grandma. She misses you.",
	"Even the dishwasher needs a rinse cycle sometimes.",
	"A goose never apologizes. Neither should you (sometimes).",
	"If you don’t have haters, you’re probably not farting loud enough.",
	"The Wi-Fi may disconnect, but friendship is Ethernet.",
	"Don’t worry about making waves. Boats are supposed to rock.",
	"Even socks that don’t match still keep your feet warm.",
	"Fart with confidence. The timid ones smell worse.",
	"A day without laughter is just Monday.",
	"Carry snacks. Always.",
	"Water your plants. They’re rooting for you.",
	"The floor is sticky because you stepped in soda, not destiny.",
	"If you get lost, follow the smell of pizza.",
	"Don’t trust escalators. They’re always up to something.",
	"The best advice is often wrapped in a burrito.",
	"Don’t eat yellow Legos.",
	"Don’t trust clowns named Steve.",
	"One does not simply walk into Chuck E. Cheese.",
	"Stop drop and roll."
)

saying_list = (
	'"Cheese"',
	"Don't look behind you.",
	"6 7",
	"Last one to the car is a rotten egg!",
	"What time did the man go to the dentist? Tooth-Hurty!",
	"A doctor a day keeps the apple away.",
	"An apple a day keeps the doctor away.",
	"Skibidi bop, yes yes. Skibidi bop dee dee.",
	"Banana phone is always on silent mode.",
	"My left shoe knows secrets my right shoe will never hear.",
	"The moon owes me five dollars.",
	"I licked a cactus and now I’m bilingual.",
	"Chair today, gone tomorrow.",
	"Slap a sandwich and call it art.",
	"Water is just crunchy air.",
	"Hot dogs are just meat saxophones.",
	"Beans are just jellybeans that skipped college.",
	"If socks disappear in the dryer, maybe it's because they wanted freedom.",
	"Honk if you’ve ever spoken to a mailbox.",
	"Clouds are just sky potatoes.",
	"Waffles are pancakes with abs.",
	"A goose is basically an angry balloon.",
	"Slap the bassoon, scare the raccoon.",
	"Bananas are berries. Strawberries are liars.",
	"Yanny isn't real. It never was.",
	"Stranger Danger!",
	"Ooga-booga, the math test is due-ga!",
	"Oops! All Goblins.",
	"Duck, duck, GOOSE!",
	"Last one to blink is a rotten pickle!",
	"I spy with my little eye... your mom.",
	"No cap, I lost my cap.",
	"I’m faster than WiFi at grandma’s house.",
	"One fish, two fish, red fish, blue fish.",
	"Tag, you’re mom.",
	"The alphabet ends at Q if you’re brave enough.",
	"Marco! Polo! FBI, open up!",
	"Batteries not included.",
	"Step on a crack, summon a snack.",
	"Hide and seek champion since 2007.",
	"Give me liberty or give me milk.",
	"That goat is the sauce!"
)

quiz = {
	"What is the capital of France?": "Paris",
	"What is the only food that never expires?": "honey",
	"What is the furthest planet from the Sun?": "Neptune",
	"What is 7 + 8?": "15",
	"What is 67 * 5?": "335",
	"What is 3 * 3 * 3?": "27",
	"What is 13^2?": "169",
	"What is ln(e)?": "1",
	"What kind of dragon is Toothless from 'How to Train Your Dragon'?": "Night Fury",
	"Who is the 'King of Rock and Roll'?": "Elvis Presley",
	"Which is hotter: 80 F or 30 C": "30 C",
	"What is the 22nd letter of the alphabet?": "v",
	"What is 100 in Roman Numerals?": "C",
	"Who is the 16th President of the USA?": "Abraham Lincoln",
	"What should you not do right now?": "Look behind you",
	"How many sides does a decagon have?": "10",
	"Who is McDonald's mascot?": "Ronald McDonald",
	"What color is made by mixing red and blue paint together?": "purple",
	"What is the powerhouse of the cell?": "Mitochondria",
	"What country is Venice located in?": "Italy",
	"Who holds the record for the most olympic medals?": "Michael Phelps",
	"Who won the 2022 NBA Finals?": "Warriors",
	"Who won the 2025 SuperBowl?": "Eagles",
	"Who was the first man to step on the moon?": "Neil Armstrong",
	"Who was the first woman to fly solo around the world?": "Jerrie Mock",
	"Who is Harry Potter's father?": "James Potter",
	"I shave every day but my beard remains the same, what am I?": "barber",
	"What is the 7th element on the periodic table?": "Nitrogen",
	"Which element has exactly 30 protons?": "Zinc",
	"What does the atomic symbol Au stand for?": "Gold",
	"What is the atomic symbol for Platinum?": "Pt",
	"What is 12 * 12?": "144",
	"What is 25 * 4?": "100",
	"What is 81 / 9?": "9",
	"What is the square root of 225?": "15",
	"What is 9 factorial?": "362880",
	"What is 2^10?": "1024",
	"What is the derivative of x^2?": "2x",
	"What is the integral of 1/x?": "ln(x)",
	"What is the chemical symbol for Iron?": "Fe",
	"What is the chemical symbol for Sodium?": "Na",
	"What is the lightest element?": "Hydrogen",
	"What is the heaviest naturally occurring element?": "Uranium",
	"What planet has the most moons?": "Saturn",
	"What planet spins on its side?": "Uranus",
	"What is the largest planet?": "Jupiter",
	"What is the smallest planet?": "Mercury",
	"What is the fastest land animal?": "Cheetah",
	"What is the slowest animal?": "Sloth",
	"What mammal lays eggs?": "Platypus",
	"What is the tallest mountain on Earth?": "Everest",
	"What is the longest river on Earth?": "Nile",
	"What is the largest ocean?": "Pacific",
	"What is the smallest country?": "Vatican",
	"What is the largest desert?": "Sahara",
	"What is the currency of Japan?": "Yen",
	"What is the currency of Mexico?": "Peso",
	"What is the national sport of Japan?": "Sumo",
	"What is the national animal of Canada?": "Beaver",
	"What is the national flower of USA?": "Rose",
	"Who painted Mona Lisa?": "Leonardo da Vinci",
	"Who painted Starry Night?": "Vincent van Gogh",
	"Who wrote Hamlet?": "Shakespeare",
	"Who wrote Odyssey?": "Homer",
	"Who discovered gravity?": "Newton",
	"Who discovered electricity with a kite experiment?": "Benjamin Franklin",
	"Who invented telephone?": "Alexander Graham Bell",
	"Who invented light bulb?": "Thomas Edison",
	"Who was first President of USA?": "George Washington",
	"Who wrote Declaration of Independence?": "Thomas Jefferson",
	"Who freed slaves with Emancipation Proclamation?": "Abraham Lincoln",
	"Who discovered America in 1492?": "Christopher Columbus",
	"Who crossed Alps with elephants?": "Hannibal",
	"Who was first emperor of Rome?": "Augustus",
	"What is the longest bone in human body?": "Femur",
	"What is the smallest bone in human body?": "Stapes",
	"What is the hardest substance in human body?": "Enamel",
	"What is the largest organ in human body?": "Skin",
	"What is the rarest blood type?": "AB-",
	"What is the universal donor blood type?": "O-",
	"What is the universal recipient blood type?": "AB+",
	"What does DNA stand for?": "Deoxyribonucleic acid",
	"What does CPU stand for?": "Central Processing Unit",
	"What does GPU stand for?": "Graphics Processing Unit",
	"What does RAM stand for?": "Random Access Memory",
	"What does HTTP stand for?": "Hypertext Transfer Protocol",
	"What does URL stand for?": "Uniform Resource Locator",
	"What does NASA stand for?": "National Aeronautics and Space Administration",
	"What does FBI stand for?": "Federal Bureau of Investigation",
	"What does CIA stand for?": "Central Intelligence Agency",
	"What does ATM stand for?": "Automated Teller Machine",
	"What is Mario's brother's name?": "Luigi",
	"What is Sonic's sidekick's name?": "Tails",
	"What color is Pac-Man?": "yellow",
	"What game has creepers and endermen?": "Minecraft",
	"What is Link's horse's name?": "Epona",
	"What is Pikachu's evolution?": "Raichu",
	"What is the first Pokemon in the Pokedex?": "Bulbasaur",
	"What type is Charizard?": "Fire",
	"What is the rarest Pokemon card?": "Pikachu Illustrator",
	"What is the most sold video game ever?": "Minecraft",
	"What does GTA stand for?": "Grand Theft Auto",
	"What is the highest selling console?": "PlayStation 2",
	"What sport uses a shuttlecock?": "Badminton",
	"What sport uses a pommel horse?": "Gymnastics",
	"What sport uses wickets?": "Cricket",
	"What sport uses a scrum?": "Rugby",
	"What sport uses checkered flag?": "Racing",
	"What sport uses a foil?": "Fencing",
	"What animal has three hearts?": "Octopus",
	"What animal has the longest neck?": "Giraffe",
	"What animal has black and white stripes?": "Zebra",
	"What animal is the largest mammal?": "Blue Whale",
	"What animal can regrow its limbs?": "Starfish",
	"What animal never sleeps?": "Bullfrog",
	"What fruit has seeds on the outside?": "Strawberry",
	"What fruit is yellow and curved?": "Banana",
	"What fruit is also a color?": "Orange",
	"What vegetable makes you cry?": "Onion",
	"What vegetable is Bugs Bunny's favorite?": "Carrot",
	"What nut is used to make Nutella?": "Hazelnut",
	"What is the square root of 144?": "12",
	"What is 21 * 21?": "441",
	"What is 2^10?": "1024",
	"What is 0! equal to?": "1",
	"What is the chemical formula for water?": "H2O",
	"What is the main gas we breathe in?": "oxygen",
	"What is the capital of Japan?": "Tokyo",
	"What is the capital of Canada?": "Ottawa",
	"What is the capital of Mexico?": "Mexico City",
	"What is the tallest mountain in the world?": "Everest",
	"What is the largest ocean on Earth?": "Pacific",
	"What is the longest river in the world?": "Nile",
	"What planet has the most moons?": "Saturn",
	"What planet is known as the Red Planet?": "Mars",
	"What galaxy is Earth located in?": "Milky Way",
	"What is the speed of light in m/s (approx)?": "300000000",
	"What does DNA stand for?": "Deoxyribonucleic acid",
	"What does CPU stand for?": "Central Processing Unit",
	"What does GPU stand for?": "Graphics Processing Unit",
	"What does RAM stand for?": "Random Access Memory",
	"What programming language is named after a snake?": "Python",
	"What is the symbol for Potassium?": "K",
	"What is the symbol for Silver?": "Ag",
	"What is the symbol for Iron?": "Fe",
	"What is the heaviest naturally occurring element?": "Uranium",
	"What is the largest mammal in the world?": "Blue Whale",
	"What is the fastest land animal?": "Cheetah",
	"What is the only mammal capable of true flight?": "bat",
	"What is the national bird of the USA?": "Bald Eagle",
	"What is the national sport of Japan?": "Sumo",
	"What is the national flower of France?": "Iris",
	"What is the hardest natural substance on Earth?": "diamond",
	"What is the lightest element?": "Hydrogen",
	"What is the rarest blood type?": "AB negative",
	"What is the longest bone in the human body?": "femur",
	"What is the smallest bone in the human body?": "stapes",
	"What part of the body produces insulin?": "pancreas",
	"What is the scientific name for humans?": "Homo sapiens",
	"What is 9 * 9 * 9?": "729",
	"What is 15 squared?": "225",
	"What is 14 cubed?": "2744",
	"What is the derivative of x^2?": "2x",
	"What is the integral of 1/x dx?": "ln(x)",
	"What is the 1st prime number?": "2",
	"What is the 10th prime number?": "29",
	"What is the 26th letter of the alphabet?": "z",
	"What is the Greek letter for 3.14159?": "pi",
	"What is the Roman numeral for 50?": "L",
	"What is the Roman numeral for 1000?": "M",
	"What is the Roman numeral for 500?": "D",
	"What is 1 mile in feet?": "5280",
	"What is 1 inch in centimeters?": "2.54",
	"What is 1 kilogram in grams?": "1000",
	"What is 1 liter in milliliters?": "1000",
	"What is 1 gigabyte in megabytes?": "1024",
	"What is the boiling point of water in Celsius?": "100",
	"What is the freezing point of water in Fahrenheit?": "32",
	"What is the largest continent?": "Asia",
	"What is the smallest continent?": "Australia",
	"What is the most spoken language worldwide?": "English",
	"What is the second most spoken language worldwide?": "Mandarin",
	"What is the currency of Japan?": "yen",
	"What is the currency of UK?": "pound",
	"What is the currency of USA?": "dollar",
	"What is the currency of Mexico?": "peso",
	"What color is chlorophyll?": "green",
	"What color are emeralds?": "green",
	"What color are rubies?": "red",
	"What color are sapphires?": "blue",
	"What color are amethysts?": "purple",
	"What color is obsidian?": "black",
	"What animal says moo?": "cow",
	"What animal says meow?": "cat",
	"What animal says woof?": "dog",
	"What animal says ribbit?": "frog",
	"What animal says quack?": "duck",
	"What animal says neigh?": "horse",
	"What animal says oink?": "pig",
	"What animal says baaa?": "sheep",
	"What animal says cock-a-doodle-doo?": "rooster",
	"What color is an orange?": "orange",
	"What fruit is yellow and curved?": "banana",
	"What fruit has spikes and is known as the king of fruits?": "durian",
	"What fruit is red and often mistaken for a vegetable?": "tomato",
	"What vegetable makes you cry when you cut it?": "onion",
	"What vegetable is Bugs Bunny always eating?": "carrot",
	"What vegetable is green and looks like tiny trees?": "broccoli",
	"What food is traditionally eaten on Thanksgiving in USA?": "turkey",
	"What food is made from fermented milk?": "yogurt",
	"What food comes from bees?": "honey",
	"What drink is made from ground roasted beans?": "coffee",
	"What drink is made from leaves steeped in hot water?": "tea",
	"What drink is made from fermented grapes?": "wine",
	"What drink is made from hops and barley?": "beer",
	"What is 17 * 19?": "323",
	"What is 2^8?": "256",
	"What is the cube root of 27?": "3",
	"What is 100 factorial divided by 99 factorial?": "100",
	"What is the derivative of sin(x)?": "cos(x)",
	"What is the derivative of cos(x)?": "-sin(x)",
	"What is the integral of cos(x)?": "sin(x)",
	"What is the integral of e^x?": "e^x",
	"What is the 5th Fibonacci number?": "5",
	"What is the 12th Fibonacci number?": "144",
	"What is the capital of Italy?": "Rome",
	"What is the capital of Germany?": "Berlin",
	"What is the capital of Australia?": "Canberra",
	"What is the capital of Brazil?": "Brasilia",
	"What is the capital of China?": "Beijing",
	"What is the capital of India?": "New Delhi",
	"What is the capital of South Korea?": "Seoul",
	"What is the capital of Egypt?": "Cairo",
	"What is the capital of Russia?": "Moscow",
	"What is the capital of Spain?": "Madrid",
	"What is the symbol for Sodium?": "Na",
	"What is the symbol for Gold?": "Au",
	"What is the symbol for Mercury?": "Hg",
	"What is the symbol for Lead?": "Pb",
	"What is the atomic number of Carbon?": "6",
	"What is the atomic number of Oxygen?": "8",
	"What is the atomic number of Neon?": "10",
	"What is the most common element in universe?": "Hydrogen",
	"What is the largest desert in world?": "Sahara",
	"What is the longest wall in world?": "Great Wall of China",
	"What is the fastest bird?": "Peregrine Falcon",
	"What is the largest land carnivore?": "Polar Bear",
	"What is the slowest mammal?": "Sloth",
	"What is the loudest animal?": "sperm whale",
	"What is the tallest land animal?": "Giraffe",
	"What is the smallest planet?": "Mercury",
	"What is the hottest planet?": "Venus",
	"What is the coldest continent?": "Antarctica",
	"What is the driest continent?": "Antarctica",
	"What is the wettest place on Earth?": "Mawsynram",
	"What is the most common blood type?": "O positive",
	"What is the first element on periodic table?": "Hydrogen",
	"What is the last element currently?": "Oganesson",
	"What is the binary of 13?": "1101",
	"What is the hexadecimal of 255?": "FF",
	"What is the octal of 64?": "100",
	"What is ASCII code for A?": "65",
	"What is Morse code for SOS?": "...---...",
	"What is the language with most native speakers?": "Mandarin",
	"What is the largest island in world?": "Greenland",
	"What is the biggest ocean trench?": "Mariana Trench",
	"What is the currency of China?": "yuan",
	"What is the currency of South Korea?": "won",
	"What is the currency of India?": "rupee",
	"What is the tallest building in world?": "Burj Khalifa",
	"What is the fastest train in world?": "Maglev",
	"What is the most popular sport worldwide?": "soccer",
	"What is the national animal of Scotland?": "unicorn",
	"What is the national fruit of India?": "mango",
	"What is the national dish of Japan?": "sushi",
	"What is the national drink of UK?": "tea",
	"What is the study of earthquakes?": "seismology",
	"What is the study of stars?": "astronomy",
	"What is the study of fungi?": "mycology",
	"What is the study of insects?": "entomology",
	"What is the fear of spiders?": "arachnophobia",
	"What is the fear of heights?": "acrophobia",
	"What is 0 divided by 0?": "undefined",
	"What is the opposite of opposite?": "same",
	"What is Mario’s brother’s name?": "Luigi",
	"What is orange and rhymes with parrot?": "carrot",
	"What is Pikachu’s type?": "electric",
	"What is the shape of stop sign?": "octagon",

	# trick questions
	"What is heavier: 1 pound of feathers or 1 pound of bricks?": "neither",
	"What is the airspeed velocity of an unladen swallow?": "nothing" or "what",
	"What color is a mirror?": "mirror" or "reflective",
	"What is the answer to life, the universe, and everything?": "42",
	"What is brown and sticky?": "stick",
	"What do cows drink?": "water",
	"What do you call fake spaghetti?": "impasta",
	"What do you call cheese that doesn't belong to you": "nacho cheese",
	"What is 2+2=5 called?": "wrong" or "incorrect",
	"What is the color of math?": "blue"
}

while restart:

	# User chooses what they want to do
	choice = str(input("Welcome to the MAGIC-9 BALL!!! \nType 1 for advice \nType 2 for a silly saying \nType 3 for a game \nType 4 for a quiz\n\n"))
	replay = True

	# select a random piece of advice from a list
	if choice.lower() in ("1", "one", "uno"):
		while replay:
			advice = random.choice(advice_list)
			print()
			print(advice)
			replay_q = input("\n	(T/F) You want another silly saying. ")
			if replay_q.lower() in ("f", "false"):
				replay = False

	# select a random silly quote from a list
	elif choice.lower() in ("2", "two", "dos"):
		while replay:
			saying = random.choice(saying_list)
			print()
			print(saying)
			replay_q = input("\n	(T/F) You want another silly saying. ")
			if replay_q.lower() in ("f", "false"):
				replay = False


	# select a random game
	elif choice.lower() in ("3", "three", "tres"):
		while replay:
			game = random.randint(1, 5)
			print()


			# the don't turn around game
			if game == 1:
				print("Don't look behind you.")



			# the number guessing game
			elif game == 2:
			
				# Gets the random number and gives the player's first guess
				rand_num = random.randint(1, 100)
				attempts = 0
				guesses = 5

				print("⚖️  WELCOME to Higher or Lower!!! ⚖️")
				guess = int(input("Guess a number from 1 to 100. You have " + str(guesses) + " guesses: "))
				attempts += 1
				guesses -= 1

				# Allows player to guess a number until they guess the correct one
				while guess != rand_num and guesses != 0:
					if guess < rand_num:
						print("\ntoo low! ⬆️")
					else:
						print("\ntoo high! ⬇️")

					# Determines and displays how close the user is to the actual number
					if abs(guess - rand_num) >= 80:
						print("You're in the arctic!")
					elif abs(guess - rand_num) >= 60 and abs(guess - rand_num) < 80:
						print("You're freezing!")
					elif abs(guess - rand_num) >= 40 and abs(guess - rand_num) < 60:
						print("You're ice cold!")
					elif abs(guess - rand_num) >= 25 and abs(guess - rand_num) < 40:
						print("You're cold!")
					elif abs(guess - rand_num) >= 15 and abs(guess - rand_num) < 25:
						print("You're warm!")
					elif abs(guess - rand_num) >= 5 and abs(guess - rand_num) < 15:
						print("You're hot!")
					elif abs(guess - rand_num) >= 2 and abs(guess - rand_num) < 5:
						print("You're burning!")
					else:
						print("You're in lava!")

					print("You have " + str(guesses) + " guesses left\n")
					guess = int(input("Guess again: "))
					attempts += 1
					guesses -= 1

				print(" ")

				# Congratualtory line & Failure line
				if guess == rand_num:
					print("You guessed the number!")
					print ("It took you " + str(attempts) + " guesses.")
				else:
					print("You ran out of guesses :(")



			# the giant number guessing game
			elif game == 3:
				# Gets the random number and gives the player's first guess
				rand_num = random.randint(1, 1000000)
				attempts = 0
				guesses = 25

				print("⚖️⚖️⚖️  WELCOME to Higher or Lower - EXPANSIVE EDITION!!! ⚖️⚖️⚖️\n")
				guess = int(input("Guess a number from 1 to 1,000,000. You have " + str(guesses) + " guesses: "))
				attempts += 1
				guesses -= 1

				# Allows player to guess a number until they guess the correct one
				while guess != rand_num and guesses != 0:
					if guess < rand_num:
						print("\ntoo low! ⬆️")
					else:
						print("\ntoo high! ⬇️")


					# Determines and displays how close the user is to the actual number
					if abs(guess - rand_num) >= 999999:
						print("You literally can't get colder.")
					elif abs(guess - rand_num) >=999000  and abs(guess - rand_num) < 999999:
						print("You're in the deep void of space!")
					elif abs(guess - rand_num) >= 995000 and abs(guess - rand_num) < 999000:
						print("You're frozen solid!")
					elif abs(guess - rand_num) >= 950000 and abs(guess - rand_num) < 995000:
						print("You're stranded in the arctic ocean!")
					elif abs(guess - rand_num) >= 900000 and abs(guess - rand_num) < 950000:
						print("You're frostbitten!")
					elif abs(guess - rand_num) >= 850000 and abs(guess - rand_num) < 900000:
						print("You're in a freezer!")
					elif abs(guess - rand_num) >= 800000 and abs(guess - rand_num) < 850000:
						print("You're in the fridge!")
					elif abs(guess - rand_num) >= 750000 and abs(guess - rand_num) < 800000:
						print("You're in Alaska!")
					elif abs(guess - rand_num) >= 700000 and abs(guess - rand_num) < 750000:
						print("You're taking a cold shower!")
					elif abs(guess - rand_num) >= 650000 and abs(guess - rand_num) < 700000:
						print("You're in the pool!")
					elif abs(guess - rand_num) >= 600000 and abs(guess - rand_num) < 650000:
						print("You're freezing!")
					elif abs(guess - rand_num) >= 550000 and abs(guess - rand_num) < 600000:
						print("You're frigid!")
					elif abs(guess - rand_num) >= 500000 and abs(guess - rand_num) < 550000:
						print("You're in a dessert!")
					elif abs(guess - rand_num) >= 450000 and abs(guess - rand_num) < 500000:
						print("You're cold!")
					elif abs(guess - rand_num) >= 350000 and abs(guess - rand_num) < 450000:
						print("You're chilly!")
					elif abs(guess - rand_num) >= 300000 and abs(guess - rand_num) < 350000:
						print("You're cool!")
					elif abs(guess - rand_num) >= 250000 and abs(guess - rand_num) < 300000:
						print("You're room temperature!")
					elif abs(guess - rand_num) >= 150000 and abs(guess - rand_num) < 250000:
						print("You're lukewarm!")
					elif abs(guess - rand_num) >= 100000 and abs(guess - rand_num) < 150000:
						print("You're tepid!")
					elif abs(guess - rand_num) >= 50000 and abs(guess - rand_num) < 100000:
						print("You're slightly warm!")
					elif abs(guess - rand_num) >= 25000 and abs(guess - rand_num) < 50000:
						print("You're warm!")
					elif abs(guess - rand_num) >= 10000 and abs(guess - rand_num) < 25000:
						print("You're smoldering!")
					elif abs(guess - rand_num) >= 7500 and abs(guess - rand_num) < 10000:
						print("You're hot!")
					elif abs(guess - rand_num) >= 4000 and abs(guess - rand_num) < 7500:
						print("You're Super Hot!")
					elif abs(guess - rand_num) >= 2000 and abs(guess - rand_num) < 4000:
						print("You're burning!")
					elif abs(guess - rand_num) >= 1000 and abs(guess - rand_num) < 2000:
						print("You're in Arizona!")
					elif abs(guess - rand_num) >= 500 and abs(guess - rand_num) < 1000:
						print("You're in a desert!")
					elif abs(guess - rand_num) >= 100 and abs(guess - rand_num) < 500:
						print("You're on fire!")
					elif abs(guess - rand_num) >= 50 and abs(guess - rand_num) < 100:
						print("You're in the oven!")
					elif abs(guess - rand_num) >= 10 and abs(guess - rand_num) < 50:
						print("You're in an active volcano!")
					elif abs(guess - rand_num) >= 5 and abs(guess - rand_num) < 10:
						print("You're swimming in lava!")
					elif abs(guess - rand_num) >= 2 and abs(guess - rand_num) < 5:
						print("You're in the Sun!")
					else:
						print("You literally cannot get hotter.")



						print("")


					print("You have " + str(guesses) + " guesses left\n")
					guess = int(input("Guess again: "))
					attempts += 1
					guesses -= 1

				print(" ")

				# Congratualtory line & Failure line
				if guess == rand_num:
					print("You guessed the number!")
					print ("It took you " + str(attempts) + " guesses.")
				else:
					print("You ran out of guesses :(")



			# rock, paper, scissors
			elif game == 4:
				p_rps = input("Let's play Rock, Paper, Scissors! You go first: ")
				if p_rps.lower() == "rock":
					p_rps = 1
				elif p_rps.lower() == "paper":
					p_rps = 2
				elif p_rps.lower() == "scissors":
					p_rps = 3
				else:
					print("\nThat's not an option silly!")

				if type(p_rps) is int:
					cpu_rps = random.randint(1, 3)

					if cpu_rps == 1:
						print("I choose rock!")
					elif cpu_rps == 2:
						print("I choose paper!")
					else:
						print("I choose scissors!")

					if p_rps + cpu_rps == 5:
						pass
					else:
						p_rps = p_rps % 3
						cpu_rps = cpu_rps % 3

					if p_rps > cpu_rps:
						print("You win!")
						rps_score += 1
						rps_streak += 1
					elif p_rps < cpu_rps:
						print("You lose.")
						rps_streak = 0
					else:
						print("It's a draw.")
					if rps_streak > rps_high:
						rps_high = rps_streak

					print("\nTotal Score: " + str(rps_score))
					print("Highest Streak: " + str(rps_high))
				else:
					print("Ya doofus. Let's have a rematch sometime where you play fairly!")



			# tag
			elif game == 5:
				print('"Tag! You are it!!"')
				print("(type tag to tag him back)")
				print()
				p_tag = input()

				while p_tag.lower() == "tag":

					# for if the player gets the perfect skill check
					if tag_monster == True:
						print('\n"WAIT! I recognize that form. No... It can not be you! NO!!! I give up! Please, mercy!!"')
						print("Your opponent gets on his knees and pleads for mercy. \nYou win.")
						break

					# 1st random event
					outcome1 = random.randint(1, 8)
					# quitter
					if outcome1 == 1:
						print('\n"STOP IT! I Do not wanna play this game anymore!!!"')
						print("You're stuck without another player to tag. You are it forever. \nYou lose.")
						break
					# no tagbacks
					elif outcome1 == 2:
						print('\n"Tag again! No tagbacks!"')
						print("You are no longer able to tag the only other player in the game. \nYou lose.")
						break
					# two tag agains
					elif outcome1 == 3:
						print('\n"Tag Again foo!"\n')
						p_tag = input()
					else:
						print('\n"Tag again!"\n')
						p_tag = input()

					# 2nd random event
					outcome2 = random.randint(1, 4)
					# no tagbacks
					if outcome2 == 1:
						print('\n"Tag again again! No tagbacks!"\n')
						print("You are no longer able to tag the only other player in the game. \nYou lose.")
						break
					# the blind path
					elif outcome2 == 2:
						print('\n"Take somma this!"')
						print("You are tagged in the eyes. You can no longer see.\n")
						p_tag = input()
						outcomeblind = random.randint(1,50)
						if outcomeblind == 1:
							print('\n"Dang. You got me. Tag again!"\n')
							p_tag = input()
							outcomeblind2 = random.randint(1,2)
							if outcomeblind2 == 1:
								print('\n"You know what? I feel too bad. It is obviously hard for you to see. I concede."')
								print("You're opponent concedes. \nYou win!")
								break
							else:
								print('\n"Woah friend are you okayyyyhuhhhh??..."')
								print("Your eyes feel a burning pain and you feel your strength slip away from the blood loss. \nYou lose.")
								break
						elif outcomeblind == 2:
							print('\n"WAIT! Careful where you are tagging me!!! We are right next to a-a-AHHHHHHHHH!!!!"')
							print("You successfully tag your opponent. You hear a loud thud a few seconds later. Your opponent does not tag you back. \nYou win!")
							break
						else:
							print("You miss your opponent. You cannot see them. You cannot tag them. \nYou lose.")
							break
					# hit too hard
					elif outcome2 == 3:
						print('\n"Oh No! I tagged you pretty hard there! Are you okay?"')
						print("You feel your organs explode. You die. \nYou lose.")
						break

					# 3rd random event
					outcome3 = random.randint(1, 12)
					if outcome3 in (1, 2, 4, 9, 12):
						# roll stats into a dictionary
						tag_stats = {
							"Strength": random.randint(1, 20),
							"Dexterity": random.randint(1, 20),
							"Wisdom": random.randint(1, 20),
							"Perception": random.randint(1, 20),
							"Charisma": random.randint(1, 20),
							"Luck": random.randint (1, 20)
						}

						tsv = tag_stats.values()

						# print stats and their values
						print("\nSkill Check!\n")
						for stat, value in tag_stats.items():
							print(f"{stat}: {value}")

						# different outcomes depending on the stats

						# if all stats are 20
						if all(v == 20 for v in tsv):
							print('\n"Wh-What?, That Tag was INSANE!!!!!!! I-I can not do this! no way!!!"')
							print("Your opponent retreats. It seems unlikely he will challenge you again. \nYou win. Forever.")
							tag_monster = True
							break

						# if a stat is 20 and none are 1
						elif 20 in tsv and not 1 in tsv:
							max_stats = [stat for stat, value in tag_stats.items() if value == 20]
							print(f'\n"That is some insane {" & ".join(max_stats)}! You are crazy talented!"')
							print("You outclass your opponent with your excellence! You win!")
							break

						# if a stat is 1 and none are 20
						elif 1 in tsv and not 20 in tsv:
							min_stats = [stat for stat, value in tag_stats.items() if value == 20]
							print(f'\n"That is some pathetic {" & ".join(min_stats)}! You are crazy if you think you can take me!"')
							print("You are outclassed through your mediocrity! You lose!")
							break

						# if no stats are substantial
						else:
							print('\n"Haha! good stats on ya! But nevertheless it will not matter! Tag!"\n')
							p_tag = input()

					# no tagbacks
					if outcome3 == 3:
						print('\n"Tag again! No tagbacks!"')
						print("You are no longer able to tag the only other player in the game. \nYou lose.")
						break
						




			replay_q = input("\n	(T/F) You want to play another game. ")
			if replay_q.lower() in ("f", "false"):
				replay = False

	# gives the user a quiz
	elif choice.lower() in ("4", "four", "cuatro"):
		while replay:
			q_score = 0
			question_order = list(quiz.keys())
			random.shuffle(question_order)
			print("\n(please do not use articles [a, an, the])")
			for i in range(10):
				print()
				question = question_order[i]
				answer = quiz[question]
				ans = input(question + " ")
				if ans.strip().lower() == answer.strip().lower():
					print("That's correct! \n\n+1 point")
					q_score += 1
				else:
					print("That's incorrect. The correct answer was " + answer + ".\n")
				print("Score: " + str(q_score) + "/10")
		

			replay_q = input("\n	(T/F) You want to take another quiz. ")
			if replay_q.lower() in ("f", "false"):
				replay = False

	else:
		print("That wasn't an option silly! Try something else.\n")

	restart_q = input("\n		(T/F) You want to try something else. ")
	if restart_q in ("f", "false"):
		restart = False
	print()

# To end the program
input("Press Enter to terminate...")
