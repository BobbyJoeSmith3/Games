#Write a trivia game that has 5 questions

#print "Hello, world!"

#Welcome Screen
print "\n\nWelcome to the game, prepare to test your wits!"

score = 0
#Section 1. The first question
print "According to the Center for American Progress, what proportion of US citizines will live at least one year of their lives in poverty?"
print "\ta) One-fifth \n\tb) One-third \n\tc) One-half"
answer = raw_input("Your answer: ")

if answer == "b":
	print "Beginners luck!\n"
	score = score+1
else:
	print 'Actually, the answer is "b". One-third of US citizens will live at least one year of their lives in poverty.\n'


#Section 2. The second question
print "According to the Children's Defense Fund (CDF; 2010), how often is a child born into poverty in the US?"
print "\ta) Every 32 seconds \n\tb) Every 3 minutes and 2 seconds \n\tc) Every 32 minutes"
answer = raw_input("Your answer: ")

if answer == "a":
	print "Correct!\n"
	score = score+1
else:
	print 'Sorry! The answer is "a". A child is born into poverty in the US every 32 seconds \n'

#Section 3. The third question
print "Where do most poor people in the US live?"
print "\ta) In inner cities \n\tb) Outside of inner cities"
answer = raw_input("Your answer:")

if answer == "b":
	print "Correct!\n"
	score = score+1
else:
	print 'Good guess, but the correct answer is "b". Most poor people in the US live outside of inner cities.\n'


#Section 4. The fourth question
print "Which sorts of areas in the U.S. are seeing the greatest increases in poverty rates?"
print "\ta) Urban areas \n\tb) Rural areas \n\tc) Suburban areas"
answer = raw_input("Your answer:")

if answer == "c":
	print "Oh you Fancy huh! \n"
	score = score+1
else:
	print 'Sorry homie! The correct answer is "c", \n Suburban areas are seeing the greates increases in povert in the US. \n'

#Section 5. Game Summary.
print "Well...that's it. Hope you had tons of fun playing a game about poverty!\n"
print "Your final score is:", score, "out of 4 possible points."

if score == 4:
	print "Wow. You sure seem to know a-whole-lot about poverty....Are you the 'Man'?\n"
elif score == 3:
	print "Not bad! I mean, you're no Paul Krugman, but I'm sure you're a good person./n"	
elif score == 2:
	print "Well, not bad. Not good, but not bad either.\n"
elif score == 1:
	print "Wow. That was a struggle! I hope you weren't trying to impress anyone with your progressive grasp of social issues.\n"
else:
	print "Soooo....were you even trying to get any of the answers right? I mean, you didn't get a single question right. I'm not judging you perse, I'm more impressed that you failed so spectacularly. You must be the 1%.\n"





