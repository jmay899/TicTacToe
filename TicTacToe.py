#Jacob Mayfield
#Tic Tac Toe Personal Project

board = [' ' for x in range(10)]

def mainGame():
	print("Welcome to Tic Tac Toe! Select a position to begin, or type \"quit\" to exit the game at any time.")
	printBoard(board)
	
	while not boardFull(board):
		if not checkWin(board,'O'):
			player1Move()
			printBoard(board)
		else:
			print("Player 2 wins!")
			
		if not checkWin(board,'X'):
			player2Move()
			printBoard(board)
		else:
			print("Player 1 wins!")
			break
			
		if boardFull(board):
			print("This game is a tie.")

def insertMarker(letter,pos):
	board[pos] = letter

def spaceFree(pos):
	return board[pos] == ' '
	
def printBoard(board):
	print(' '+board[1]+' | '+board[2]+' | '+board[3])
	print('   |   |')
	print('----------')
	print(' '+board[4]+' | '+board[5]+' | '+board[6])
	print('   |   |')
	print('----------')
	print(' '+board[7]+' | '+board[8]+' | '+board[9])
	print('   |   |')
	
def checkWin(board,letter):
	return ((board[1]==board[2]==board[3]==letter) or
	(board[4]==board[5]==board[6]==letter) or
	(board[7]==board[8]==board[9]==letter) or
	(board[1]==board[4]==board[7]==letter) or
	(board[2]==board[5]==board[8]==letter) or
	(board[3]==board[6]==board[9]==letter) or
	(board[1]==board[5]==board[9]==letter) or
	(board[3]==board[5]==board[7]==letter))
	
def boardFull(board):
	return not board.count(' ') > 1

		
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
	
	
mainGame()