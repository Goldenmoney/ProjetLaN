import pygame
pygame.init()


Display_Width = 1024
Display_Height = 768

Display = pygame.display.set_mode((Display_Width,Display_Height))
pro = pygame.image.load("img/missile.png").convert_alpha()

pro = pygame.transform.scale(pro,(20,40))

gravite = 0.5

"""image pour mouvement perso"""
move_image1 = pygame.image.load("move/segway1.png").convert_alpha()
move_image2 = pygame.image.load("move/segway2.png").convert_alpha()
move_image3 = pygame.image.load("move/segway3.png").convert_alpha()
move_image4 = pygame.image.load("move/segway4.png").convert_alpha()

move_image1 = pygame.transform.scale(move_image1,(64,128))
move_image2 = pygame.transform.scale(move_image2,(64,128))
move_image3 = pygame.transform.scale(move_image3,(64,128))
move_image4 = pygame.transform.scale(move_image4,(64,128))


class Player(pygame.sprite.Sprite):
    def __init__(self):
##        super().__init__()
        self.auSol = True
        self.rect = move_image1.get_rect()
        self.rect.y = 50
        self.rect.x = 0
        self.vitesseX = 0
        self.vitesseY = 0
        pygame.sprite.Sprite.__init__(self)
        self.animation_speed_init = 10
        self.animation_speed= self.animation_speed_init
        self.animation_list = [move_image1,move_image2,move_image3,move_image4]
        self.animation_position = 0
        self.animation_maximun = 3 #len(self.animation)-1
        self.image = move_image1
        self.update(1, 1)
        self.Gamelost = False



    # modifie le deplacement du joueur
    def update(self,vitesseX,vitesseY):
        self.vitesseX = vitesseX
        if self.rect.y >= 580:
            self.rect.y = 580
            self.auSol = True
        else:
            self.auSol = False
        self.animation_speed -= 1
        self.rect.x += self.vitesseX
        self.rect.y += self.vitesseY
        self.gravite()
        if self.animation_speed == 0:
            self.image = self.animation_list[self.animation_position]
            self.animation_speed = self.animation_speed_init
            if self.animation_position == self.animation_maximun:
                self.animation_position = 0
            else:
                self.animation_position += 1
        Display.blit(self.image,(self.rect.x,self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

    # gere le saut
    def saut(self,vitesseY):
        self.vitesseY = vitesseY

    # gere la gravité
    def gravite(self):
        if self.vitesseY < 30 and self.auSol == False:
            self.vitesseY += gravite
