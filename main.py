from player import *
from ennemi import * 
from random import randint
import time

"""
try : essayer quelque chose
except : si le try ne marche pas
else : si le try fonctionne
finally : pour la fin du try
"""

def attack(j1, j2):
    if j2.parade == True:
        j1.temp_damage = j1.damage // 2
    j2.health -= j1.temp_damage

def charger(j):
    j.temp_damage *= 1.5

def combat(joueur, _ennemi):
    choix = ["attaquer", "parer", "charger"]
    while joueur.health > 0 or _ennemi.health > 0:
        joueur.parade = False
        joueur.temp_damage = joueur.damage
        player_choice = input("Vous avez le choix d'attaquer, charger votre attaque ou de bloquer la future attaque de votre adversaire\nQue faites vous ? ")
        assert player_choice in choix, "Vous ne respectez pas les règles"
        if player_choice == "attaquer":
            attack(joueur, _ennemi)
            print(f"> Vous attaquez le monstre !\nIl lui reste {_ennemi.health} points de vie")
        elif player_choice == "charger":
            charger(joueur)
            print(f"> Vous chargez votre attaque\nAu prochain tour vous ferez {joueur.temp_damage} dégâts")
        else:
            joueur.parade = True
            print(f"> Vous parez la prochaine attaque du monstre")

        _ennemi.parade = False
        _ennemi.temp_damage = _ennemi.damage
        ennemi_choice = randint(1, 3)
        time.sleep(5)
        if ennemi_choice == 1:
            attack(_ennemi, joueur)
            print(f"\nLe monstre vous a attaqué\nIl vous reste {joueur.health} points de vie\n")
        elif ennemi_choice == 2:
            charger(_ennemi)
            print("\nLe monstre charge son attaque...\n")
        else:
            _ennemi.parade = True
            print(f"\nLe monstre pare votre prochaine attaque\n")
        time.sleep(5)

    if joueur.health <= 0:
        return "Vous êtes mort, vous avez perdu..."
    else:
        return "Le monstre est mort, vous avez gagné !"


player_name = str(input("Quel est votre nom ? "))
player = Player(player_name)
monster = Ennemi()

"""for round in range(5):
    chance = randint(1, 3)
    if chance == 1:
        combat(player, monster)"""

combat(player, monster)