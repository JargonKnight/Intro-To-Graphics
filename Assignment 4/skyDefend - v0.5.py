#Author: Jesse Higgins
#Last Modified By: Jesse Higgins
#Date Last Modified: Friday July 5th 2013

"""Program Description: This is a side-scroller game. 

Version: 0.5 - * Implementing score and players lives
             - * instruction screen
             
"""

import pygame, random
pygame.init()

screen = pygame.display.set_mode((960, 480))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemyPlane.png")
        self.rect = self.image.get_rect()
        self.reset()
        
    def update(self):
        self.rect.left -= self.dx
        if (self.rect.right <= 0):
            self.reset()

    def reset(self):
        self.rect.center = (random.randrange(screen.get_width()+50, screen.get_width() +200), random.randrange(20, 460))
        self.dx = random.randrange(6,10)
               
class Plane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("fighterPlane.png")
        self.rect = self.image.get_rect()
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (mousex, mousey)

        #handle boundary detection with plane sprite
        if (mousey <= 20):
            self.rect.center = (mousex, 20)
            
        if (mousey >= 460):
            self.rect.center = (mousex, 460)

        if (mousex <= 50):
            self.rect.center = (50, mousey)
            
        if (mousex >= 110):
            self.rect.center = (110, mousey)

        #handle the corner detections of plane sprite
        if (mousex <= 50) and (mousey <= 20):
            self.rect.center = (50, 20)

        if (mousex >110) and (mousey <= 20):
            self.rect.center = (110, 20)

        if (mousex <= 50) and (mousey >= 460):
            self.rect.center = (50, 460)

        if (mousex >= 110) and (mousey >= 460):
            self.rect.center = (110, 460)

