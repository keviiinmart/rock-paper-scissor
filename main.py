#Project: Rock paper scissor
#User vs Rand num gen 
#Requirements are only three choices randomlly selected. every round ends in A win lose or a draw
#Best of 5 rounds
#Draws are auto redo points for win only first to 3

#imports
import random
import constants

#constants
rps = constants.choices

def opponet():
	opp_choice = random.choice(rps)
	print(opp_choice.title())
	return opp_choice.title()

def user():
	user_choice = input("Do you choose Rock, Paper, or Scissor? ")
	print(user_choice)
	return user_choice.title()

def game_logic(a,b):
	point = 0
	if(a == b):
		point = 0
		print("Draw")
	elif(a=="Rock" and b=="Scissor"):
		point = 1
		print("Rock beats Scissor")
	elif(a=="Paper" and b=="Rock"):
		point = 1
		print("Paper beats Rock")
	elif(a=="Scissor"and b=="Paper"):
		point = 1
		print("Scissor beats Paper")
	elif(a=="Scissor" and b=="Rock"):
		point = -1
		print("Rock beats Scissor")
	elif(a=="Rock" and b=="Paper"):
		point = -1
		print("Paper beats Rock")
	elif(a=="Paper" and b=="Scissor"):
		point = -1
		print("Scissor beats Paper")
	return point


def game():
	User = 0
	Opponet = 0
	point = 0
	GameOver = "no"
	while(GameOver != "GAME OVER"):
		point = game_logic(user(),opponet())
		if point == 1:
			User = User + 1
		elif point == -1:
			Opponet = Opponet + 1
		if User == 3 or Opponet == 3:
			print("Game Over!!!!")
			GameOver = "GAME OVER"
		
		
		print("\nUser: " + str(User) + " Point(s)\n")
		print("Opponet: " + str(Opponet) + " Point(s)\n")


game()
	
