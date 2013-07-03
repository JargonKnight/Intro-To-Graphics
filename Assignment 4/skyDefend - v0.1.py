#Author: Jesse Higgins
#Last Modified By: Jesse Higgins
#Date Last Modified: Wednesday June 26th 2013

"""Program Description: This is a side-scroller game. 

Version: 0.1 - *Beginning with creating the background image which will
                act as a parallax background
"""
    
import pygame, random
pygame.init()

screen = pygame.display.set_mode((960, 480))
    
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Parallax.jpg")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dy = 5
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
        
        
        allSprites = pygame.sprite.OrderedUpdates(bgImage)
        clock = pygame.time.Clock()
        keepGoing = True
        while keepGoing:
            clock.tick(30)
            pygame.mouse.set_visible(False)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                    
                
            
            allSprites.clear(screen, background)
            allSprites.update()
            allSprites.draw(screen)
            
            pygame.display.flip()
        
        pygame.mouse.set_visible(True)
        
if __name__ == "__main__":
    main()
