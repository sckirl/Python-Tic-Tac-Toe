# To play: left click on  mouse to fill tic tac toe grids. to see the winner, just look at the terminal
# after winning the game, you can restart the game with pressing any key on your keyboard (press any key to restart)
# Enjoy!

import pygame
import sys
pygame.init()

# display config for pygame
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic Tac Toe")

clock = pygame.time.Clock()

class game():
    def __init__(self): # important variables to work with
        self.round = 0
        self.stop = False
        self.players = ["X", "O"]
        self.board = [[None, None, None], [None, None, None], [None, None, None]] # drawing the board in 2D array, to store data
        self.font = pygame.font.SysFont('ubuntu', 100) # using font for drawing "X"'s and "O"'s

    def play(self, position):
        if not self.stop:
            x, y = ((position[0]//200), (position[1]//200)) # getting position from player's mouse position (see below, line 53)
            if not self.board[x][y]:                        # convert the position value into list index, and replace list index with current player
                self.board[x][y] = self.players[0]
                self.round += 1                                        
            
            if self.win(x, y): 
                print("{} win".format(self.players[0]))
                self.stop = True
            elif self.round == 9: 
                print("draw")
                self.stop = True
            
            self.switchPlayer()
                
    def win(self, x, y): # function to check which player win the game
        vertical = horizontal = diagonal = rdiag = 0
        for i in range(3): # checks every moves and count how many are connected
            if self.board[x][i] == self.players[0]: vertical += 1 
            if self.board[i][y] == self.players[0]: horizontal += 1
            if self.board[i][i] == self.players[0]: diagonal += 1
            if self.board[i][(3-1)-i] == self.players[0]: rdiag += 1
        
        return vertical == 3 or horizontal == 3 or diagonal == 3 or rdiag== 3
        # credit to https://stackoverflow.com/a/1058804

    def switchPlayer(self):
        self.players.insert(0, self.players.pop()) # switch players on every round
                                                   # ex. ["X", "O"] -> ["O", "X"], get the value of pop() and put it back on front

    def restart(self):
        self.round = 0
        self.stop = False
        self.players = ["X", "O"]
        self.board = [[None, None, None], [None, None, None], [None, None, None]]

    def draw(self):
        for x in range(3):
            for y in range(3):
                pygame.draw.rect(win, (0, 0, 0), (x*200, y*200, 200, 200), 10) # drawing grid with rectangles
                XO = self.font.render(self.board[x][y], 100, (0,0,0))
                win.blit(XO, (x*200+70, y*200+40)) # to draw the X and O at the middle of rectangle

ticTacToe = game()
while(True): # main loop
    clock.tick(10)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
        if events.type == pygame.MOUSEBUTTONDOWN: # whenever player press a key, record the position
            ticTacToe.play(pygame.mouse.get_pos())
        elif events.type == pygame.KEYDOWN: 
            ticTacToe.restart()
    
    #redraw
    win.fill((255, 255, 255))
    ticTacToe.draw()
    pygame.display.update()