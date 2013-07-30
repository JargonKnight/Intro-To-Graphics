
import pygame
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1000, 640))

class Animals(pygame.sprite.Sprite):
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
        self.rect.center = (450, 600)
        self.frame = 0
        self.jumpUp = False
        self.jumpDown = False
        self.jumpRight = False
        self.jumpLeft = False
        self.animation = True
      
        
    def loadImages(self):
        self.imageStand = pygame.image.load("Resources/Frogger_Up0.gif")
        
        self.imagesJumpUp = []
        for i in range(5):
            imgName = "FroggerJump/Frogger_Up%d.gif" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesJumpUp.append(tmpImage)
            self.counter = 100
            self.dy = 5
            
        self.imagesJumpDown = []
        for i in range(5):
            imgName = "FroggerJump/Frogger_Down%d.gif" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesJumpDown.append(tmpImage)
            self.counter = 100
            self.dy = 5
            
        self.imagesJumpRight = []
        for i in range(5):
            imgName = "FroggerJump/Frogger_Right%d.gif" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesJumpRight.append(tmpImage)
            self.counter = 100
            self.dy = 5
            self.dx = 5
            
        self.imagesJumpLeft = []
        for i in range(5):
            imgName = "FroggerJump/Frogger_Left%d.gif" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesJumpLeft.append(tmpImage)
            self.counter = 100
            self.dy = 5
            self.dx = 5
            
    def update(self):
        Jump = pygame.mixer.Sound("FroggerSounds/FroggerJump.ogg")
        self.counter +=4
        if self.jumpUp:
            self.rect.centery -= self.dy
            if self.counter > 5.5:
                self.frame += 1
                if self.frame >= len(self.imagesJumpUp):
                    Jump.play()
                    print "In the frame test"
                    self.frame = 0
                    self.animation = True
                    self.jumpUp = False
                self.image = self.imagesJumpUp[self.frame]
                self.counter = 0
        
        keys = pygame.key.get_pressed()
        print self.animation
        if keys[pygame.K_UP] and self.animation:
            
            self.jumpUp = True
            self.counter = 0
            self.animation = False
            
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

        if self.rect.left < 0:
            self.rect.center = (15, self.rect.centery)
        if self.rect.right > screen.get_width():
            self.rect.center = ((screen.get_width() - 15), self.rect.centery)
        if self.rect.top < 0:
            self.rect.center = (self.rect.centerx, 15)
        if self.rect.bottom > screen.get_height():
            self.rect.center = (self.rect.centerx, (screen.get_height() - 18))
        
            
