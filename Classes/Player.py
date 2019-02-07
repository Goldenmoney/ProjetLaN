import pygame
pygame.init()


Display_Width = 1024
Display_Height = 768

Display = pygame.display.set_mode((Display_Width,Display_Height))

# gravite = 0.5

"""image pour mouvement perso"""
move_image1 = pygame.image.load("move/guy1.png").convert_alpha()
move_image2 = pygame.image.load("move/guy2.png").convert_alpha()
move_image3 = pygame.image.load("move/guy3.png").convert_alpha()
move_image4 = pygame.image.load("move/guy4.png").convert_alpha()
move_image5 = pygame.image.load("move/guy5.png").convert_alpha()
move_image6 = pygame.image.load("move/guy6.png").convert_alpha()


imageWidth = 78
imageHeight = 110
move_image1 = pygame.transform.scale(move_image1,(imageWidth,imageHeight))
move_image2 = pygame.transform.scale(move_image2,(imageWidth,imageHeight))
move_image3 = pygame.transform.scale(move_image3,(imageWidth,imageHeight))
move_image4 = pygame.transform.scale(move_image4,(imageWidth,imageHeight))
move_image5 = pygame.transform.scale(move_image5,(imageWidth,imageHeight))
move_image6 = pygame.transform.scale(move_image6,(imageWidth,imageHeight))

move_image1_r = pygame.transform.flip(move_image1, True, False)
move_image2_r = pygame.transform.flip(move_image2, True, False)
move_image3_r = pygame.transform.flip(move_image3, True, False)
move_image4_r = pygame.transform.flip(move_image4, True, False)

class Player(pygame.sprite.Sprite):
    def __init__(self):
##        super().__init__()
        self.gravite = 0.5
        self.auSol = False
        self.rect = move_image1.get_rect()
        self.rect.y = 500
        self.rect.x = 0
        self.vitesseX = 0
        self.vitesseY = 0
        pygame.sprite.Sprite.__init__(self)
        self.animation_speed_init = 10
        self.animation_speed= self.animation_speed_init
        self.animation_list = [move_image1,move_image2,move_image3,move_image4]
        self.animation_list_r = [move_image1_r,move_image2_r,move_image3_r,move_image4_r]
        self.animation_position = 0
        self.animation_maximun = 3 #len(self.animation)-1
        self.image = move_image1
        self.update(1, 1)
        self.Gamelost = False



    # modifie le deplacement du joueur
    def update(self,vitesseX,vitesseY):
        self.vitesseX = vitesseX

        #change image par image
        self.animation_speed -= 1

        self.gravite()
        if self.rect.x < 950 and vitesseX == 5: #blocage à droite
            self.rect.x += self.vitesseX
        elif self.rect.x > -5 and vitesseX == -5: #blocage à gauche
            self.rect.x += self.vitesseX

        if self.rect.y < 0:
            self.vitesseY = 1
        self.rect.y += self.vitesseY
        
        if self.animation_speed == 0:
            if vitesseX == 5: #le personnage avance
                self.image = self.animation_list[self.animation_position]
                self.animation_speed = self.animation_speed_init
                #si on est sur la dernière image on remet la première
                if self.animation_position == self.animation_maximun:
                    self.animation_position = 0
                else: #sinon on augmente l'image courante
                    self.animation_position += 1

            elif vitesseX == -5: #le personnage avance
                self.image = self.animation_list_r[self.animation_position]
                self.animation_speed = self.animation_speed_init
                #si on est sur la dernière image on remet la première
                if self.animation_position == self.animation_maximun:
                    self.animation_position = 0
                else: #sinon on augmente l'image courante
                    self.animation_position += 1
            elif vitesseY == -1:
                self.image = move_image6


            self.animation_speed = 10

        Display.blit(self.image,(self.rect.x,self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

    def setAuSol(self,auSol):
        self.auSol = auSol

    # gere le saut
    def saut(self,vitesseY):
        if self.auSol == True:
            self.auSol = False
            self.vitesseY = vitesseY
            self.update(self.vitesseX,self.vitesseY)

    # gere la gravité
    def is_gravite(self):
        if self.auSol == False:
            self.vitesseY += self.gravite
        else:
            self.vitesseY = 0

    def setGravite(self, grav):
        self.gravite = grav