class Missile(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("missile.png")
        self.rect = self.image.get_rect()
        self.rect.center = (posx,posy)
        self.dx = 7
        
    def update(self):
        self.rect.left += self.dx

class Explosion(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        
        self.STANDING = 0
        self.EXPLODING = 1
        
        self.loadImages()
        self.image = self.imageStand
        self.rect = self.image.get_rect()
        self.rect.center = (posx, posy)
        self.frame = 0
        self.delay = 2
        self.pause = 1
        self.state = self.STANDING
        pygame.mixer.init()
 #       self.moo = pygame.mixer.Sound("explosion.ogg")

    def update(self):
        if self.state == self.STANDING:
            self.image = self.imageStand
        else:
            self.pause += 1
            if self.pause > self.delay:
                #reset pause and advance animation
                self.pause = 0
                self.frame += 1
                if self.frame >= len(self.explodeImages):
                    self.frame = 0
                    self.state = self.STANDING
                    self.image = self.imageStand
                else:
                    self.image = self.explodeImages[self.frame]

    def loadImages(self):
        self.imageStand = pygame.image.load("Explosion/explosionSprite016.png")
        self.imageStand = self.imageStand.convert()
        transColor = self.imageStand.get_at((1, 1))
        self.imageStand.set_colorkey(transColor)

        self.explodeImages = []
        for i in range(16):
            imgName = "Explosion/explosionSprite0{0}.png".format(i)
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.explodeImages.append(tmpImage)
    
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Parallax.jpg")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 5
        self.reset()
        
    def update(self):
        self.rect.left -= self.dx
        if self.rect.left <= -1920:
            self.reset() 
    
    def reset(self):
        self.rect.left = 0


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.score = 0
        self.font = pygame.font.SysFont("None", 50)
        
    def update(self):
        self.text = "Lives:                             Score: %d" % (self.score)
        self.image = self.font.render(self.text, 1, (0, 255, 0))
        self.rect = self.image.get_rect()
        
class livesImage(pygame.sprite.Sprite):
    def __init__(self, posx):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("planeScore.png")
        self.rect = self.image.get_rect()
        self.rect.center = (posx, 20)

        
def game():
        #initialize the screen
        pygame.display.set_caption("Sky Defender")

        background = pygame.Surface(screen.get_size())
        background.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        #create instances of classes
        bgImage = Background()
        plane = Plane()
        scoreboard = Scoreboard()

        #x variable to increment placement of plane lives image
        x = 85
        
        #create the sprite groups
        allSprites = pygame.sprite.OrderedUpdates(bgImage)
        scoreboardSprite = pygame.sprite.Group(scoreboard)
        livesSprite = pygame.sprite.Group()
        goodSprites = pygame.sprite.Group(plane)
        missileSprites = pygame.sprite.Group()
        enemySprites = pygame.sprite.Group()
        explodeSprites = pygame.sprite.Group()

        #create the lives of the plane represented by mini
        #plane images
        for i in range (scoreboard.lives):
            lives = livesImage(x + 50)
            livesSprite.add(lives)#add each lives sprite to its group
            x += 50
        #create the enemy sprites
        for i in range (0, 4):
            enemy = Enemy()
            enemySprites.add(enemy)
            
        
        clock = pygame.time.Clock()
        keepGoing = True
        while keepGoing:
            clock.tick(30)
            pygame.mouse.set_visible(False)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False

                if event.type == pygame.MOUSEBUTTONUP:
                    mousex, mousey = pygame.mouse.get_pos()
                    #check on the release of the mouse the x position
                    #and release the missile at the center of the player sprite
                    if (mousex >= 110):
                        missile = Missile(110, mousey)
                    else:
                        missile = Missile(mousex,mousey)
                    #add the missile sprite to the missile group
                    missileSprites.add(missile)    

 

                
            #check collision here and remove any missiles that collide
            #with enemy sprites
            for missile in pygame.sprite.groupcollide(missileSprites, enemySprites, False,False):
                for enemy in pygame.sprite.groupcollide(enemySprites, missileSprites, False, False):
                    enemy.reset()
                    missileSprites.remove(missile)
                    scoreboard.score += 200


                    explosion = Explosion(missile.rect.right, missile.rect.top)
                    explosion.state = explosion.EXPLODING
                    explodeSprites.add(explosion)
 
            
            plane_collision = pygame.sprite.spritecollide(plane, enemySprites, False)
            if plane_collision:
                explosion = Explosion(plane.rect.right, plane.rect.top)
                explosion.state = explosion.EXPLODING
                explodeSprites.add(explosion)

                #reset x variable for re-creating the lives counter
                #for player represented by mini plane images
                x = 85
                
                #remove a life from player
                scoreboard.lives -= 1
                
                #give a bonus score to the player
                scoreboard.score += 500
                
                #remove all the livesSprites that exist each time the plane
                #loses a life
                for lives in pygame.sprite.Group(livesSprite):
                    livesSprite.remove(lives)
                    
                #then use the new lives value in scoreboard class
                #and re create that many livesSprites to represent it
                for i in range (scoreboard.lives):
                    lives = livesImage(x + 50)
                    livesSprite.add(lives)
                    x += 50
                    
                #end the game if he loses all his lives
                if scoreboard.lives <= 0:
                    keepGoing = False

                #reset all enemies and remove all missiles
                for enemy in pygame.sprite.Group(enemySprites):
                    enemy.reset()
                for missile in pygame.sprite.Group(missileSprites):
                    missileSprites.remove(missile)

                

            
            allSprites.update()
            scoreboardSprite.update()
            livesSprite.update()
            goodSprites.update()
            enemySprites.update()
            missileSprites.update()
            explodeSprites.update()
            
            allSprites.draw(screen)
            scoreboardSprite.draw(screen)
            livesSprite.draw(screen)
            goodSprites.draw(screen)
            enemySprites.draw(screen)
            missileSprites.draw(screen)
            explodeSprites.draw(screen)
            
            pygame.display.flip()
        
        pygame.mouse.set_visible(True)
        return scoreboard.score

        
def instructions(score):
    pygame.display.set_caption("Mail Pilot!")

    plane = Plane()
    background = Background()
    
    allSprites = pygame.sprite.Group(background, plane)
    insFont = pygame.font.SysFont(None, 50)
    insLabels = []
    instructions = (
    " *!* ~Sky Defend ~ *!*     Last Score: %d" % score ,
    "",
    "Instructions:  You are a Fighter Jet,",
    "taking on multiple incoming Enemy Planes.",
    "",
    "Shoot your missiles with your mouse",
    "to take the enemies out of the sky!",    
    "You may take out the enemies by crashing",
    "into them for a bigger score! But",
    "Keep an eye on your lives!.",
    "",
    "Best of Luck!",
    "",
    "click to start, escape to quit..."
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (0,0, 0))
        insLabels.append(tempLabel)
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
    
        allSprites.update()
        allSprites.draw(screen)

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
        
 #   plane.sndEngine.stop()    
    pygame.mouse.set_visible(True)
    return donePlaying

def main():
    donePlaying = False
    score = 0
    while not donePlaying:
        donePlaying = instructions(score)
        if not donePlaying:
            score = game()
 
  
if __name__ == "__main__":
    main()
