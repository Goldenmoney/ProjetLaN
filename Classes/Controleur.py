
import pygame
from pygame.locals import *
pygame.init()
from Classes.Level import *
from Classes.Player import *
from Classes.Lancerocket import *
from Classes.Projectile import *
import time
import sys #module systeme
from Classes.Piece import *
from threading import Timer

Display_Width = 1024
Display_Height = 768

#==============================================================================#
#=============================== IMAGES =======================================#
"""Ajout des images menu"""
background = pygame.image.load("images/background.png").convert_alpha()
titre = pygame.image.load("images/titre.png").convert_alpha()
jouer0 = pygame.image.load("images/jouer.png").convert_alpha()
jouer = pygame.transform.scale(jouer0, (300, 100))
options0 = pygame.image.load("images/options.png").convert_alpha()
options = pygame.transform.scale(options0, (300, 100))
credits0 = pygame.image.load("images/credits.png").convert_alpha()
credits = pygame.transform.scale(credits0, (300, 100))
quitter0 = pygame.image.load("images/quitter.png").convert_alpha()
quitter = pygame.transform.scale(quitter0, (300, 100))

"""Ajout des images options"""
choixlvl = pygame.image.load("images/choixlvl.png").convert_alpha()
lvl_10 = pygame.image.load("images/1.png").convert_alpha()
lvl_1 = pygame.transform.scale(lvl_10, (300, 100))
lvl_20 = pygame.image.load("images/2.png").convert_alpha()
lvl_2 = pygame.transform.scale(lvl_20, (300, 100))
lvl_30 = pygame.image.load("images/3.png").convert_alpha()
lvl_3 = pygame.transform.scale(lvl_30, (300, 100))

#==============================================================================#
#==============================================================================#

# A SUPPRIMER A L'AVENIR
# menu victoire
credit = pygame.image.load("img/credit.png").convert_alpha()
credi_en = pygame.image.load("img/crediten.png").convert_alpha()
lvl_suivant = pygame.image.load("img/levelsuivant.png").convert_alpha()
lvl_suivant_en = pygame.image.load("img/levelsuivanten.png").convert_alpha()

# menu credit
Creditfinal = pygame.image.load("img/creditfinal.png").convert_alpha()


# fond
fond_menu0 = pygame.image.load("img/fondmenu.png").convert_alpha()
fond_menu = pygame.transform.scale(fond_menu0, (Display_Width, Display_Height))
fond_menu = pygame.image.load("img/fondmenu.png").convert_alpha()
fond_base0 = pygame.image.load("img/fond.png").convert_alpha()
fond_base = pygame.transform.scale(fond_base0, (Display_Width, Display_Height))
titreaenlever = pygame.image.load("img/titre.png").convert_alpha()
Victoire = pygame.image.load("img/youwin.png").convert_alpha()

"""musique"""
##musique_jeux = pygame.mixer.music.load('music/musiqueenjeux.mp3')

#==============================================================================#
#============================= CLASSES MENUS ==================================#


# creation des variable de base
pygame.display.set_caption("CHICAGO ADVENTURE")
clock = pygame.time.Clock()
Display = pygame.display.set_mode((Display_Width,Display_Height))
global level_en_cours_numero
FPS = 60

# affiche menu principal
def Menu_Start():
    global level_en_cours_numero
    menuStart = True

    while menuStart:
        positionSouris = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if pla.collidepoint(positionSouris):
                    #Display.blit(play_en,(320,185)) # Image quand bouton enfoncé
                    pygame.display.update()
                    time.sleep(1)
                    Menu_niveau()

                if opt.collidepoint(positionSouris):
                    pygame.display.update()
                    time.sleep(1)
                    Menu_options()

                if quit.collidepoint(positionSouris):
                    pygame.display.update()
                    time.sleep(1)
                    pygame.quit()
                    sys.exit()

        Display.blit(background,(0,0))
        titr = Display.blit(titre,(0,0))
        pla = Display.blit(jouer,(362,335))
        opt = Display.blit(options,(362,460))
        quit =  Display.blit(quitter,(362,580))
        pygame.display.flip()


# affiche menu pour choix niveau
def Menu_niveau():
    global level_en_cours_numero
    MenuOptions = True

    pygame.key.set_repeat(400,30)
    while MenuOptions:
        posSouris = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if lvl1.collidepoint(posSouris):
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = 1
                    GameLoop()

                if lvl2.collidepoint(posSouris):
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = 2
                    GameLoop()


                if lvl3.collidepoint(posSouris):
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = 3
                    GameLoop()

        Display.blit(background,(0,0))
        Display.blit(choixlvl,(0,0))
        lvl1 = Display.blit(lvl_1,(50,320))
        lvl2 = Display.blit(lvl_2,(370,320))
        lvl3 =  Display.blit(lvl_3,(690,320))
        pygame.display.flip()

# affichage menu options
def Menu_options():
    global level_en_cours_numero
    menuOptions = True

    pygame.key.set_repeat(400,30)
    while menuOptions:
        mpos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if CredO.collidepoint(mpos):
                    pygame.display.update()
                    time.sleep(1)
                    Credit()

                if MenuO.collidepoint(mpos):
                    pygame.display.update()
                    time.sleep(1)
                    Menu_Start()

                if ExiO.collidepoint(mpos):
                    pygame.display.update()
                    time.sleep(1)
                    pygame.quit()
                    sys.exit()

        Display.blit(background,(0,0))
        CredO = Display.blit(credits,(362,335))
        #MenuO =  Display.blit(A MODIFIER,(362,335))
        ExiO = Display.blit(quitter,(362,460))
        pygame.display.flip()

