
from pygame.math import Vector2; import pygame, sys, random

class rooms:
    def __init__(self):
        self.roomSeed = 0
        self.walls = []
        self.numOfRooms = 10
        self.i = None

    def generateRoom(self):
        screenWidth = 1000
        screenHeight = 750

        for _ in range(self.numOfRooms):
            x = random.randint(0, screenWidth)
            y = random.randint(50, screenHeight)
            if random.choice([True, False]):
                width = 10
                height = random.randint(50, 400)
            else:
                width = random.randint(50, 400)
                height = 10
            self.walls.append([x, y, width, height])
        
    def drawRoom(self):
        for wall in self.walls:
            pygame.draw.rect(screen, [250, 25, 50], wall)

    def getWalls(self):
        return self.walls

class PLAYER1:
    def __init__(self):
        self.position = Vector2(20, 20)
        self.color = [70, 70, 170]
        self.speed = 2
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.position.y -= self.speed
        if keys[pygame.K_s]:
            self.position.y += self.speed
        if keys[pygame.K_a]:
            self.position.x -= self.speed
        if keys[pygame.K_d]:
            self.position.x += self.speed

        # Boundary checks
        self.position.x = max(self.position.x, 20)
        self.position.x = min(self.position.x, 1000 - 20)
        self.position.y = max(self.position.y, 20)
        self.position.y = min(self.position.y, 750 -  20)

class MAIN:
    def __init__(self):
        self.player1 = PLAYER1()
        self.rooms = rooms()
    
    def movement(self):
        self.player1.move()
        
    def drawElements(self):
        pygame.draw.circle(screen, self.player1.color, self.player1.position, 20)
        self.rooms.drawRoom()
        
    def checkCollision(self):
        playerRect = pygame.Rect(self.player1.position.x -  10, self.player1.position.y -  10,  20,  20)
        if len(self.rooms.walls) <=  10:
            self.rooms.generateRoom()
        for wall in self.rooms.getWalls():
            if playerRect.colliderect(wall):
                self.gameOver()
            
    def gameOver(self):
        pygame.QUIT
        sys.exit()

pygame.init()

screen = pygame.display.set_mode([1000, 750])
clockSpeed = 60
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 10)
game = MAIN()
player1 = PLAYER1()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            sys.exit()

        if event.type == SCREEN_UPDATE:
            game.movement()
            game.checkCollision()

    screen.fill([20, 20, 0])
    game.drawElements()
    
    pygame.display.update()
    clock.tick(clockSpeed)