class Water(pygame.sprite.Sprite):
    def __init__(self,posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.image = pygame.image.load("Resources/Water.gif")
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy
        
class Bridge(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.image = pygame.image.load("Resources/Bridge.gif")
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy
    
class Grass(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.image = pygame.image.load("Resources/GrassGrow_0.gif")
        self.frame = 0
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy
        self.LoadImages()
        self.GrassGrow = False
        
        
    def LoadImages(self):
        self.imageStand = pygame.image.load("Resources/GrassGrow_0.gif")
        
        self.imagesGrassGrow = []
        for i in range(9):
            imgName = "MoreGrass/GrassGrow_%d.gif" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesGrassGrow.append(tmpImage)
            self.counter = 100
            
    def update(self):
        self.counter += 1
        if self.GrassGrow:
            if self.counter > 1:
                self.frame += 1
                if self.frame >= len(self.imagesGrassGrow):
                    self.frame = 0
                    self.counter = 0
                    self.GrassGrow = False
                self.image = self.imagesGrassGrow[self.frame]

    def reset(self):
        self.GrassGrow = True
        self.counter = 0  
        
class Label(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("None", 50)
        self.text = ""
        self.center = (120,110)
        self.counter = 0
        
    def update(self):
        self.image = self.font.render(self.text, 1, (0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        self.counter += 1
        if self.counter > 60:
            self.text = ""
        
        
        
class Walls(pygame.sprite.Sprite):
    def __init__(self, posx, posy, Length, Width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((Length, Width))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy
        
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
        #transColor = self.imageStand.get_at((1, 1))
        #self.imageStand.set_colorkey(transColor)
        
        self.imagesCoinSpin = []
        for i in range(50):
            imgName = "FroggerCoins/FroggerCoin_%d.gif" % i
            tmpImage = pygame.image.load(imgName)
            #transColor = tmpImage.get_at((10, 10))
            #tmpImage.set_colorkey(transColor)
            self.imagesCoinSpin.append(tmpImage)
            self.counter = 100
        
        
    def update(self):
        self.counter += 1
        if self.counter > 2:
            self.frame += 3
            if self.frame >= len(self.imagesCoinSpin):
                print "Coins Working"
                self.frame = 0
                self.animation = True
            self.image = self.imagesCoinSpin[self.frame]
            self.counter = 0
            
    
        
                
def main():
    
    pygame.display.set_caption("Leapy")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((43, 124, 36))
    screen.blit(background, (0,0))

    counter = 0
    level = 1
    
    animal1 = Animals("FroggerEnemies/FroggerGator0_right.gif", "right", 175)
    animal2 = Animals("FroggerEnemies/FroggerGator0_right.gif", "right", 400)
    animal3 = Animals("FroggerEnemies/FroggerGator0_left.gif", "left", 500)
    animal4 = Animals("FroggerEnemies/FroggerGator0_left.gif", "left", 35)
    human1 = Animals("FroggerEnemies/LawnMower0_left.gif", "left", 350)
    human2 = Animals("FroggerEnemies/LawnMower0_right.gif", "right", 225)
    human3 = Animals("FroggerEnemies/LawnMower0_left.gif", "left", 450)
    
    water = Water(-5, 100)
    water2 = Water(100, 100)
    water3 = Water(150, 100)
    water4 = Water(200, 100)
    water5 = Water(300, 100)
    water6 = Water(350, 100)
    water7 = Water(400, 100)
    water8 = Water(500, 100)
    water9 = Water(550, 100)
    water10 = Water(600, 100)
    water11 = Water(700, 100)
    water12 = Water(750, 100)
    water13 = Water(800, 100)
    water14 = Water(900, 100)
    water15 = Water(950, 100)
    water16 = Water(1000, 100)
    
    bridge = Bridge(50, 100)
    bridge2 = Bridge(250, 100)
    bridge3 = Bridge(450, 100)
    bridge4 = Bridge(650, 100)
    bridge5 = Bridge(850, 100)
    
    grass1 = Grass(500, 250)
    grass2 = Grass(200, 375)
    grass3 = Grass(600, 475)
    
    
    frogger = Frogger()
    
    label = Label()
    label.text = "***LEVEL 1***"
    label.center = (500,300)
    
    wall1 = Walls(500, -15, 1000, 25)
    wall2 = Walls(1015,-15, 25, 1400) 
    wall3 = Walls(500, 653, 1000, 25)
    wall4 = Walls(-15, -15, 25, 1400)
    
    coin1 = Coins(600, 200)
#    coin2 = Coins(200, 300)
#    coin3 = Coins(750, 25)
#    coin4 = Coins(750, 500)
    
    
    Squish = pygame.mixer.Sound("FroggerSounds/Squish.ogg")
    Splash = pygame.mixer.Sound("FroggerSounds/Splash.ogg")
    BgMusic = pygame.mixer.Sound("FroggerSounds/BgMusic.ogg")
    bgMusic2 = pygame.mixer.Sound("FroggerSounds/SonicMusicForFrogger.ogg")
    coinCollect = pygame.mixer.Sound("FroggerSounds/CoinCollect.ogg")
    BgMusic.play(-1)
    bgMusic2.play(-1)
        
    allAnimals = pygame.sprite.Group(animal1, animal2, animal3, animal4)
    allHumans = pygame.sprite.Group(human1, human2, human3)
    allPlayers = pygame.sprite.Group(frogger)    
    allWater = pygame.sprite.Group(water, water2, water3, water4, water5, water6, water7, water8, water9, water10, water11, water12, water13, water14, water15, water16)
    allBridge = pygame.sprite.Group(bridge, bridge2, bridge3, bridge4, bridge5)
    allGrass = pygame.sprite.Group(grass1, grass2, grass3)
    allLabels = pygame.sprite.Group(label)
    allWalls = pygame.sprite.Group(wall1, wall2, wall3, wall4)
    allCoins = pygame.sprite.Group(coin1)
    
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        if pygame.sprite.spritecollide(frogger, allAnimals, False):
            Squish.play()
            frogger.rect.centery = 600
            
        if pygame.sprite.spritecollide(frogger, allWater, False):
            Splash.play()
            frogger.rect.centery = 600

        for human in pygame.sprite.groupcollide(allHumans, allGrass, False, False):
            for grass in pygame.sprite.groupcollide(allGrass, allHumans, False, False):
                grass.reset()
                
 

        for coin in pygame.sprite.spritecollide(frogger,allCoins, False, False):

            allCoins.remove(coin)
            coinCollect.play()
            print pygame.sprite.Group.sprites(allCoins)

            if pygame.sprite.Group.sprites(allCoins) == []:
                keepGoing = False
        
        
        animal1.changeSpeed(20)
        animal2.changeSpeed(5)
        animal3.changeSpeed(-17)
        human1.changeSpeed(-20)
        
        
            
        allGrass.clear(screen, background)
        allAnimals.clear(screen, background)
        allHumans.clear(screen, background)
        allWater.clear(screen, background)
        allBridge.clear(screen, background)
        allWalls.clear(screen, background)
        allCoins.clear(screen, background)
        allPlayers.clear(screen, background)
        allLabels.clear(screen, background)
        
        allAnimals.update()
        allHumans.update()
        allCoins.update()
        allPlayers.update()
        allGrass.update()
        allLabels.update()
        
        
        allGrass.draw(screen)
        allAnimals.draw(screen)
        allHumans.draw(screen)
        allWater.draw(screen)
        allBridge.draw(screen)
        allCoins.draw(screen)
        allWalls.draw(screen)
        allPlayers.draw(screen)
        allLabels.draw(screen)
        
        
        
        pygame.display.flip()

    
    
