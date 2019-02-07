import pygame
pygame.init()

Display_Width = 1200
Display_Height = 675
Display = pygame.display.set_mode((Display_Width,Display_Height))
platlist=[]

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,type="platform"):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        if self.type == "platform":
            plat = pygame.image.load("images/platform.png").convert_alpha()
            #width1, height1 = plat.get_rect().size
            #hitbox = pygame.transform.scale(plat,(int(width),int(height*0.6)))
        elif self.type == "trampoline":
            plat = pygame.image.load("images/trampoline.png").convert_alpha()
            #width1, height1 = plat.get_rect().size
            #hitbox = pygame.transform.scale(plat,(int(width),int(height*0.5)))

        width, height = plat.get_rect().size
        plat = pygame.transform.scale(plat,(int(width*0.84),int(height*0.84)))
        self.rect = plat.get_rect()
        #width2, height2 = hitbox.get_rect().size
        #self.rect = self.rect.move(0,height1-height2)
        self.rect.x = x
        self.rect.y = y
        self.image = plat


#    def Fall(self):
#        self.Y += self.chute

#        if self.Y >= Display_Height-10:
#            self.Y = 0
#            son_decolage.set_volume(0.1)
#            son_decolage.play()
        #self.rect = pygame.Rect(self.X,self.Y,20,40)
        #self.mask = pygame.mask.from_surface(self.image)
        #Display.blit(self.image,self.rect)
