from math import inf as oo
import os
import random
class Game:
	def __init__(self):
		self.board = self.createBoard()
		self.current_winner = None
		self.final_winner = None


	@staticmethod
	def createBoard():
		return [[' ' for i in range(3) ] for j in range(3)]

	def drawBoard(self):
		print('----------')
		for i in range(len(self.board)):
			B = '|'
			for j in range(len(self.board)):
				B += self.board[i][j] + '|'
			print(B)
			print('----------')
		return
	def getFigure(self, x, y, letter):
		self.board[x][y] = letter
		return self.board
	def winner(self, cell, letter):
		x, y = cell
		# check for row
		for row in self.board:
			if row.count(letter) == 3:
		#self.winner = letter
				return True

# check for col:
		tranpose = list(map(list, zip(*self.board)))

		for col in tranpose:
			if col.count(letter) == 3:
		#self.winner = letter
				return True

		diagonal1 = [(0,0), (1,1), (2,2)]
		diagonal2 = [(0,2), (1,1), (2,0)]

		count1 = 0
		count2 = 0
		for row, col in diagonal1:
			if self.board[row][col] == letter:
				count1 += 1
		for row, col in diagonal2:
			if self.board[row][col] == letter:
				count2 +=1
		#self.winner = letter if count1 == 3 or count2 == 3 else None
		return count1 == 3 or count2 == 3

	def isFull(self):
		for row in self.board:
			if ' ' in row:
				return False
		return True

	def getEmptySquare(self):
		result = []
		for x in range(len(self.board)):
			for y in range(len(self.board)):
				if self.board[x][y] == ' ':
					result.append((x, y))

		return result

	def makeMove(self, cell, letter):
		x, y = cell
		if self.board[x][y] == ' ':
			self.board[x][y] = letter
			if self.winner(cell, letter):
				self.current_winner = letter
				return True
		return False
	def reset(self):
		return self.createBoard()
class Player():
	def __init__(self, letter):
		self.letter = letter

	def getMove(self):
		pass

class Human(Player):
	def __init__(self, letter):
		super(Human, self).__init__(letter)

	def getMove(self, game):
		options = game.getEmptySquare()
		showedOptions = list(enumerate(options))
		print(showedOptions)
		valid = False
		choice = None
		while not valid:
			try:
				choice = int(input("Enter a cell "))
				if choice < 0 or choice >= len(showedOptions):
					raise ValueError
				valid = True
			except:
				print("Invalid choice")
		return showedOptions[choice][1]

#Level
EASY = 1
HARD = 2

class Comp(Player):
	def __init__(self, letter):
		super(Comp, self).__init__(letter)

	def getMove(self, game, level):
		choice = None
		if level == EASY:
			choice = self.naive(game)
		elif level == HARD:
			choice = self.minimax(game, self.letter)
		return choice['cell']

	def naive(self, game):
		x = random.randint(0,len(game.board)-1)
		y = random.randint(0, len(game.board)-1)

		while game.board[x][y] != ' ':
			x = random.randint(0, len(game.board )-1)
			y = random.randint(0, len(game.board) -1)

		return {'cell' : (x, y)}


	def minimax(self, state, player):
		maxPlayer = self.letter
		minPlayer = 'O' if maxPlayer == 'X' else 'X'
		otherPlayer = 'X' if player == 'O' else 'O'

		if state.current_winner == otherPlayer:
			return {'cell' : None, 'score' : 1} if otherPlayer == maxPlayer else {'cell' : None, 'score' : -1}
		elif len(state.getEmptySquare()) == 0:
			return {'cell' : None, 'score' : 0}

		options = state.getEmptySquare()

		if player == maxPlayer:
			best = {'cell' : None, 'score' : -oo}
		else :
			best = {'cell' : None, 'score' : oo}
		
		for cell in options:
			state.makeMove(cell, player)
			simScore = self.minimax(state, otherPlayer)
			simScore['cell'] = cell
			if player == maxPlayer and simScore['score'] > best['score']:
				best = simScore
			if player == minPlayer and simScore['score'] < best['score']:
				best = simScore

			state.board[cell[0]][cell[1]] = ' '
			state.current_winner = None

		return best





