import pygame, sys
from tkinter import *
from tkinter import messagebox
from model import Game, Player, Human, Comp

# Color
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0,255,0)
BACKGROUND_COLOR = (198,185,0)

# Size
WIDTH = 600
HEIGHT = 600
BLOCKSIZE = 200

#TextBox in menu size
BOX_WIDTH = 140
BOX_HEIGHT = 40
PIVOT_X = 250
PIVOT_Y = 250

#Level:
HARD = 2
EASY = 1
class Window(object):
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((600, 600))
		pygame.display.set_caption('Tic Tac Toe')
		self.screen.fill(BACKGROUND_COLOR)
		self.game = Game()
		self.player = Human('X')
		self.comp = Comp('O')
		self.level = None
		
	
	def loop(self):
		mouseX = 0
		mouseY = 0
		coordX = 0
		coordY = 0
		root = Tk().wm_withdraw()
		msg = ''
		menuFlag = True
		while True:
			msg = ''
			pygame.time.delay(100)
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if menuFlag == False:
						mouseX = event.pos[0]
						mouseY = event.pos[1]
						
						coordX = int(mouseX // 200)
						coordY = int(mouseY // 200)

					else:
						mouseX = event.pos[0]
						mouseY = event.pos[1]
						self.level = None
						while self.level == None:
							if  PIVOT_X <= mouseX <= PIVOT_X + BOX_WIDTH and PIVOT_Y <= mouseY <= PIVOT_Y + BOX_HEIGHT:
								self.level = EASY
								
							elif PIVOT_X <= mouseX <= PIVOT_X + BOX_WIDTH and PIVOT_Y + 50 <= mouseY <= PIVOT_Y + BOX_HEIGHT + 50:
								self.level = HARD
				
				if event.type == pygame.MOUSEBUTTONUP:
					if menuFlag == False:
						result = 0
						valid = False # check valid tick.
						if msg == '':
							if self.game.board[coordX][coordY] != ' ':
								valid = False
							else:
								result = self.humanPlay(coordX, coordY)
								if result == 1:
									msg = 'Draw Game. Play again'
								elif result == 2:
									msg = 'You win. Play again'
								valid = True
						if msg == '':	
							if valid == True:
								result = self.compPlay()
								if result == 1:
									msg = "Draw game. Play again"
									
								elif result == 2:
									msg = 'You lost. Play again'
					else:
						menuFlag = False
						self.screen.fill(BACKGROUND_COLOR)
					
						
			if menuFlag == True:
				self.showMenu()

			else:
				self.drawLines()
			pygame.display.flip()
			if msg != '':
				choice = messagebox.askyesno("Game over", msg)
				if choice == True:
					menuFlag = True
					self.screen.fill(BACKGROUND_COLOR)
					self.game.board = self.game.reset()
					
				else:
					sys.exit()
			
			


	def drawLines(self):
		LINE_WIDTH = 15
		pygame.draw.line(self.screen,  BLACK, (0,200), (600,200), LINE_WIDTH)
		pygame.draw.line(self.screen,  BLACK, (0,400), (600,400), LINE_WIDTH)
		pygame.draw.line(self.screen,  BLACK, (200,0), (200,600), LINE_WIDTH)
		pygame.draw.line(self.screen,  BLACK, (400,0), (400,600), LINE_WIDTH)

	def compPlay(self):
		if self.game.isFull():
			return 1
		x, y = self.comp.getMove(self.game, self.level)
		self.game.board[x][y] = self.comp.letter
		pygame.draw.circle(self.screen,  BLACK, (int(x * 200 + 100), int(y * 200 + 100)), 40, 8)
		
		if self.game.winner((x, y), self.comp.letter):
			return 2
		
		return 0

	def humanPlay(self, coordX, coordY):
		if self.game.isFull():
			return 1
		self.game.board[coordX][coordY] = self.player.letter

		def drawX():
			pygame.draw.line(self.screen,  BLACK, (200* coordX + 75, 200*coordY + 75), (200*coordX + 125, 200*coordY + 125), 10)
			pygame.draw.line(self.screen,  BLACK, (200* coordX + 75, 200*coordY + 125), (200*coordX + 125, 200*coordY + 75), 10)
		
		drawX()

		if self.game.winner((coordX, coordY), self.player.letter):
			return 2 
		return 0 

	def showMenu(self):
		colorDark = (170,170,170)
		colorLight = (100,100,100)

		smallFont = pygame.font.SysFont('Corbel', 35)
		text = smallFont.render('EASY', True, WHITE)
		pygame.draw.rect(self.screen, colorLight, [PIVOT_X , PIVOT_Y , 140,40])
		self.screen.blit(text, [PIVOT_X + 30 , PIVOT_Y + 5])

		smallFont = pygame.font.SysFont('Corbel', 35)
		text = smallFont.render('HARD', True, WHITE)
		pygame.draw.rect(self.screen, colorLight, [PIVOT_X, PIVOT_Y + 50 , 140,40])
		self.screen.blit(text, [PIVOT_X + 30, PIVOT_Y + 55 ])





		

		


		




		

	



		
		

		

