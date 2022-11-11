import pygame
import threading
from utils import *

class Visualiser:

    def __init__(self,width,height,rows,cols):
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.display = pygame.display.set_mode((self.width,self.height))
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.path = []
        self.queue = []
        self.start = None
        self.end = None
        self.run = True

    def main(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.start and self.end:
                            neighbours = return_neighbours(self.grid)
                            thread = threading.Thread(target=self.bfs,args=[neighbours,self.start,self.end])
                            thread.start()
                    elif event.key == pygame.K_r:
                        self.reset()
                key = pygame.mouse.get_pressed()
                if key[0]:
                    if self.start is None:
                        x,y = pygame.mouse.get_pos()
                        col,row = (x // (self.width // self.cols),y // (self.height // self.rows))
                        self.start = (row,col)
                        self.grid[row][col] = 'S'
                    elif self.end is None:
                        x,y = pygame.mouse.get_pos()
                        col,row = (x // (self.width // self.cols),y // (self.height // self.rows))
                        if self.start != (row,col):
                            self.end = (row,col)
                            self.grid[row][col] = 'E'
                    elif self.end and self.start:
                        x,y = pygame.mouse.get_pos()
                        col,row = (x // (self.width // self.cols),y // (self.height // self.rows))
                        if (row,col) != self.start and (row,col) != self.end:
                            self.grid[row][col] = '#'
                elif key[2]:
                    if self.start:
                        x,y = pygame.mouse.get_pos()
                        col,row = (x // (self.width // self.cols),y // (self.height // self.rows))
                        if self.grid[row][col] == 'S':
                            self.start = None
                            self.grid[row][col] = ' '
                        elif self.grid[row][col] == 'E':
                            self.end = None
                            self.grid[row][col] = ' '
                        else:
                            self.grid[row][col] = ' '
            self.draw(self.display)

        pygame.quit()
        
    def draw(self,win):
        win.fill((255,255,255))
        for index,row in enumerate(self.grid):
            for index2,col in enumerate(self.grid[index]):
                if col == '#':
                    pygame.draw.rect(win,(0,0,0),(index2 * (self.width // self.cols),index * (self.height // self.rows),self.width // self.cols,self.height // self.rows))
                elif col == 'S':
                    pygame.draw.rect(win,(255,0,0),(index2 * (self.width // self.cols),index * (self.height // self.rows),self.width // self.cols,self.height // self.rows))
                elif col == 'E':
                    pygame.draw.rect(win,(0,0,255),(index2 * (self.width // self.cols),index * (self.height // self.rows),self.width // self.cols,self.height // self.rows))                
                elif col == '*':
                    pygame.draw.rect(win,(255,255,0),(index2 * (self.width // self.cols),index * (self.height // self.rows),self.width // self.cols,self.height // self.rows))
                elif col == '+':
                    pygame.draw.rect(win,(128,0,128),(index2 * (self.width // self.cols),index * (self.height // self.rows),self.width // self.cols,self.height // self.rows))
        for row,col in self.path:
            self.grid[row][col] = '+'
        for row,col in self.queue:
            pygame.draw.rect(win,(0,255,0),(col * (self.width // self.cols),row * (self.height // self.rows),self.width // self.cols,self.height // self.rows))
        for i in range(0,self.height,self.height // self.rows):
            for j in range(0,self.width,self.width // self.cols):
                pygame.draw.rect(win,(128,128,128),(j,i,self.width // self.cols,self.height // self.rows),1)
        pygame.display.update()

    def reset(self):
        self.grid = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.path = []
        self.queue = []
        self.start,self.end = None,None

    def bfs(self,neighbours,start,end):
        visited = []
        self.queue = [start]
        predecessorNodes = {}

        while self.queue:
            if self.run:
                node = self.queue.pop(0)
                for neighbour in neighbours[node]:
                    if neighbour not in visited:
                        visited.append(neighbour)
                        self.queue.append(neighbour)
                        predecessorNodes[neighbour] = node
                        if self.end in predecessorNodes:
                            self.queue.clear()
                        row,col = neighbour
                        if (row,col) != start:
                            self.grid[row][col] = '*'
                        pygame.time.delay(15)
        if self.run:
            currentNode = end
            while currentNode != start:
                currentNode = predecessorNodes[currentNode]
                if currentNode != start and currentNode != end:
                    self.path.append(currentNode)
                pygame.time.delay(15)
                
vis = Visualiser(750,750,30,30)
vis.main()
