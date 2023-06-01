import random 
import tkinter as tk
from tkinter import *
from time import time, sleep

def initialisation():       # distribution des cartes et créations d'images
    joker=["+4","+4","jV","jV","4c","4c","jJ","jJ","sV","sV","+4","+4","sJ","sJ","4c","4c","jB","jB","sB","sB","jR","jR","sR","sR"]
    cartes=["9V","9V","8V","8V","7V","7V","6V","6V","5V","5V","4V","4V","3V","3V","2V","2V","1V","1V","0V","9J","9J","8J","8J","7J","7J","6J","6J","5J","5J","4J","4J","3J","3J","2J","2J","1J","1J","0J","9R","9R","8R","8R","7R","7R","6R","6R","5R","5R","4R","4R","3R","3R","2R","2R","1R","1R","0R","9B","9B","8B","8B","7B","7B","6B","6B","5B","5B","4B","4B","3B","3B","2B","2B","1B","1B","0B"]     
    random.shuffle (joker)  
    random.shuffle (cartes) 
     
    images_cartes = dict()
    for carte in set(cartes):
        image = "imagecarte/" + carte.lower() + ".png"
        images_cartes[carte] = tk.PhotoImage(file=image)
    talon=[cartes.pop()]
     
    image_joker = dict ()
    for carte in set (joker):
        image = "imagecarte/" + carte.lower() + ".png"
        image_joker[carte] = tk.PhotoImage(file=image)
 
    cartes.extend(joker)
    random.shuffle(cartes)
    images_cartes.update(image_joker)
    carte_joueur_1=[]       
    carte_joueur_2=[]         
    for i in range (7):        
        carte_joueur_1.append(cartes.pop())        
        carte_joueur_2.append(cartes.pop())         
    return images_cartes,joker,cartes,carte_joueur_1,carte_joueur_2,talon
 
def affichage_choix_couleur (): #  fenetre pour choisir une couleur apres un joker
    w = tk.Tk()
    # le tableau à afficher : [0, 1, 2, 3]
    tableau = [[0,1],[2,3]]
    # taille d'une "case"
    size = 100
    couleurs = {0: "green", 1: "blue", 2:"red", 3:"yellow"} # les 4 couleurs à utiliser
    can = tk.Canvas(w, width=200, height=200)# création canevas
    can.grid()
 
    # affichage du tableau de cette fenetre
    for j in range(2):
        for i in range(2) :
            can.create_rectangle(i * size,
                            j*size,
                            i * size + size,
                            j*size+size,
                            fill = couleurs[tableau[i][j]])
   
    def couleur(evt):      # renvoie couleur choisis suite a un joker
        pos_x = int(evt.x / size)
        pos_y = int(evt.y / size)
 
        if tableau[pos_x][pos_y] == 0:
            print ("V")
            nouvelle_couleur = ["+V"]
            w.destroy()
        elif tableau[pos_x][pos_y] == 1:
            print ("B")
            nouvelle_couleur = ["+B"]
            w.destroy()
        elif tableau[pos_x][pos_y] == 2:
            print ("R")
            nouvelle_couleur = ["+R"]
            w.destroy()
        elif tableau[pos_x][pos_y] == 3:
            print ("J")
            nouvelle_couleur = ["+J"]
            w.destroy()
     
    can.bind("<Button-1>", couleur) # binding de la fonction couleur sur le canevas
    w.mainloop()  # boucle principale
     
def deplacement_carte():
    global image, image_talon, images_cartes_joueur_1,carte_joueur_1, selection_carte, i
        # Suppression du tag pour que la carte ne puisse plus être cliquable
    table_jeu.dtag(image, "carte_joueur_1")
# Déplacement de la carte sur le talon
    table_jeu.coords(image, COORD_TALON)
 # S'il y avait déjà une image sur le talon, on la supprime
    if image_talon is not None:
        table_jeu.delete(image_talon)
# On affecte à l'image du talon la nouvelle carte
        image_talon = image
# Suppression de l'image et de la carte
    images_cartes_joueur_1.pop(i)
    carte_joueur_1.pop(i)
# Décalage vers la gauche des images (pour ne pas laisser de trou entre les cartes
    for ii in range(i, len(carte_joueur_1)):
        table_jeu.move(images_cartes_joueur_1[ii], -CHEVAUCHEMENT_CARTE, 0)
# On remet à None la selection car il n'y en a plus.
    selection_carte = None
 
 
def jouer_carte (event):
    global image, image_talon, images_cartes_joueur_1,carte_joueur_1, selection_carte, i
# items du canvas sur lequels le clic souris a été fait
    items = table_jeu.find_overlapping(event.x, event.y, event.x, event.y)
    i = len(carte_joueur_1) - 1 # index max des cartes joueurs
# Parcours des images de droite à gauche
    for image in images_cartes_joueur_1[::-1]:
# Si le clic correspond à cette image
        if image in items:
            break
        i -= 1
    else:
# Le clic n'a pas été fait sur une image des cartes joueurs
# Il n'y a rien à faire
        return
    carte = carte_joueur_1[i]
