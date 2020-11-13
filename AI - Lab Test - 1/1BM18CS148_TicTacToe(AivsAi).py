import random
from time import sleep
import copy

def isSpaceFree(board,move):
	return board[move] == ' '

def drawBoard(board):
	print(board[1] + '|' + board[2] + '|' + board[3])
	print('-+-+-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-+-+-')
	print(board[7] + '|' + board[8] + '|' + board[9])
	print()

def isWinner(board,letter):
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

def randomNumber():
	return random.randint(1,9)

def canWin(board,letter,move):
	temp = copy.deepcopy(board)
	temp[move] = letter
	return isWinner(temp,letter)

def WinStrategy(board,letter):
	if isSpaceFree(board,5):
		return 5
	for i in [1, 3, 7, 9]:
		if isSpaceFree(board,i):
			return i
	for i in [2, 4, 6, 8]:
		if isSpaceFree(board,i):
			return i

def getAgentMove(theBoard,letter):
	if letter == 'O':
		for move in range(1,10):
			if isSpaceFree(theBoard,move) == True and canWin(theBoard,'O',move):
				return move
		for move in range(1,10):
			if isSpaceFree(theBoard,move) == True and canWin(theBoard,'X',move):
				return move
	else:
		for move in range(1,10):
			if isSpaceFree(theBoard,move) == True and canWin(theBoard,'X',move):
				return move
		for move in range(1,10):
			if isSpaceFree(theBoard,move) == True and canWin(theBoard,'O',move):
				return move
	return WinStrategy(theBoard,letter)

def main():
	print("TIC-TAC-TOE")
	print("AI vs AI")

	while True:
		theBoard = [' ']*10
		drawBoard('0 1 2 3 4 5 6 7 8 9'.split())
		isGamePlaying = True
		first = True
		while isGamePlaying:
			for agent in ['X','O']:
				print("AI " + agent + "'s turn:")
				if(first):
					move = randomNumber()
					print("Selects " + str(move))
					theBoard[move] = agent
					first = False
				else:
					move = getAgentMove(theBoard,agent)
					print("Selects " + str(move))
					theBoard[move] = agent
				#check if any agent has won the match
				if isWinner(theBoard,agent):
					drawBoard(theBoard)
					print(agent + " won the game")
					isGamePlaying = False
					break
				if isDraw(theBoard):
					drawBoard(theBoard)
					print("Its a Tie!")
					isGamePlaying = False
					break
				drawBoard(theBoard)
				sleep(1)
		print("Do you want them play again : ( Y / N ) ")
		choice = input()
		if choice == 'n' or choice == 'N':
			break

if __name__ == '__main__':
    main()