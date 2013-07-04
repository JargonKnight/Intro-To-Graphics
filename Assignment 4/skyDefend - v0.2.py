#Author: Jesse Higgins
#Last Modified By: Jesse Higgins
#Date Last Modified: Tuesday July 3rd 2013

"""Program Description: This is a side-scroller game. 

Version: 0.2 - *A Player sprite has been added to the side-scroller
             - *This player will be able to shoot missiles/bullets
"""

import pygame, random
pygame.init()

screen = pygame.display.set_mode((960, 480))

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
        screen = pygame.display.set_mode((960, 480))
 
        pygame.display.set_caption("Sky Defender")

        background = pygame.Surface(screen.get_size())
        background.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        
        bgImage = Background()
        plane = Plane()
        
        allSprites = pygame.sprite.OrderedUpdates(bgImage)
        goodSprites = pygame.sprite.OrderedUpdates(plane)
        
        clock = pygame.time.Clock()
        keepGoing = True
        while keepGoing:
            clock.tick(30)
            pygame.mouse.set_visible(False)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = pygame.mouse.get_pos()

                    if (mousex >= 110):
                        missile = Missile(110, mousey)
                    else:
                        
                        missile = Missile(mousex,mousey)
                        
                    missile.add(goodSprites)
                
            #check collision here

            
            allSprites.update()
            goodSprites.update()
            
            allSprites.draw(screen)
            goodSprites.draw(screen)
            
            pygame.display.flip()
        
        pygame.mouse.set_visible(True)
        
if __name__ == "__main__":
    main()
