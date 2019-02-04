import pygame
pygame.init()


Display_Width = 1200
Display_Height = 675

Display = pygame.display.set_mode((Display_Width,Display_Height))
rocket = pygame.image.load("img/Rocket.png").convert_alpha()
rocket = pygame.transform.scale(rocket,(80,80))

class Lance_rocket(pygame.sprite.Sprite):
    def __init__(self,X_pro):
        pygame.sprite.Sprite.__init__(self)
        self.X_pro = X_pro


        self.rect = rocket.get_rect()
        self.rect.x = self.X_pro
        self.rect.y = -10
        self.image = rocket


    def Update(self):
        Display.blit(self.image,(self.rect))
