from pygame.math import Vector2; import pygame, sys, random
class player:
    def __init__(self):
        self.position = Vector2(20, 20)
        self.color = [0, 50, 200]
        self.speed = 1.5
    
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

        self.position.x = max(self.position.x, 15)
        self.position.x = min(self.position.x, 1000 - 15)
        self.position.y = max(self.position.y, 15)
        self.position.y = min(self.position.y, 700 -  15)

class enemies:
    def __init__(self):
        self.enemiesPositions = []
    
    def spawnEnemy(self):
        enemy_position = [random.randint(5, game.screenWidth - 20), random.randint(5, game.screenHeight - 20)]
        enemy_rect = pygame.Rect(enemy_position[0], enemy_position[1], 25, 25)
        self.enemiesPositions.append(enemy_rect)
        # print(f"Enemies are at: {self.enemiesPositions}") # Debugging print statement
        
    def drawEnemies(self):
        for enemy in self.enemiesPositions:
            pygame.draw.rect(screen, [255,  0,  0], [enemy[0], enemy[1],  25,  25])
        
    def getEnemiesPos(self):
        return self.enemiesPositions
    
class main:
    def __init__(self):
        self.player = player()
        self.enemies = enemies()
        self.kills = 0
        self.screenWidth = 1000
        self.screenHeight = 700
        self.positionsOfEnemies = self.enemies.getEnemiesPos()

    def movement(self):
        self.player.move()
        
    def drawElements(self):
        pygame.draw.circle(screen, self.player.color, self.player.position, 15)
        
    def checkCollision(self):
        playerRect = pygame.Rect(self.player.position.x, self.player.position.y,  15,  15)
        print(self.positionsOfEnemies)
        for enemy in self.positionsOfEnemies:
            print(f"Enemy Rect: {enemy}")  # Debugging print statement
            if playerRect.colliderect(enemy):
                print("Collision detected!")  # Debugging print statement
                self.gameOver()
     
    def gameOver(self):
        pygame.QUIT
        sys.exit()

pygame.init()

game = main()
player = player()
enemies = enemies()

screen = pygame.display.set_mode([game.screenWidth, game.screenHeight])
clockSpeed = 60
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 10)
ENEMY_SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ENEMY_SPAWN_EVENT, 1000) # random.randint(900, 4500)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            sys.exit()

        if event.type == SCREEN_UPDATE:
            game.movement()
            game.checkCollision()
        
        if event.type == ENEMY_SPAWN_EVENT:
            enemies.spawnEnemy()

    screen.fill([25, 5, 75])
    game.drawElements()
    enemies.drawEnemies()
    
    pygame.display.update()
    clock.tick(clockSpeed)
