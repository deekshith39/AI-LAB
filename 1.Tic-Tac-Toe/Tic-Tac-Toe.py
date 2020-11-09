import random

def drawBoard(board):
	# This function prints out the board that it was passed.
	# "board" is a list of 10 strings representing the board (ignore index 0)
	print(board[1] + '|' + board[2] + '|' + board[3])
	print('-+-+-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-+-+-')
	print(board[7] + '|' + board[8] + '|' + board[9])

def isSpaceFree(board,move):
	return board[move] == ' '

def getPlayerMove(board):
	# Let the player type in their move.
	move = ''
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
		print('What is your next move? (1-9)')
		move = input()
	return int(move)

def isWinner(board,letter):
	# Given a board and a player's letter, this function returns True if that player has won.
	return ((board[1]==letter and board[2]==letter and board[3]==letter) or
			(board[4]==letter and board[5]==letter and board[6]==letter) or
			(board[7]==letter and board[8]==letter and board[9]==letter) or
			(board[1]==letter and board[4]==letter and board[7]==letter) or
			(board[2]==letter and board[5]==letter and board[8]==letter) or
			(board[3]==letter and board[6]==letter and board[9]==letter) or
			(board[1]==letter and board[5]==letter and board[9]==letter) or
			(board[3]==letter and board[5]==letter and board[7]==letter))

def isDraw(board):
	for i in range(1,10):
		if isSpaceFree(board,i) == True:
			return False
	return True

def MiniMax(board,isMax,ComputerLetter):
	if ComputerLetter == 'X':
		PlayerLetter = 'O'
	else:
		PlayerLetter = 'X'

	if isWinner(board,ComputerLetter):
		return 1
	if isWinner(board, PlayerLetter):
		return -1
	if isDraw(board):
		return 0

	if isMax:
		maxVal = -1000
		for i in range(1,10):
			if isSpaceFree(board, i):
				board[i] = ComputerLetter
				eval = MiniMax(board,not isMax,ComputerLetter)
				board[i] = ' '
				maxVal = max(maxVal, eval)
		return maxVal
	else:
		minVal = 1000
		for i in range(1,10):
			if isSpaceFree(board, i):
				board[i] = PlayerLetter
				eval = MiniMax(board,not isMax,ComputerLetter)
				board[i] = ' '
				minVal = min(minVal, eval)
		return minVal


def findBestMove(board, ComputerLetter):
	if ComputerLetter == 'O':
		playerletter = 'X'
	else:
		playerletter = 'O'

	best = -1000
	bestMove = -1

	for i in range(1,10):
		if isSpaceFree(board,i):
			board[i] = ComputerLetter
			moveVal = MiniMax(board,False,ComputerLetter)
			board[i] = ' ' #we will have to redo it to empty so that we can check it for other moves

			if moveVal > best :
				bestMove = i
				best = moveVal
	return bestMove



if __name__ == '__main__':
	print("**TIC-TAC-TOE**")
	drawBoard('0 1 2 3 4 5 6 7 8 9'.split())
	print("Choose the number between 1-9")
	PlayerLetter = input("Do you want to be X or O ? ")



	while True:
		theBoard = [' '] * 10
		if (PlayerLetter == "X" or PlayerLetter == "x"):
			ComputerLetter = "O"
		else:
			ComputerLetter = "X"

		turn = input("Do you want to go first ? (Y or N) ")
		if turn == "Y" or turn == "y":
			turn = 'player'
		else:
			turn = 'computer'

		print(turn + " would go first. ")
		isGamePlaying = True
		while isGamePlaying:
			if turn == 'player':				#Player Move
				move = getPlayerMove(theBoard)
				theBoard[move] = PlayerLetter
				drawBoard(theBoard)
			#check if the move has finished the game
				if isWinner(theBoard,PlayerLetter):
					drawBoard(theBoard)
					print("You have won the game!")
					isGamePlaying = False
				else:
					if isDraw(theBoard):
						drawBoard(theBoard)
						print("The game is a Draw!")
						isGamePlaying = False
					else:
						#drawBoard(theBoard)
						turn = 'computer'
			else:									#AI Move
				print()
				print("AI's Move")
				move = findBestMove(theBoard, ComputerLetter)
				theBoard[move] = ComputerLetter
				drawBoard(theBoard)

				if isWinner(theBoard,ComputerLetter):
					drawBoard(theBoard)
					print("AI wins the game!")
					isGamePlaying = False
				else:
					if isDraw(theBoard):
						drawBoard(theBoard)
						print("The game is draw!")
						isGamePlaying = False
					else:
						#drawBoard(theBoard)
						turn = 'player'

		play = input("Do you want to play again: (Y or N) : ")
		if play == 'N' or play == 'n':
			break






