import random
c = [ 'rock' , 'scissor' , 'paper' ]
x = 0
y = 0
print("||     LET'S PLAY ROCK - PAPER - SCISSORS     ||")
print("------------------------------------------------")
print("Note : your text should be in small letters | try '/help'")
print("------------------------------------------------")
nme = str(input("Enter your name please : "))
print("------------------------------------------------")
cfrm = input("Should we start [yes / no] : ")
print("------------------------------------------------")
while cfrm == "yes" :
	bren = random.choice(c)
	plyr = input("rock / paper / scissor : ")
	print("------------------------------------------------")
	if bren == plyr :
		print("computer goes with : " + str(bren))
		print("It's a tie !")
	elif plyr == "/help":
		print("• /exit  : exit from the game !")
		print("• /score : know your score !")
		print("• /grow  : gain 10 points at instant !")
		print("------------------------------------------------")
		print("•• Created by Prakhar aka Duckie ••")
	elif plyr == "/grow":
		x += 10
		print("cheat activated !")
	elif plyr == "/score" :
		print(str(nme) + " : "+ str(x) + " | Computer : " + str(y))
		if x > y :
			print(str(nme) + " is in lead of " + str(x - y) + " points !")
		elif x < y :
			print("Computer is in lead of " + str( y - x ) + " points !")
		else :
			print("Both are at same point !")
	elif plyr == "rock" :
		if bren == "paper" :
			print("computer goes with : " + str (bren))
			print(str(nme) + " lost !")
			y += 1
		elif bren == "scissor" :
			print("computer goes with : " + str (bren))
			print(str(nme) + " Won !")
			x += 1
	elif plyr == "paper" :
		if bren == "scissor" :
			print("computer goes with : " + str (bren))
			print(str(nme) + " lost !")
			y += 1
		elif bren == "rock" :
			print("computer goes with : " + str (bren))
			print(str(nme) + " Won !")
			x += 1
	elif plyr == "scissor" :
		if bren == "rock" :
			print("computer goes with : " + str (bren))
			print(str(nme) + " lost !")
			y += 1
		elif bren == "paper" :
			print("computer goes with : " + str (bren))
			print(str(nme) + " Won !")
			x += 1
	elif plyr == "/exit" :
		cfrm = "no"
		print("The final scores are :")
		print("Player : " + str(x) + " | Computer : " + str(y))
		print("------------------------------------------------")
		if x > y :
			print(str(nme) + " won the game by  :  " + str(x - y) + " points !")
		elif x < y :
			print(str(nme) + " lost the game by : " + str( y - x ) + " points !")
		else :
			print("Both are at same point ! Hence, its a tie !")
	else :
		print("Enter proper value ! for help , type '/help' !")
		print("------------------------------------------------")
	print("------------------------------------------------")
print("Thanks for playing the game !!")
print("------------------------------------------------")
#PRAKHAR ON TOP
