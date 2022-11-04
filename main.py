import pygame
from algorithm import return_neighbours,bfs,reconstruct_path
from tkinter import messagebox

pygame.font.init()

class Visualizer:

    def __init__(self,width,height,rows,cols):
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.display = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption('Shortest Path Finding Algorithm Visualiser')
        self.grid = [[' ' for i in range(self.cols)] for j in range(self.rows)]
        self.run = True
        self.start = None
        self.end = None
        self.diagonal_traversal = False
        self.path = []

    def main(self):
        while self.run:
            if self.diagonal_traversal:
                pygame.display.set_caption('Diagonal = True')
            else:
                pygame.display.set_caption('Diagonal = False')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                key = pygame.mouse.get_pressed()
                if key[0]:
                    if not self.start:
                        x,y = pygame.mouse.get_pos()
                        self.start = (y // (self.height // self.rows),x // (self.width // self.cols))
                        self.grid[self.start[0]][self.start[1]] = 'S'
                    elif not self.end:
                        x,y = pygame.mouse.get_pos()
                        self.end = (y // (self.height // self.rows),x // (self.width // self.cols))
                        self.grid[self.end[0]][self.end[1]] = 'E'
                    elif self.start and self.end:
                        x,y = pygame.mouse.get_pos()
                        self.pos = (y // (self.height // self.rows),x // (self.width // self.cols))
                        if self.pos != self.start and self.pos != self.end:
                            self.grid[self.pos[0]][self.pos[1]] = '#'
                elif key[2]:
                    x,y = pygame.mouse.get_pos()
                    row,col = (y // (self.height // self.rows),x // (self.width // self.cols))
                    if (row,col) == self.start:
                        self.start = None
                        self.grid[row][col] = ' '
                    elif (row,col) == self.end:
                        self.end = None
                        self.grid[row][col] = ' '
                    else:
                        self.grid[row][col] = ' '
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.start and self.end:
                        neighbours = return_neighbours(self.grid,self.diagonal_traversal)
                        path = bfs(neighbours,self.start,self.end)
                        if path:
                            reconstruct_path(self.grid,path)
                    elif event.key == pygame.K_c:
                        self.reset()
                    elif event.key == pygame.K_r:
                        self.remove_path()
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        if self.diagonal_traversal:
                            self.diagonal_traversal = False
                        else:
                            self.diagonal_traversal = True

            self.draw(self.display)
            pygame.display.update()

        pygame.quit()

    def reset(self):
        self.start = None
        self.end = None
        self.grid = [[' ' for i in range(self.cols)] for j in range(self.rows)]

    def remove_path(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == '*':
                    self.grid[i][j] = ' '

    def draw(self,win):
        win.fill((255,255,255))
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 'S':
                    pygame.draw.rect(win,(255,0,0),(j * (self.width // self.cols),i * (self.height // self.rows),self.width // self.cols,self.height // self.rows))
                elif self.grid[i][j] == 'E':
                    pygame.draw.rect(win,(255,0,0),(j * (self.width // self.cols),i * (self.height // self.rows),self.width // self.cols,self.height // self.rows))
                elif self.grid[i][j] == '#':
                    pygame.draw.rect(win,(0,0,0),(j * (self.width // self.cols),i * (self.height // self.rows),self.width // self.cols,self.height // self.rows))
                elif self.grid[i][j] == '*':
                    pygame.draw.rect(win,(255,255,0),(j * (self.width // self.cols),i * (self.height // self.rows),self.width // self.cols,self.height // self.rows))
        for i in range(self.cols):
            for j in range(self.rows):
                pygame.draw.rect(win,(100,100,100),(j * (self.width // self.cols),i * (self.height // self.rows),self.width // self.cols,self.height // self.rows),1)

vis = Visualizer(750,750,25,25)
vis.main()
