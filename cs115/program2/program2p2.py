'''
Prolog:
        University of Kentucky
	CS 115
	Program 2 phase 2

Description:
	Graphical game of 21

Pre-conditions:
	Get string input from user for name and whether to roll or pass

Post-conditions:
	Print results of game
'''

from random import *
from graphics import *
import time


def main():
	'''
	Description: 
		Main function with game loop.
	Preconditions: 
		Player names, decisions to roll or pass.
	Postconditions: 
		Prompts, displays of totals and pass counts, rolls of the die
		statement of who wins.
	'''
	# prepare graphics window
	win = GraphWin("Twenty One", 500, 500)
	start_screen = Text(Point(250, 100),
	"TWENTY ONE\nDon't hit 21 or over!\nYou have 2 passes\nClick to continue")
	start_screen.draw(win)
	win.getMouse()
	start_screen.undraw()
	
	#  get player 1's name using Entry object
	name_screen = Text(Point(250, 100),\
	"PLAYER ONE\nEnter your name\n(click to enter)")
	
	name_screen.draw(win)
	p1_name_entry = Entry(Point(250, 200), 20)
	p1_name_entry.draw(win)
	win.getMouse()
	name_screen.undraw()
	p1_name = p1_name_entry.getText()
	p1_name_entry.undraw()
	
	#  get player 2's name using Entry object
	name_screen = Text(Point(250, 100),\
	"PLAYER TWO\nEnter your name\n(click to enter)")
	
	name_screen.draw(win)
	p2_name_entry = Entry(Point(250, 200), 20)
	p2_name_entry.draw(win)
	win.getMouse()
	name_screen.undraw()	
	p2_name = p2_name_entry.getText()
	p2_name_entry.undraw()
	
	
	# initialize player roll totals
	p1_total, p2_total = 0, 0

	# initialize player number of passes
	p1_pass, p2_pass = 2, 2
	
	# initialize int of rounds
	round_num = 0
	
	#set up score display
	score_display = Text(Point(400, 200),"")
	
	# while neither player has lost
	while p1_total < 21 and p2_total < 21:
		# increment and display round number 
		round_num += 1
		score_display.undraw()
		score_display.setText("Round: " + str(round_num) + "\n\nPlayer 1: " + 
		p1_name + "\nScore: " + str(p1_total) + "\nPasses: " + str(p1_pass) + 
		"\n\nPlayer 2: " + p2_name + "\nScore: " + str(p2_total) + "\nPasses: "
		 + str(p2_pass))
		score_display.draw(win)
		
		# do player one's turn, then player two's if player one didn't lose
		p1_total, p1_pass = play_turn(p1_name, p1_total, p1_pass, win)
		if p1_total < 21:
			score_display.undraw()
			score_display.setText("Round: " + str(round_num) + "\n\nPlayer 1: " + 
			p1_name + "\nScore: " + str(p1_total) + "\nPasses: " + str(p1_pass) + 
			"\n\nPlayer 2: " + p2_name + "\nScore: " + str(p2_total) + "\nPasses: "
			 + str(p2_pass))
			score_display.draw(win)
			p2_total, p2_pass = play_turn(p2_name, p2_total, p2_pass, win)
			score_display.undraw()
			score_display.setText("Round: " + str(round_num) + "\n\nPlayer 1: " + 
			p1_name + "\nScore: " + str(p1_total) + "\nPasses: " + str(p1_pass) + 
			"\n\nPlayer 2: " + p2_name + "\nScore: " + str(p2_total) + "\nPasses: "
			 + str(p2_pass))
		
		# clean screen
		score_display.undraw()
		score_display.setText("Round: " + str(round_num) + "\nPlayer 1: " + 
		p1_name + "\nScore: " + str(p1_total) + "\nPasses: " + str(p1_pass) + 
		"\n\nPlayer 2: " + p2_name + "\nScore: " + str(p2_total) + "\nPasses: " 
		+ str(p2_pass))
		score_display.draw(win)
	
	# if one player exceeds 21, displays that the other player wins
	if p1_total > 21:
		winner_text = Text(Point(100, 20), "Player " + p2_name + " wins!")
	else:
		winner_text = Text(Point(100, 20), "Player " + p1_name + " wins!")
	winner_text.draw(win)
	win.getMouse()

