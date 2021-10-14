#Jacob Mayfield
#Tic Tac Toe Personal Project

board = [' ' for x in range(10)]

def mainGame():
	print("Welcome to Tic Tac Toe! Select a position to begin, or type \"quit\" to exit the game at any time.")
	printBoard(board)
	
	#ask if single player or multiplayer game
	singleOrMulti = input("Do you want to play single player against the CPU, or local multiplayer? (Type \'s\' or \'m\'): ")
	if singleOrMulti == "quit":
		exit()
	while singleOrMulti != "s" and singleOrMulti != "m":
		singleOrMulti = input("Please enter a valid input (\'s\' or \'m\'): ")
		if singleOrMulti == "quit":
			exit()
	
	while not boardFull(board):
		#player 1 move and check
		if not checkWin(board,'O'):
			player1Move()
			printBoard(board)
		else:
			if singleOrMulti == "s":
				print("The CPU wins.")
				break
			else:
				print("Player 2 wins!")
				break
		
		#top if local multiplayer, bottom if singleplayer against cpu
		if singleOrMulti == 'm':
			if boardFull(board):
				print("Player 1 wins!")
				exit()
			if not checkWin(board,'X'):
				player2Move()
				printBoard(board)
			else:
				print("Player 1 wins!")
				break
		else:
			if not checkWin(board,'X'):
				move = computerMove()
				if move == 0:
					print("This game is a tie.")
				else:
					insertMarker('O', move)
					print("The CPU placed an O in position",move)
					printBoard(board)					
			else:
				print("You won!")
				break
				
	if boardFull(board):
		print("This game is a tie.")

#insert X or O into spot
def insertMarker(letter,pos):
	board[pos] = letter

#tell if space is available
def spaceFree(pos):
	return board[pos] == ' '
	
#print board with X's and O's if applicable
def printBoard(board):
	print(' '+board[1]+' | '+board[2]+' | '+board[3])
	print('   |   |')
	print('----------')
	print(' '+board[4]+' | '+board[5]+' | '+board[6])
	print('   |   |')
	print('----------')
	print(' '+board[7]+' | '+board[8]+' | '+board[9])
	print('   |   |')
	
#check if player who just played has won
def checkWin(board,letter):
	return ((board[1]==board[2]==board[3]==letter) or
	(board[4]==board[5]==board[6]==letter) or
	(board[7]==board[8]==board[9]==letter) or
	(board[1]==board[4]==board[7]==letter) or
	(board[2]==board[5]==board[8]==letter) or
	(board[3]==board[6]==board[9]==letter) or
	(board[1]==board[5]==board[9]==letter) or
	(board[3]==board[5]==board[7]==letter))
	
#check if board is full
def boardFull(board):
	return not board.count(' ') > 1

#allow player 1 to select their position - either single or multiplayer
def player1Move():
	active = True
	while active:
		move = input("Player 1: Select an open position to place your X (1-9): ")
		if move == "quit":
			exit()
		try:
			move = int(move)
			if move > 0 and move < 10:
				if spaceFree(move):
					active = False
					insertMarker('X', move)
				else:
					print("This space is occupied, try again.")
			else:
				print("Please enter a valid number.")
		except:
			print("Please type a number between 1 and 9")
	
#allow player 2 to select their position - only in multiplayer
def player2Move():
	active = True
	while active:
		move = input("Player 2: Select an open position to place your O (1-9): ")
		if move == "quit":
			exit()
		try:
			move = int(move)
			if move > 0 and move < 10:
				if spaceFree(move):
					active = False
					insertMarker('O', move)
				else:
					print("This space is occupied, try again.")
			else:
				print("Please enter a valid number.")
		except:
			print("Please type a number between 1 and 9")
	
#allow the computer to select their position - only in single player
def computerMove():
	availableSpots = [i for i, letter in enumerate(board) if letter == ' ' and i!=0]
	move = 0
	
	#win game if possible
	for l in ['O','X']: #l for letter
		for i in availableSpots:
			boardTemp = board[:]
			boardTemp[i] = l
			if checkWin(boardTemp,l):
				return i
	
	#find available corners - always choose open corner if possible
	availableCorners = []
	for i in availableSpots:
		if i in [1,3,7,9]:
			availableCorners.append(i)
	
	if len(availableCorners) > 0:
		return selectRandomTile(availableCorners)
		
	#choose middle spot after corners taken
	if 5 in availableSpots:
		return 5
		
	#last case scenario, choose a random edge
	availableEdges = []
	for i in availableSpots:
		if i in [2,4,6,8]:
			availableEdges.append(i)
	
	if len(availableEdges) > 0:
		return selectRandomTile(availableEdges)
	
	#no open spot, return 0
	return move
	
#for computer only - select a random tile from those available	
def selectRandomTile(list):
	import random
	length = len(list)
	rand = random.randrange(0,length)
	return list[rand]
	
mainGame()