import pygame
import solve

class display():
    def __init__(self,grid):
        self.W = 900
        self.H = 900
        self.grid = grid
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        
        #init pygame and set screen
        self.screen = pygame.display.set_mode((self.W,self.H))
        pygame.init()
        self.screen.fill(self.WHITE)
        pygame.display.set_caption('Sudoku solve')
     
        
   
    def draw_board(self):
        font1 = pygame.font.SysFont("comicsans", 40)
        dif = 900/9
        for i in range (9):
            for j in range (9):
                if self.grid[i][j] != 0:  
                    text1 = font1.render(str(self.grid[i][j]), 1, self.BLACK)
                    self.screen.blit(text1, (j * dif + 15, i * dif + 15))

        for i in range(10):
            if i % 3 == 0 :
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.screen, self.BLACK, (0, i * dif), (900, i * dif), thick)
            pygame.draw.line(self.screen, self.BLACK, (i * dif, 0), (i * dif, 900), thick)

        
    
BOARD = [
    [2, 5, 0, 0, 3, 0, 9, 0, 1],
    [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]
    ]



board1 = display(BOARD)
while 1: 
    for event in pygame.event.get():
        #call function board
        board1.draw_board()


        if event.type == pygame.QUIT:
            pygame.quit() 

        pygame.display.flip()
