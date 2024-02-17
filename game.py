
from pygame.math import Vector2; import pygame, sys, random

class wall:
    def __init__(self) -> None:
        self.wallType1 = pygame.Rect(200, 200, 10, 200)
        self.wallType2 = pygame.Rect(200, 200, 200, 10)
        self.wallType3 = pygame.Rect(200, 200, 100, 10)
        self.wallType4 = pygame.Rect(200, 200, 10, 100)
        self.wallType5 = pygame.Rect(200, 200, 150, 10)
        self.wallType6 = pygame.Rect(200, 200, 10, 150)
    
    def draw(self):
        pygame.draw.rect(screen, [225, 10, 25], self.wallType3)

class PLAYER1:
    def __init__(self) -> None:
        self.position = Vector2(100, 100)
        self.color = [70, 70, 170]
        self.speed = 3.5
    
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
    
    def movement(self):
        self.player1.move()
        
    def drawElements(self):
        pygame.draw.circle(screen, self.player1.color, self.player1.position, 20)
        wall.draw()
        
    def checkCollision(self):
        playerRect = pygame.Rect(self.player1.position.x -  10, self.player1.position.y -  10,  20,  20)
        wall = pygame.Rect(200,  200,  210,  210)
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
wall = wall()
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