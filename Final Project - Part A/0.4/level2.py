
import pygame, sys
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1000, 640))

class Cars(pygame.sprite.Sprite):
    def __init__(self, pic, direction, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.image = pygame.image.load(pic)
        self.rect = self.image.get_rect()
        self.rect.centery = posy
        self.counter = 100
        self.dx = 10
        self.dir = direction
        self.setDir()
        
        
    def update(self):
        self.counter += 1
        self.rect.centerx += self.dx
        if self.rect.left > screen.get_width():
            self.rect.left = 0 
        if self.rect.left < 0:
            self.rect.left = 1000
            
    def setDir(self):
        if self.dir == "left":
           self.rect.centerx = 1000
           self.dx = -10

        else:
            self.rect.centerx = 0
            self.dx = 10
    
    def changeSpeed(self,speed):
        self.dx = speed
        
            
class Frogger(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.rect = self.image.get_rect()
        self.loadImages()
        self.image = self.imageStand
        self.rect = self.image.get_rect()
        self.rect.center = (450, 620)
        self.frame = 0
        self.jumpUp = False
        self.jumpDown = False
        self.jumpRight = False
        self.jumpLeft = False
        self.animation = True
        self.direction = ""
      
        
    def loadImages(self):
        self.imageStand = pygame.image.load("Resources/Frogger_Up0.gif")
        
        self.imagesJumpUp = []
        for i in range(5):
            imgName = "FroggerJump/Frogger_Up%d.gif" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesJumpUp.append(tmpImage)
            self.counter = 100
            self.dy = 3
            
        self.imagesJumpDown = []
        for i in range(5):
            imgName = "FroggerJump/Frogger_Down%d.gif" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesJumpDown.append(tmpImage)
            self.counter = 100
            self.dy = 3
            
        self.imagesJumpRight = []
        for i in range(5):
            imgName = "FroggerJump/Frogger_Right%d.gif" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesJumpRight.append(tmpImage)
            self.counter = 100
            self.dy = 3
            self.dx = 3
            
        self.imagesJumpLeft = []
        for i in range(5):
            imgName = "FroggerJump/Frogger_Left%d.gif" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesJumpLeft.append(tmpImage)
            self.counter = 100
            self.dy = 3
            self.dx = 3
            
    def update(self):
        Jump = pygame.mixer.Sound("FroggerSounds/FroggerJump.ogg")
        self.counter +=4
        if self.jumpUp:
            self.rect.centery -= self.dy
            if self.counter > 5.5:
                self.frame += 1
                if self.frame >= len(self.imagesJumpUp):
                    Jump.play()
                    self.frame = 0
                    self.animation = True
                    self.jumpUp = False
                self.image = self.imagesJumpUp[self.frame]
                self.counter = 0
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.animation:
            
            self.jumpUp = True
            self.counter = 0
            self.animation = False
            self.direction = "N"
            
        if self.jumpDown:
            self.rect.centery += self.dy
            if self.counter > 5.5:
                self.frame += 1
                if self.frame >= len(self.imagesJumpDown):
                    Jump.play()
                    self.frame = 0
                    self.animation = True
                    self.jumpDown = False
                self.image = self.imagesJumpDown[self.frame]
                self.counter = 0
        
        if keys[pygame.K_DOWN] and self.animation:
            self.jumpDown = True
            self.counter = 0
            self.animation = False
            self.direction = "S"
            
        if self.jumpRight:
            self.rect.centerx += self.dx
            if self.counter > 5.5:
                self.frame += 1
                if self.frame >= len(self.imagesJumpDown):
                    Jump.play()
                    self.frame = 0
                    self.animation = True
                    self.jumpRight = False
                self.image = self.imagesJumpRight[self.frame]
                self.counter = 0
      
        if keys[pygame.K_RIGHT] and self.animation:
            self.jumpRight = True
            self.counter = 0
            self.animation = False
            self.direction = "E"
            
        if self.jumpLeft:
            self.rect.centerx -= self.dx
            if self.counter > 5.5:
                self.frame += 1
                if self.frame >= len(self.imagesJumpLeft):
                    Jump.play()
                    self.frame = 0
                    self.animation = True
                    self.jumpLeft = False
                self.image = self.imagesJumpLeft[self.frame]
                self.counter = 0
        
        if keys[pygame.K_LEFT] and self.animation:
            self.jumpLeft = True
            self.counter = 0
            self.animation = False
            self.direction = "W"

        if self.rect.left < 0:
            self.rect.center = (15, self.rect.centery)
        if self.rect.right > screen.get_width():
            self.rect.center = ((screen.get_width() - 15), self.rect.centery)
        if self.rect.top < 0:
            self.rect.center = (self.rect.centerx, 15)
        if self.rect.bottom > screen.get_height():
            self.rect.center = (self.rect.centerx, (screen.get_height() - 18))

        
class Road(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.image = pygame.image.load("Resources/street.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy

class Walls(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.image = pygame.image.load("Resources/guardrail.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy

        
class Label(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("None", 50)
        self.text = ""
        self.center = (120,110)
        self.counter = 0
        
    def update(self):
        self.image = self.font.render(self.text, 1, (0,0,200))
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        self.counter += 1
        if self.counter > 60:
            self.text = ""
        
        
class Coins(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.rect = self.image.get_rect()
        self.LoadImages()
        self.image = self.imageStand
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy
        self.frame = 0
        
    def LoadImages(self):
        self.imageStand = pygame.image.load("FroggerCoins/FroggerCoin_0.gif")
        
        self.imagesCoinSpin = []
        for i in range(50):
            imgName = "FroggerCoins/FroggerCoin_%d.gif" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesCoinSpin.append(tmpImage)
            self.counter = 100
        
        
    def update(self):
        self.counter += 1
        if self.counter > 2:
            self.frame += 3
            if self.frame >= len(self.imagesCoinSpin):
                self.frame = 0
                self.animation = True
            self.image = self.imagesCoinSpin[self.frame]
            self.counter = 0

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.font = pygame.font.SysFont("None", 50)
        
    def update(self):
        self.text = "Lives:"
        self.image = self.font.render(self.text, 1, (0, 255, 0))
        self.rect = self.image.get_rect()
        
class livesImage(pygame.sprite.Sprite):
    def __init__(self, posx):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Resources/scoreFrogger.gif")
        self.rect = self.image.get_rect()
        self.rect.center = (posx, 20)
        


def decreaseLives(livesSprite, scoreboard):
    x = 85
    scoreboard.lives -= 1
            
    for live in pygame.sprite.Group(livesSprite):
        livesSprite.remove(live)
                
    for i in range (scoreboard.lives):
        lives = livesImage(x + 50)
        livesSprite.add(lives)#add each lives sprite to its group
        x += 50

def main():
    
    pygame.display.set_caption("Leapy")

    background = pygame.Surface(screen.get_size())
    background = pygame.image.load("Resources/concrete.png")
    screen.blit(background, (0,0))

    counter = 0
    x = 85
    
    car1 = Cars("FroggerEnemies/Car_right1.png", "right", 520)
    car2 = Cars("FroggerEnemies/Car_left1.png", "left", 440)
    car3 = Cars("FroggerEnemies/Car_right2.png", "right", 560)
    car4 = Cars("FroggerEnemies/Car_left2.png", "left", 480)
    car5 = Cars("FroggerEnemies/FroggerCar_left.gif", "left", 140)
    car6 = Cars("FroggerEnemies/FroggerCar3_left.gif", "left", 180)
    car7 = Cars("FroggerEnemies/FroggerCar2_right.gif", "right", 260)
    car8 = Cars("FroggerEnemies/FroggerCar4_right.gif", "right", 220)
 

    road1 = Road(500, 500)
    road2 = Road(500, 200)

    wall1 = Walls(40,350)
    wall2 = Walls(140,350)
    wall3 = Walls(340, 350)
    wall4 = Walls(440, 350)
    wall5 = Walls(640, 350)
    wall6 = Walls(740, 350)
    wall7 = Walls(940, 350)
    scoreboard = Scoreboard()
    
    
    frogger = Frogger()
    
    label = Label()
    label.text = "***LEVEL 2***"
    label.center = (500,300)
    
    coin1 = Coins(600, 220)
    coin2 = Coins(240, 350)
    coin3 = Coins(540, 350)
    coin4 = Coins(840, 350)
    coin5 = Coins(500, 520)
    
    
    Horn = pygame.mixer.Sound("FroggerSounds/horn.ogg")
    Squish = pygame.mixer.Sound("FroggerSounds/Squish.ogg")
    BgMusic = pygame.mixer.Sound("FroggerSounds/bgMusicLevel2.ogg")
    bgMusic2 = pygame.mixer.Sound("FroggerSounds/SonicMusicForFrogger.ogg")
    coinCollect = pygame.mixer.Sound("FroggerSounds/CoinCollect.ogg")
    BgMusic.play(-1)
    bgMusic2.play(-1)
        
    allCars = pygame.sprite.Group(car1, car2, car3, car4, car5, car6, car7, car8)
    allPlayers = pygame.sprite.Group(frogger)    
    allRoad = pygame.sprite.Group(road1, road2)
    allWalls = pygame.sprite.Group(wall1, wall2, wall3, wall4, wall5, wall6, wall7)
    allLabels = pygame.sprite.Group(label)
    allCoins = pygame.sprite.Group(coin1, coin2, coin3, coin4, coin5)
    livesSprite = pygame.sprite.Group()
    scoreboardSprite = pygame.sprite.Group(scoreboard)


    for i in range (scoreboard.lives):
        lives = livesImage(x + 50)
        livesSprite.add(lives)#add each lives sprite to its group
        x += 50
    
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level = -1
                BgMusic.stop()
                bgMusic2.stop()
                keepGoing = False
                
                
        if pygame.sprite.spritecollide(frogger, allCars, False):
            Squish.play()
            Horn.play()
            frogger.rect.center = (450, 620)

            decreaseLives(livesSprite, scoreboard)                
 

        if pygame.sprite.spritecollide(frogger, allWalls, False):
            if frogger.direction == "N":
                frogger.rect.center = (frogger.rect.centerx, (frogger.rect.centery + 5))
            if frogger.direction == "S":
                frogger.rect.center = (frogger.rect.centerx, (frogger.rect.centery - 5))
            if frogger.direction == "E":
                frogger.rect.center = ((frogger.rect.centerx - 5), frogger.rect.centery)
            if frogger.direction == "W":
                frogger.rect.center = ((frogger.rect.centerx + 5), frogger.rect.centery)

             

        for coin in pygame.sprite.spritecollide(frogger,allCoins, False, False):

            allCoins.remove(coin)
            coinCollect.play()
            print pygame.sprite.Group.sprites(allCoins)

            if pygame.sprite.Group.sprites(allCoins) == []:
                level = -1
                keepGoing = False
        
        if scoreboard.lives == 0:
            level = -1
            BgMusic.stop()
            bgMusic2.stop()
            keepGoing = False

        
        car1.changeSpeed(20)
        car4.changeSpeed(-25)
        car6.changeSpeed(-15)
        car8.changeSpeed(15)
        
        

        allRoad.clear(screen, background)           
        allCars.clear(screen, background)
        allCoins.clear(screen, background)
        allPlayers.clear(screen, background)
        allWalls.clear(screen, background)
        allLabels.clear(screen, background)
        livesSprite.clear(screen, background)
        scoreboardSprite.clear(screen, background)
        
        allCars.update()
        allCoins.update()
        allPlayers.update()
        allLabels.update()
        livesSprite.update()
        scoreboardSprite.update()
        

        allRoad.draw(screen)
        allCars.draw(screen)
        allWalls.draw(screen)
        allCoins.draw(screen)
        allPlayers.draw(screen)
        allLabels.draw(screen)
        livesSprite.draw(screen)
        scoreboardSprite.draw(screen)
        
        
        
        pygame.display.flip()

    return level
    