def play_turn(p_name, p_total, p_pass, win):
	'''
	Description:
		Do one player's turn, perform rolls or passes as player chooses.
	Precondition:
		Player name, player roll total, player's pass count.
	Postcondition: 
		Player toll total and player's pass count, modified as needed.
	'''
	turn_text = Text(Point(200, 300),"")
	# if user has passes remaining ask for choice, else return roll
	if p_pass != 0:
		# call function to prompt for pass or roll
		turn = pass_or_roll(p_name, win)
		# branch to either roll or pass and call function to draw die
		if turn == "P":
			p_pass -= 1
			turn_text.setText("Player " + p_name + " passed the roll")
			turn_text.draw(win)
			die = draw_die(0, win)
			
		elif turn == "R":
			roll = randint(1,6)
			p_total += roll
			turn_text.setText("Player " + p_name + " rolled " + str(roll))
			turn_text.draw(win)
			die = draw_die(roll, win)
			
	# if user has no more passes, roll without prompting for choice
	else:
		roll = randint(1,6)
		p_total += roll
		turn_text.setText("Player " + p_name + " rolled " + str(roll))
		turn_text.draw(win)
		die = draw_die(roll, win)
	
	# get click to proceed
	end_choice_screen = Text(Point(100, 20), "Click to continue")
	end_choice_screen.draw(win)
	win.getMouse()
	
	# clean screen
	turn_text.undraw()
	die.undraw()
	end_choice_screen.undraw()
	
	return p_total, p_pass

def pass_or_roll(p_name, win):
	'''
	Description:
		Ask the player whether they want to pass the die or roll.
	Precondition: 
		The player's name and graphics window.
	Postcondition: 
		Either 'P' or 'R' based on player's click on one of 2 boxes
	'''
	# draw buttons and initialize color
	pass_button = Rectangle(Point(100, 100), Point(150, 150))
	roll_button = Rectangle(Point(200, 100), Point(250, 150))
	
	pass_button.draw(win)
	pass_text = Text(Point(127, 127),"PASS")
	pass_text.draw(win)
	pass_button.setFill("white")
	
	roll_button.draw(win)
	roll_text = Text(Point(227, 127),"ROLL")
	roll_text.draw(win)
	roll_button.setFill("white")
	
	# draw prompt asking user to click pass or roll buttons
	choice_screen = Text(Point(100, 20),"PLAYER " + str(p_name) + 
	"\n Pass or Roll?")
	choice_screen.draw(win)
	click = win.getMouse()

	# when neither button is pressed ask user to try again
	while not is_between(Point(100, 100), Point(150, 150), click) and not \
	is_between(Point(200, 100), Point(250, 150), click):
		choice_screen.undraw()
		click_again_screen = Text(Point(100, 20),
		"No button pressed\nPlease click either button")
		click_again_screen.draw(win)
		click = win.getMouse()
		click_again_screen.undraw()

	# color green whichever button is pressed and return 'P' or 'R'
	answer = "R"
	if is_between(Point(100, 100), Point(150, 150), click):
		pass_button.setFill("green")
		time.sleep(1)
		answer = "P"
	else:
		roll_button.setFill("green")
		time.sleep(1)
		
	# clean screen
	if answer == "P":
		pass_button.setFill("white")
	else:
		roll_button.setFill("white")
	choice_screen.undraw()
	
	return answer
				
def draw_die(roll, win):
	'''
	Description:
		Draws an image of a die on a graphics window, based on what
		the roll is.
	Preconditions:  
		The roll (integer 0-6) and GraphWin object.
	Postconditions:
		Draws and returns the Image object created with the correct gif file in 
		it.
	'''
	# create filename by adding file suffix, open file, draw and return image
	file_name = str(roll) + ".gif"
	image_file = open(file_name, 'r')
	die_image = Image(Point(200, 400), file_name)
	die_image.draw(win)
	image_file.close()
	return die_image
	
def is_between(p1, p2, p3):
	'''
	Description:
		Tests one point to see if it falls between two other points.
	Preconditions:
		3 Point objects, first two are boundaries, last one is the one to test 
		(p1, p2, p3)
	Postconditions:
		True if the Point to be tested has x and y coordinates that fall between
		the coordinates of the other 2 Points, else False.
	'''
	# initialize return value to false, and return true if p3 falls between p1, p2
	retval = False
	if (p1.getX() < p3.getX() < p2.getX()) and (p1.getY() < p3.getY() < p2.getY()):
		retval = True
		
	return retval
main()
