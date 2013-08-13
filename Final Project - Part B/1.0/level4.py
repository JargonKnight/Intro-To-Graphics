
import pygame, sys, math, random
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1000, 640))        
            
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
        self.direction = "N"
      
    #loading the images into their own arrays
    def loadImages(self):
        self.imageStand = pygame.image.load("FroggerJump/Frogger_Up0.gif")
        
        self.imagesJumpUp = []
        for i in range(5):
            imgName = "FroggerJump/Frogger_Up%d.gif" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesJumpUp.append(tmpImage)
            self.counter = 100
            self.dy = 4
            
        self.imagesJumpDown = []
        for i in range(5):
            imgName = "FroggerJump/Frogger_Down%d.gif" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesJumpDown.append(tmpImage)
            self.counter = 100
            self.dy = 4
            
        self.imagesJumpRight = []
        for i in range(5):
            imgName = "FroggerJump/Frogger_Right%d.gif" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesJumpRight.append(tmpImage)
            self.counter = 100
            self.dy = 4
            self.dx = 4
            
        self.imagesJumpLeft = []
        for i in range(5):
            imgName = "FroggerJump/Frogger_Left%d.gif" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesJumpLeft.append(tmpImage)
            self.counter = 100
            self.dy = 4
            self.dx = 4

    #the update will take the keyboard input and iterate through the
    #corresponding array of images to represent the motion of Leapy
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
        if self.rect.top < 0:
            self.rect.center = (self.rect.centerx, 15)
        if self.rect.bottom > screen.get_height():
            self.rect.center = (self.rect.centerx, (screen.get_height() - 18))
        if self.rect.right > screen.get_width():
            self.rect.center = ((screen.get_width() - 15), self.rect.centery)


#other classes for the level design
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
        
class Fireball(pygame.sprite.Sprite):
    def __init__(self, posx, posy, direction):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        self.image = self.imageStand
        self.rect = self.image.get_rect()
        self.rect.center = (posx, posy)
        self.direction = direction
        self.attack = 10
        
        self.frame = 0
        pygame.mixer.init()

    def update(self):

        if self.direction == "N":
            self.counter += 1
            self.rect.centery -= 5
            if self.counter > 5:
                self.frame += 1
                if self.frame >= len(self.imagesFireballUp):
                    self.frame = 0
                self.image = self.imagesFireballUp[self.frame]
                self.counter = 0


        if self.direction == "S":
            self.counter += 1
            self.rect.centery += 5
            if self.counter > 5:
                self.frame += 1
                if self.frame >= len(self.imagesFireballDown):
                    self.frame = 0
                self.image = self.imagesFireballDown[self.frame]
                self.counter = 0
                
     

        if self.direction == "W":
            self.counter += 1
            self.rect.centerx -= 5
            if self.counter > 5:
                self.frame += 1
                if self.frame >= len(self.imagesFireballLeft):
                    self.frame = 0
                self.image = self.imagesFireballLeft[self.frame]
                self.counter = 0
            

        if self.direction == "E":
            self.counter += 1
            self.rect.centerx += 5
            if self.counter > 5:
                self.frame += 1
                if self.frame >= len(self.imagesFireballRight):
                    self.frame = 0
                self.image = self.imagesFireballRight[self.frame]
                self.counter = 0

        if self.rect.left < 0:
            self.kill()
        if self.rect.top < 0:
            self.kill()
        if self.rect.bottom > screen.get_height():
            self.kill()
        if self.rect.right > screen.get_width():
            self.kill()
                

    def loadImages(self):
        self.imageStand = pygame.image.load("FireBall/fireBallUp - 0.png")

        self.imagesFireballUp = []
        for i in range(2):
            imgName = "FireBall/fireBallUp - %d.png" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesFireballUp.append(tmpImage)
            self.counter = 100
            self.dy = 3
            
        self.imagesFireballDown = []
        for i in range(2):
            imgName = "FireBall/fireBallDown - %d.png" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesFireballDown.append(tmpImage)
            self.counter = 100
            self.dy = 3
            
        self.imagesFireballRight = []
        for i in range(2):
            imgName = "FireBall/fireBallRight - %d.png" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesFireballRight.append(tmpImage)
            self.counter = 100
            self.dy = 3
            self.dx = 4
            
        self.imagesFireballLeft = []
        for i in range(2):
            imgName = "FireBall/fireBallLeft - %d.png" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesFireballLeft.append(tmpImage)
            self.counter = 100
            self.dy = 3
            self.dx = 4