# S'il y avait une sélection et que c'est la même que la nouvelle
    if selection_carte == i:
        print("Le joueur joue la carte :", carte)
         
        #-------------------------------------conditions d'une carte posable-----------------------------------------
        if carte == '+4':   # +4 carte à l'adversaire
            talon.append (carte)
            deplacement_carte ()
            w = 200
            for i in range (4):       
                p=cartes.pop()
                n=len (carte_joueur_2)
                o= (n*CHEVAUCHEMENT_CARTE)+ w
                carte_joueur_2.append(p)
                table_jeu.create_image(o, 150, image=images_cartes[p], tags="carte_joueur_2")
                images_cartes_joueur_2.append(p)
                o += CHEVAUCHEMENT_CARTE
                sleep(1)
            affichage_choix_couleur ()
    
                          
        elif carte == '4c':    #changement de couleur
            talon.append (carte)
            deplacement_carte ()
            affichage_choix_couleur ()
 
        elif carte [1] == talon[-1][1] and carte [0] == "j" or talon[-1][0]=="j" and carte[0] == "j": # +2
            talon.append (carte)
            deplacement_carte ()
            w = 200
            for i in range (2):       
                p=cartes.pop()
                n=len (carte_joueur_2)
                o= (n*CHEVAUCHEMENT_CARTE)+ w
                carte_joueur_2.append(p)
                table_jeu.create_image(o, 150, image=images_cartes[p], tags="carte_joueur_2")
                images_cartes_joueur_2.append(p)
                o += CHEVAUCHEMENT_CARTE
                table_jeu.update()
                sleep(1)
                 
        elif carte [1] == talon[-1][1]:     # carte de la meme couleur du talon
            talon.append (carte)
            deplacement_carte()
   
        elif carte [0] == talon[-1][0]:  # carte du meme chiffre du talon
            talon.append (carte)
            deplacement_carte ()
      
# Soit il n'y avait pas de sélection, soit elle différente de la précédente
    else:
# Il y avait une sélection
        if selection_carte is not None:
            print("Le joueur choisit une autre carte :", carte)
# désélection de la précédente carte
            image_carte_precedente = images_cartes_joueur_1[selection_carte]
            table_jeu.move(image_carte_precedente, 0, DECALAGE_SELECTION_CARTE)
        else:
# 1ère sélection
            print("Le joueur selectionne la carte :", carte)
# Mise en sélection de la carte
        table_jeu.move(image, 0, -DECALAGE_SELECTION_CARTE)
        selection_carte = i
 
 
#--------------------PROGRAMME--------------------------------------------------------------
 
#INTERFACE GRAPHIQUE
 
LARGEUR_TABLE = 1500
HAUTEUR_TABLE = 700 
 
uno= tk.Tk()
# Distribution des cartes
images_cartes,joker,cartes,carte_joueur_1,carte_joueur_2,talon = initialisation() 
# Largeur et hauteur des cartes (on prend en base celles de la 1ère carte)
LARGEUR_CARTE = images_cartes[cartes[0]].width()  #comment reduire la taille des cartes ?
HAUTEUR_CARTE = images_cartes[cartes[0]].height()
# Chevauchement des cartes du joueur sur la table
CHEVAUCHEMENT_CARTE = int(LARGEUR_CARTE / 2)
# Décalage vers le haut lorsqu'une carte est cliquée
DECALAGE_SELECTION_CARTE = int(HAUTEUR_CARTE / 3)
 
# coordonnée sur la table de jeu de l'image du talon
COORD_TALON = (
    int(LARGEUR_TABLE / 2 + LARGEUR_CARTE + 50),
    300,
)
 
# coordonnée sur la table de jeu de l'image de la pioche
COORD_PIOCHE = (
    int(LARGEUR_TABLE / 2 - LARGEUR_CARTE - 50),
    int(HAUTEUR_TABLE / 2),
)
 
table_jeu = tk.Canvas(uno, width=LARGEUR_TABLE, height=HAUTEUR_TABLE, bg="green")
table_jeu.grid()
# Création sur la table du talon
z=int(LARGEUR_TABLE / 2 + LARGEUR_CARTE + 50)
image_talon = []
for carte in talon :    #comment faire pour que ca affiche que la derniere valeur du talon ?
    image_id = table_jeu.create_image(z, 300, image=images_cartes[carte], tags="carte_talon")
    image_talon.append(image_id)
 
 
# Création sur la table des images des cartes du joueur1.
x=200
images_cartes_joueur_1 = []
for carte in carte_joueur_1:
    image_id = table_jeu.create_image(x, 550, image=images_cartes[carte], tags="carte_joueur_1")
    images_cartes_joueur_1.append(image_id)
    x += CHEVAUCHEMENT_CARTE
   
 # Création sur la table des images des l'ordi.
w = 200
images_cartes_joueur_2 = []
for carte in carte_joueur_2:
    image_id = table_jeu.create_image(w, 150, image=images_cartes[carte], tags="carte_joueur_2")
    images_cartes_joueur_2.append(image_id)
    w += CHEVAUCHEMENT_CARTE
     
image_talon = None
selection_carte = None
 
table_jeu.tag_bind("carte_joueur_1", "<Button-1>", jouer_carte)
uno.mainloop()   