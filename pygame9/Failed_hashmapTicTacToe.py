# working version is on 'ticTacToe.py', with explanations
# this is an attempt on making tic tac toe with hashmaps, still struggling in 'win' function

import pygame
import sys
pygame.init()

win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic Tac Toe")

clock = pygame.time.Clock()

class game():
    def __init__(self): # important variables to work with
        self.players = ["X", "O"]
        self.board = {}
        self.font = pygame.font.SysFont('ubuntu', 100)

    def play(self, position):
        x, y = (position[0]//200), (position[1]//200)
        self.board.setdefault((x, y), self.players[0]) # current player can choose, using setdefault so 
                                                       # the other player can't overwrite filled place
        if self.win(x, y):
            print("{} win".format(self.players[0]))
        
        self.switchPlayer()
    
    def win(self, x, y): # function to check which player win the game
        vertical = horizontal = diagonal = rdiag = 0
        try:
            for i in range(3): # checks every moves and count how many are connected
                if self.board[(x,i)] == self.players[0]: vertical += 1 
                if self.board[(i,y)] == self.players[0]: horizontal += 1
                if self.board[(i,i)] == self.players[0]: diagonal += 1
                if self.board[(i, ((3-1)-i))] == self.players[0]: rdiag += 1
                print(vertical, horizontal, diagonal, rdiag)
            return vertical == 3 or horizontal == 3 or diagonal == 3 or rdiag==3 # credit to https://stackoverflow.com/a/1058804
        except KeyError: pass

    def switchPlayer(self):
        self.players.insert(0, self.players.pop()) # will cycle through the player
                                                   # ex. ["X", "O"] -> ["O", "X"], get the value of pop() and put it back on front

    def draw(self):
        for x in range(3):
            for y in range(3):
                pygame.draw.rect(win, (0, 0, 0), (x*200, y*200, 200, 200), 10) # drawing grid with rectangles

                if (x, y) in self.board:
                    XO = self.font.render(self.board[(x, y)], 100, (0,0,0))
                    win.blit(XO, (x*200+70, y*200+40)) # to draw the X and O at the middle of rectangle

ticTacToe = game()
while(True):
    clock.tick(10)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
        if events.type == pygame.MOUSEBUTTONDOWN:
            ticTacToe.play(pygame.mouse.get_pos())

    win.fill((255, 255, 255))
    ticTacToe.draw()
    pygame.display.update()