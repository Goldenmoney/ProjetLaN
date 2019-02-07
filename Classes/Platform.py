import pygame
pygame.init()

Display_Width = 1200
Display_Height = 675
Display = pygame.display.set_mode((Display_Width,Display_Height))

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,type="platform"):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        if self.type == "platform":
            plat = pygame.image.load("images/platform.png").convert_alpha()
        elif self.type == "trampoline":
            plat = pygame.image.load("images/trampoline.png").convert_alpha()
        width, height = plat.get_rect().size
        plat = pygame.transform.scale(plat,(int(width*0.84),int(height*0.84)))
        width, height = plat.get_rect().size
        hitbox = pygame.transform.scale(plat,(int(width),int(height*0.5)))
        h_width, h_height = hitbox.get_rect().size
        self.rect = hitbox.get_rect()
        self.rect.move(0,height-h_height)
        self.rect.x = x
        self.rect.y = y
        self.image = plat
