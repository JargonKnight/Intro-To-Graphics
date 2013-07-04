#Author: Jesse Higgins
#Last Modified By: Jesse Higgins
#Date Last Modified: Tuesday July 3rd 2013

"""Program Description: This is a side-scroller game. 

Version: 0.3 - *After having a Player sprite added to the screen
                and allowing him to shoot missiles we will now
                add an enemy sprite
                and will add collision detection
             - *The enemy sprite will reset itself and continuing moving towards
                player sprite 
"""

import pygame, random
pygame.init()

screen = pygame.display.set_mode((960, 480))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemyPlane.png")
        self.rect = self.image.get_rect()
        self.dx = 5
        self.reset()
        
    def update(self):
        self.rect.left -= self.dx

    def reset(self):
        self.rect.center = (screen.get_width(), random.randrange(20, 460))
        
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
        self.dx = 10
        
    def update(self):
        self.rect.left += self.dx
    
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
        
def main():
        #initialize the screen
        pygame.display.set_caption("Sky Defender")

        background = pygame.Surface(screen.get_size())
        background.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        #create instances of classes
        bgImage = Background()
        plane = Plane()
        enemy = Enemy()

        #create the sprite groups
        allSprites = pygame.sprite.OrderedUpdates(bgImage)
        goodSprites = pygame.sprite.Group(plane)
        missileSprites = pygame.sprite.Group()
        enemySprites = pygame.sprite.Group(enemy)
        
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
                enemy.reset()
                missileSprites.remove(missile)
 
            
            allSprites.update()
            goodSprites.update()
            enemySprites.update()
            missileSprites.update()
            
            allSprites.draw(screen)
            goodSprites.draw(screen)
            enemySprites.draw(screen)
            missileSprites.draw(screen)
            
            pygame.display.flip()
        
        pygame.mouse.set_visible(True)
        
if __name__ == "__main__":
    main()
