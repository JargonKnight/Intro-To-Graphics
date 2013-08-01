
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
        if self.rect.left > 2000:
            self.rect.left =  -1000
        if self.rect.left < -1000:
            self.rect.left = 2000
            
    def setDir(self):
        if self.dir == "left":
           self.rect.centerx = 2000
           self.dx = -10

        else:
            self.rect.centerx = -1000
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
        self.rect.center = (20, 490)
        self.frame = 0
        self.jumpUp = False
        self.jumpDown = False
        self.jumpRight = False
        self.jumpLeft = False
        self.animation = True
        self.direction = ""
      
        
    def loadImages(self):
        self.imageStand = pygame.image.load("FroggerJump/Frogger_Right0.gif")
        
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
            self.dx = 4
            
        self.imagesJumpLeft = []
        for i in range(5):
            imgName = "FroggerJump/Frogger_Left%d.gif" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesJumpLeft.append(tmpImage)
            self.counter = 100
            self.dy = 3
            self.dx = 4
            
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
        if self.rect.top < 320:
            self.rect.center = (self.rect.centerx, 335)
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

class Sidewalk(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.image = pygame.image.load("Resources/sidewalk.png")
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
        
        
class Sewers(pygame.sprite.Sprite):
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
        self.imageStand = pygame.image.load("Resources/Sewers/sewer - 1.png")
        
        self.imagesSewers = []
        for i in range(1,10):
            imgName = "Resources/Sewers/sewer - %d.png" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesSewers.append(tmpImage)
            self.counter = 100
        
        
    def update(self):
        self.counter += 1
        if self.counter > 5:
            self.frame += 1
            if self.frame >= len(self.imagesSewers):
                self.frame = 0
                self.animation = True
            self.image = self.imagesSewers[self.frame]
            self.counter = 0


class CityGirl(pygame.sprite.Sprite):
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
        self.dy = 3
        
    def LoadImages(self):
        self.imageStand = pygame.image.load("FroggerEnemies/Girl/girl - 1.png")
        
        self.imagesGirlWalk = []
        for i in range(1,4):
            imgName = "FroggerEnemies/Girl/girl - %d.png" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesGirlWalk.append(tmpImage)
            self.counter = 100
        
        
    def update(self):
        self.counter += 1
        self.rect.centery -= self.dy
        if self.rect.bottom < 305:
            self.rect.centery = screen.get_height() + 400
            
        if self.counter > 5:
            self.frame += 1
            if self.frame >= len(self.imagesGirlWalk):
                self.frame = 0
                self.animation = True
            self.image = self.imagesGirlWalk[self.frame]
            self.counter = 0


class CityChef(pygame.sprite.Sprite):
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
        self.dy = 3
        
    def LoadImages(self):
        self.imageStand = pygame.image.load("FroggerEnemies/Chef/chef - 1.png")
        
        self.imagesChefWalk = []
        for i in range(1,4):
            imgName = "FroggerEnemies/Chef/chef - %d.png" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesChefWalk.append(tmpImage)
            self.counter = 100
        
        
    def update(self):
        self.counter += 1
        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.rect.centery = 265
            
        if self.counter > 5:
            self.frame += 1
            if self.frame >= len(self.imagesChefWalk):
                self.frame = 0
                self.animation = True
            self.image = self.imagesChefWalk[self.frame]
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
 
class Background(pygame.sprite.Sprite):
    def __init__(self, pic, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(pic)
        self.rect = self.image.get_rect()
        self.rect.left = posx
        self.rect.top = posy

def main():
    
    pygame.display.set_caption("Leapy")

    background = pygame.Surface(screen.get_size())
    background.fill((0,0,0))
    screen.blit(background, (0,0))

    counter = 0
    x = 85

    bgImage = Background("Resources/houseBackground.png", 0,0)
    bgImage2 = Background("Resources/street2.png", 0, 320)
    crossing = Background("Resources/streetcrossing.png", 1100, 320)
    scoreboard = Scoreboard()
    sidewalk = Sidewalk(0,305)
    sidewalk2 = Sidewalk(1000,305)

    citygirl1 = CityGirl(1175, screen.get_height() + 200)
    citychef1 = CityChef(1575, 290)

    citycar1 = Cars("FroggerEnemies/citycar_right.png", "right", 615)
    citycar2 = Cars("FroggerEnemies/citycar_left.png", "left", 370)    
    
    frogger = Frogger()
    
    label = Label()
    label.text = "***LEVEL 3***"
    label.center = (500,300)
    
    sewer1 = Sewers(240, 370)
    sewer2 = Sewers(500, 490)
    sewer3 = Sewers(800, 615)
    sewer4 = Sewers(1575, 415)
    sewer5 = Sewers(1575, 585)
    sewer6 = Sewers(1175, 415)
    sewer7 = Sewers(1175, 585)
    sewer8 = Sewers(1375, 490)
    
    
    Horn = pygame.mixer.Sound("FroggerSounds/horn.ogg")
    Squish = pygame.mixer.Sound("FroggerSounds/Squish.ogg")
    BgMusic = pygame.mixer.Sound("FroggerSounds/bgMusicLevel2.ogg")
    bgMusic2 = pygame.mixer.Sound("FroggerSounds/SonicMusicForFrogger.ogg")
    sewerCollect = pygame.mixer.Sound("FroggerSounds/CoinCollect.ogg")
    BgMusic.play(-1)
    bgMusic2.play(-1)

    allSprites = pygame.sprite.OrderedUpdates(sidewalk,sidewalk2, bgImage, bgImage2, crossing)        
    allcityCars = pygame.sprite.Group(citycar1, citycar2)
    allcityFolk = pygame.sprite.Group(citygirl1, citychef1)
    allPlayers = pygame.sprite.Group(frogger)    
    allLabels = pygame.sprite.Group(label)
    allSewers = pygame.sprite.Group(sewer1, sewer2, sewer3, sewer4, sewer5, sewer6, sewer7, sewer8)
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
                
                
        if pygame.sprite.spritecollide(frogger, allcityCars, False):
            Squish.play()
            Horn.play()
            frogger.rect.center = (20, 490)

            decreaseLives(livesSprite, scoreboard)

        if pygame.sprite.spritecollide(frogger, allcityFolk, False):
            Squish.play()
            frogger.rect.center = (20, 490)

            decreaseLives(livesSprite, scoreboard)
          

        for sewer in pygame.sprite.spritecollide(frogger,allSewers, False, False):

            allSewers.remove(sewer)
            sewerCollect.play()
            print pygame.sprite.Group.sprites(allSewers)

            if pygame.sprite.Group.sprites(allSewers) == []:
                for car in pygame.sprite.Group(allcityCars):
                    allcityCars.remove(car)
                for person in pygame.sprite.Group(allcityFolk):
                    allcityFolk.remove(person)                   
                

        if frogger.rect.right >= screen.get_width():
            if pygame.sprite.Group.sprites(allSewers) == []:
                level = -1
                BgMusic.stop()
                bgMusic2.stop()
                keepGoing = False
            else:
                frogger.rect.centerx = (screen.get_width() - 15)
        
        if scoreboard.lives == 0:
            level = -1
            BgMusic.stop()
            bgMusic2.stop()
            keepGoing = False

        if frogger.rect.centerx >= 500:
            
            if bgImage.rect.right > 1000:
                for item in pygame.sprite.Group(allSprites):
                    item.rect.centerx -= 5
                frogger.rect.centerx -= 5
                for sewer in pygame.sprite.Group(allSewers):
                    sewer.rect.centerx -= 5
                for cityPerson in pygame.sprite.Group(allcityFolk):
                    cityPerson.rect.centerx -= 5

        if frogger.rect.centerx <= 500:
            if bgImage.rect.left < 0:
                for item in pygame.sprite.Group(allSprites):
                    item.rect.centerx += 5
                frogger.rect.centerx += 5
                for sewer in pygame.sprite.Group(allSewers):
                    sewer.rect.centerx += 5
                for cityPerson in pygame.sprite.Group(allcityFolk):
                    cityPerson.rect.centerx += 5
                
 
        if citychef1.rect.centery >= 265 and citychef1.rect.centery <= 415:
            if citycar2.rect.left > crossing.rect.right:
                citycar2.rect.left = crossing.rect.right + 400
            
            
        allSprites.clear(screen, background)
        allcityCars.clear(screen, background)
        allcityFolk.clear(screen, background)
        allSewers.clear(screen, background)
        allPlayers.clear(screen, background)
        allLabels.clear(screen, background)
        livesSprite.clear(screen, background)
        scoreboardSprite.clear(screen, background)
        
        allSewers.update()
        allcityFolk.update()
        allcityCars.update()
        allSprites.update()
        allPlayers.update()
        allLabels.update()
        livesSprite.update()
        scoreboardSprite.update()
        

        allSprites.draw(screen)
        allcityCars.draw(screen)
        allcityFolk.draw(screen)
        allSewers.draw(screen)
        allPlayers.draw(screen)
        allLabels.draw(screen)
        livesSprite.draw(screen)
        scoreboardSprite.draw(screen)
        
        pygame.display.flip()

    return level
    