class FlyBomb(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.image = pygame.image.load("FlyBomb/flyBomb.png")
        self.rect = self.image.get_rect()
        self.speed = 5
        self.dir = 0
        self.dx = 0
        self.dy = 0
        self.x = posx
        self.y = posy
        self.distancex = 0
        self.distancey = 0
        self.rect.center = (self.x, self.y)
        self.attack = 10

    def update(self):
        self.calcPos()
        self.rect.center = (self.x, self.y)

    def changeDirection(self, posx, posy):
        self.distancex = self.rect.centerx - posx
        self.distancey = self.rect.centery - posy
        self.distancey *= -1
        
        theta = math.atan2(self.distancey, self.distancex)
        self.dir = theta * 180 / math.pi
        self.dir += 180
        
        radians = self.dir * math.pi / 180
        self.dx = self.speed * math.cos(radians)
        self.dy = self.speed * math.sin(radians)
        self.dy *= -1

    def calcPos(self):
        self.x += self.dx
        self.y += self.dy
        
    def rotate(self):
        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.image, self.dir)
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter
        
        
            
class Boss(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.rect = self.image.get_rect()
        self.LoadImages()
        self.image = self.imageStand
        self.rect = self.image.get_rect()
        self.frame = 0
        self.speed = 1
        self.dir = 0
        self.dx = 0
        self.dy = 0
        self.distancex = 0
        self.distancey = 0
        self.x = posx
        self.y = posy
        self.attack = 10
        
    def LoadImages(self):
        self.imageStand = pygame.image.load("CartoonFly/cartoonFly - 0.png")
        
        self.imagesSewers = []
        for i in range(1,5):
            imgName = "CartoonFly/cartoonFly - %d.png" % i
            tmpImage = pygame.image.load(imgName)
            self.imagesSewers.append(tmpImage)
            self.counter = 100
        
    def update(self):
        self.calcPos()
        self.rect.center = (self.x, self.y)
        self.counter += 1
        if self.counter > 5:
            self.frame += 1
            if self.frame >= len(self.imagesSewers):
                self.frame = 0
            self.image = self.imagesSewers[self.frame]
            self.counter = 0
            
    def changeDirection(self, posx, posy):
        self.distancex = self.rect.centerx - posx
        self.distancey = self.rect.centery - posy
        self.distancey *= -1
        
        theta = math.atan2(self.distancey, self.distancex)
        self.dir = theta * 180 / math.pi
        self.dir += 180
        
        radians = self.dir * math.pi / 180
        self.dx = self.speed * math.cos(radians)
        self.dy = self.speed * math.sin(radians)
        self.dy *= -1


        
#       dx = self.rect.centerx - posx
#        dy = self.rect.centery - posy
#        dy *= -1
#        radians = math.atan2(dy, dx)
#        self.dir = radians * 180 / math.pi
#        self.dir += 180

#        self.x += self.dx
#        self.y += self.dy

#        self.rect.center = (self.x, self.y)
        
 #       self.dx = self.speed * math.cos(radians)
#        self.dy = self.speed * math.sin(radians)
#        self.dy *= -1
    
    def calcPos(self):
        self.x += self.dx
        self.y += self.dy
    def reset(self, posx, posy):
        self.x = posx
        self.y = posy
        

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.froggerHealth = 100
        self.bossHealth = 100
        self.font = pygame.font.SysFont("None", 50)
        
    def update(self):
        self.text = "Frogger Health: %d" % (self.froggerHealth) + "                                    Boss Health:  %d" % (self.bossHealth)
        self.image = self.font.render(self.text, 1, (0, 255, 0))
        self.rect = self.image.get_rect()
        
class livesImage(pygame.sprite.Sprite):
    def __init__(self, posx):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Resources/scoreFrogger.gif")
        self.rect = self.image.get_rect()
        self.rect.center = (posx, 20)
        
 
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

    #create all the instances of the level
    bgImage = Background("Resources/houseBackground.png", 0,0)
    bgImage2 = Background("Resources/street2.png", 0, 320)
    crossing = Background("Resources/streetcrossing.png", 1100, 320)
    scoreboard = Scoreboard()
    sidewalk = Sidewalk(0,305)
    sidewalk2 = Sidewalk(1000,305)

    #create sounds
    bgBattle = pygame.mixer.Sound("FroggerSounds/battleMusic.ogg")
    Squish = pygame.mixer.Sound("FroggerSounds/Squish.ogg")
    fireAttack = pygame.mixer.Sound("FroggerSounds/fireBall.ogg")
    
    bgBattle.play(-1)
    
    frogger = Frogger()
    
    label = Label()
    label.text = "***BOSS BATTLE***"
    label.center = (500,300)

    #instanciate a boss
    boss = Boss(450,75)
    #cause him to start moving towards leapy
    boss.changeDirection(frogger.rect.centerx, frogger.rect.centery)

    #group all the sprites accordingly
    allFireballs = pygame.sprite.Group()
    allBosses = pygame.sprite.Group(boss)
    allFlyBombs = pygame.sprite.Group()
    allPlayers = pygame.sprite.Group(frogger)    
    allLabels = pygame.sprite.Group(label)
    livesSprite = pygame.sprite.Group()
    scoreboardSprite = pygame.sprite.Group(scoreboard)

    
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level = -1
                keepGoing = False

            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()

                if key[pygame.K_SPACE]:
                    fireball = Fireball(frogger.rect.centerx, frogger.rect.centery, frogger.direction)
                    allFireballs.add(fireball)

        #check collision between leapy and the boss character
        if pygame.sprite.spritecollide(frogger, allBosses, False):
            #reset level
            #remove all flybombs from the group and fireballs
            for flyBomb in pygame.sprite.Group(allFlyBombs):
                allFlyBombs.remove(flyBomb)
            for fireBall in pygame.sprite.Group(allFireballs):
                allFireballs.remove(fireBall)
            counter = 0
            frogger.rect.center = (450, 600)
            scoreboard.froggerHealth -= boss.attack
            boss.reset(450, 75)
            boss.changeDirection(frogger.rect.centerx, frogger.rect.centery)            

        for flyBomb in pygame.sprite.spritecollide(frogger, allFlyBombs, False, False):
            #remove all flybombs from the group and fireballs
            for flyBomb in pygame.sprite.Group(allFlyBombs):
                allFlyBombs.remove(flyBomb)
            for fireBall in pygame.sprite.Group(allFireballs):
                allFireballs.remove(fireBall)
            counter = 0
            frogger.rect.center = (450, 600)
            scoreboard.froggerHealth -= flyBomb.attack
            Squish.play()
            boss.reset(450, 75)
            boss.changeDirection(frogger.rect.centerx, frogger.rect.centery)            
 

        if pygame.sprite.Group.sprites(allFireballs) != []:
            #check collision between fireballs and flybombs and remove each that collide
            for fireBall in pygame.sprite.groupcollide(allFireballs, allFlyBombs, False, False):
                for flyBomb in pygame.sprite.groupcollide(allFlyBombs, allFireballs, False, False):
                    allFireballs.remove(fireBall)
                    allFlyBombs.remove(flyBomb)
                    fireAttack.play()

            for boss in pygame.sprite.groupcollide(allBosses, allFireballs, False, False):
                for fireBall in pygame.sprite.groupcollide(allFireballs, allBosses, False, False):
                    allFireballs.remove(fireBall)
                    print "BOSS ATTACKED"
                    scoreboard.bossHealth -= fireBall.attack
                    fireAttack.play()
            

        #if Leapys health reach 0, we end the game and go to gameover screen
        #by returning the level value of -1
        #because the project file runs the loop while Level > 0
        #also if bosses health reaches0 first, set level = win
        #which will trigger the win.py file
        if scoreboard.froggerHealth == 0:
            level = -1
            bgBattle.stop()
            keepGoing = False

        if scoreboard.bossHealth == 0:
            level = -2
            bgBattle.stop()
            keepGoing = False

                            
        if boss.rect.left < 0:
            boss.changeDirection(frogger.rect.centerx, frogger.rect.centery)
        if boss.rect.right > screen.get_width():
            boss.changeDirection(frogger.rect.centerx, frogger.rect.centery)
        if boss.rect.top < 0 :
            boss.changeDirection(frogger.rect.centerx, frogger.rect.centery)
        if boss.rect.bottom > screen.get_height():
            boss.changeDirection(frogger.rect.centerx, frogger.rect.centery)


        #random number to cause boss to change direction
        rand = random.randrange(1,1000)
        #increase counter for boss to fire fly bombs at a set interval
        counter += 1

        if rand > 950:
            boss.changeDirection(frogger.rect.centerx, frogger.rect.centery)

        if counter > 75:
            counter = 0
            flybomb = FlyBomb(boss.rect.centerx, boss.rect.centery)
            flybomb.changeDirection(frogger.rect.centerx, frogger.rect.centery)
            flybomb.rotate()
            allFlyBombs.add(flybomb)
            
        
        allFireballs.clear(screen, background)
        allPlayers.clear(screen, background)
        allBosses.clear(screen, background)
        allFlyBombs.clear(screen, background)
        allLabels.clear(screen, background)
        livesSprite.clear(screen, background)
        scoreboardSprite.clear(screen, background)
        
        allFireballs.update()
        allPlayers.update()
        allBosses.update()
        allFlyBombs.update()
        allLabels.update()
        livesSprite.update()
        scoreboardSprite.update()
        

        allFireballs.draw(screen)
        allPlayers.draw(screen)
        allBosses.draw(screen)
        allFlyBombs.draw(screen)
        allLabels.draw(screen)
        livesSprite.draw(screen)
        scoreboardSprite.draw(screen)
        
        pygame.display.flip()

    return level
    