# affiche credits
def Credit():
    global level_en_cours_numero
    menuCredits = True

    pygame.key.set_repeat(400,30)
    while menuCredits:
        mpos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                # if MenuC.collidepoint(mpos):
                #     Display.blit(Gameover_menu_en,(40,570))
                #     pygame.display.update()
                #     time.sleep(1)
                #     Menu_Start()


        Display.blit(background,(0,0))
        #RAJOUTER LES CREDITS DE CORENTIN
        pygame.display.flip()

#==============================================================================#
#==============================================================================#

# A SUPPRIMER A L'AVENIR
# affiche Menu_Victoire
def Menu_Victoire():
    global level_en_cours_numero
    MenuVictoire = True

    pygame.mixer.music.stop()
    pygame.mixer.music.load('music/musiquevictoire.mp3')
    pygame.mixer.music.play(-1)

    pygame.key.set_repeat(400,30)
    while MenuVictoire:
        posSouris = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if Suivant.collidepoint(posSouris):
                    Display.blit(lvl_suivant_en,(650,300))
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = level_en_cours_numero + 1
                    if level_en_cours_numero == 11:
                        level_en_cours_numero = 10
                    pygame.mixer.music.stop()
                    GameLoop()

                if CreditV.collidepoint(posSouris):
                    Display.blit(credi_en,(700,570))
                    pygame.display.update()
                    time.sleep(1)
                    Credit()


                if MenuV.collidepoint(posSouris):
                    Display.blit(Gameover_menu_en,(370,300))
                    pygame.display.update()
                    time.sleep(1)
                    pygame.mixer.music.stop()
                    Menu_Start()

        Display.blit(fond_base,(0,0))
        Display.blit(Victoire,(0,0))

        Suivant = Display.blit(lvl_suivant,(650,300))
        CreditV = Display.blit(credit,(700,570))
        #MenuV =  Display.blit(A MODIFIER,(370,300))
        pygame.display.flip()


def GameLoop():
    global level_en_cours_numero

    GameRun = True
    GameOver = False
    i = 0
    posPersoX = 0
    posPersoY = 0
    player = Player()
    level_list = []
    # append ajouter element a la fin
    level_list.append(Level_1(player))
    level_list.append(Level_2(player))
    level_list.append(Level_3(player))
    level_list.append(Level_4(player))
    level_list.append(Level_5(player))
    level_list.append(Level_6(player))
    level_list.append(Level_7(player))
    level_list.append(Level_8(player))
    level_list.append(Level_9(player))
    level_list.append(Level_10(player))
    level_list.append(Level_alea(player))

    pygame.mixer.music.stop()
    pygame.mixer.music.load('music/musiqueenjeux.mp3')
    pygame.mixer.music.play(-1)

    # grace a level_en_cours_numero(entier) on recupere la position dans la liste et donc le lvl dans la liste
    level_en_cours = level_list[level_en_cours_numero]

    player.level = level_en_cours
    sprite_bouge = pygame.sprite.Group()
    sprite_bouge.add(player)
    piece = Piece(Display)
    piece.randomize()
    piece.draw()



def GameLoop():
    global level_en_cours_numero

    GameRun = True
    GameOver = False

    vitesseX = 0
    vitesseY = 0
    spacePressed = False
    player = Player()
    level_list = []
    # append ajouter element a la fin
    level_list.append(Level_1(player))
    level_list.append(Level_2(player))
    level_list.append(Level_3(player))
    level_list.append(Level_4(player))
    level_list.append(Level_5(player))
    level_list.append(Level_6(player))
    level_list.append(Level_7(player))
    level_list.append(Level_8(player))
    level_list.append(Level_9(player))
    level_list.append(Level_10(player))
    level_list.append(Level_alea(player))

    pygame.mixer.music.stop()
    pygame.mixer.music.load('music/musiqueenjeux.mp3')
    pygame.mixer.music.play(-1)

    # grace a level_en_cours_numero(entier) on recupere la position dans la liste et donc le lvl dans la liste
    level_en_cours = level_list[level_en_cours_numero]

    player.level = level_en_cours
    sprite_bouge = pygame.sprite.Group()
    sprite_bouge.add(player)

    while GameRun:
            while GameOver == True:
                time.sleep(1)
                pygame.mixer.music.stop()
                Menu_gameover()


            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    vitesseX = -5

                if event.key == K_RIGHT:
                    vitesseX = 5

                if event.key == K_SPACE and player.auSol == True:
                    spacePressed = True


            if event.type == KEYUP:
                if event.key == K_LEFT:
                    vitesseX = 0
                if event.key == K_RIGHT:
                    vitesseX = 0
                if event.key == K_SPACE and spacePressed == True:
                        player.saut(-10)
                        spacePressed = False

            player.update(vitesseX,vitesseY)


            #collision_player_missile_mask =  pygame.sprite.spritecollide(player,level_en_cours.pro_list,False,pygame.sprite.collide_mask)
            #collision_player_missile = pygame.sprite.spritecollide(player,level_en_cours.pro_list,False)
            collision_player_fin = pygame.sprite.spritecollide(player,level_en_cours.portal,False)


            #if collision_player_missile:
            #    if collision_player_missile_mask:
            #        GameOver = True
            #        son_decolage.stop()

            if collision_player_fin:
                time.sleep(1)
                pygame.mixer.music.stop()
                Menu_Victoire()

            level_en_cours.update()
            level_en_cours.draw(Display)
            sprite_bouge.draw(Display)

            # rafraichi l'ecran
            pygame.display.update()


            # gere les FPS
            clock.tick(FPS)
