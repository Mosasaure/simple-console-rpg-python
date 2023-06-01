import classe
from random import randint
import time

"""
try : essayer quelque chose
except : si le try ne marche pas
else : si le try fonctionne
finally : pour la fin du try
"""

def start() -> None:
    player_name = str(input("Quel est votre nom ? "))

    while True:
        try:
            _round = int(input("Combien de tour voulez vous jouer ? "))
            assert _round >= 1
            print()
            break
        except ValueError:
            print("Vous devez entrer un nombre !")
        except AssertionError:
            print("Vous devez jouer un minimum de 1 tour de jeu (donc mets au moins 1 espèce de nul ._.)")

    player = classe.Player(player_name)
    monster = classe.Ennemi("Ogre")

    print(f"{player_name} voyage dans les terres désolée à la recherche d'un village pour s'y reposer.\nPour cela il/elle décide de traverser la Forêt Impénétrable réputée pour ses nombreux montres et voleurs.\n{player_name} arrivera-t-il à ses fins ?...")
    input("Appuyez sur Entrer pour continuer")
    print()

    for tour in range(_round + 1):
        if player.health <= 0:
            print("Vous n'evez plus de point de vie\nLa partie est terminée")
            input("Appuyez sur Entrer pour continuer")
            break
        chance = randint(1, 3)
        if chance == 1:
            combat(player, monster)
        elif chance == 2:
            goodEvent(player)
        else:
            badEvent(player)

def attack(joueur, adversaire) -> None:
    """fonction qui gère une attaque, du player au monstre ou inversement"""
    if adversaire.parade == True:
        joueur.temp_damage //= 2
    adversaire.health -= joueur.temp_damage

def charger(joueur) -> None:
    """fonction qui gère quand une personne charge son attaque"""
    joueur.temp_damage *= 2

def combat(player, ennemi) -> None:
    """fonction qui gere le systeme de combat"""
    print(f"Un combat a été lancé par {ennemi.name} !")

    choix = ["attaquer", "parer", "charger", "1", "2", "3"]

    while not player.health <= 0 and not ennemi.health <= 0:

        # le joueur joue

        player.parade = False

        while True:
            try:
                player_choice = input("Vous avez le choix d'attaquer (1), charger votre attaque (2) ou de bloquer la future attaque de votre adversaire (3)\nQue faites vous ? ")
                assert player_choice in choix, "Vous ne respectez pas les règles"
                break
            except AssertionError:
                print("> Vous devez choisir ce qui vous avez été proposé !")
                time.sleep(3)            

        if player_choice == "attaquer" or player_choice == "1":
            attack(player, ennemi)
            print(f"> Vous attaquez le monstre et lui faite {player.temp_damage} dégâts !\nIl lui reste {ennemi.health} points de vie")
            player.temp_damage = player.damage
        elif player_choice == "charger" or player_choice == "2":
            charger(player)
            print(f"> Vous chargez votre attaque\nAu prochain tour vous ferez {player.temp_damage} dégâts")
        else:
            player.parade = True
            print(f"> Vous parez la prochaine attaque du monstre")

        if ennemi.health <= 0:
            break

        # le monstre joue 

        ennemi.parade = False
        ennemi_choice = randint(1, 3)
        time.sleep(5)
        if ennemi_choice == 1:
            attack(ennemi, player)
            print(f"\nLe monstre vous a attaqué et a fait {ennemi.temp_damage} dégât(s)\nIl vous reste {player.health} points de vie\n")
            ennemi.temp_damage = ennemi.damage
        elif ennemi_choice == 2:
            charger(ennemi)
            print("\nLe monstre charge son attaque...\n")
        else:
            ennemi.parade = True
            print(f"\nLe monstre pare votre prochaine attaque\n")
        time.sleep(5)

        if player.health <= 0:
            break

    if player.health <= 0:
        print("Vous êtes mort, vous avez perdu...")
        input("Appuyez sur Entrer pour continuer")
        print()
    elif ennemi.health <= 0:
        print("Le monstre est mort, vous avez gagné !")
        input("Appuyez sur Entrer pour continuer")
        print()

def goodEvent(player) -> None:
    chance = randint(1, 2)
    if chance == 1:
        print("Vous trouvez une potion sur le sol, vous ne connaissez pas ses effets mais décidez quand même de la prendre")
        input("Appuyez sur Entrer pour continuer")
        print()
        player.inventory[0]["mystery_potion"] += 1

def badEvent(player) -> None:
    chance = randint(1, 2)
    if chance == 1:
        player.health -= 5
        print(f"Vous marchez dans la forêt quand soudain un sanglier vous fonce dessus\nVous perdez 5 points de vie\nIl vous en reste {player.health}")
        input("Appuyez sur Entrer pour continuer")
        print()
    elif chance == 2 and player.inventory[1]["monney"] >= 10:
        player.inventory[1]["monney"] -= 10
        print("Vous vous asseyez sur un rocher pour vous reposer\nVous êtes tranquillement en train de dormir mais vous êtes réveillez par un bruit\nOh non !\nC'était un brigant ! il vient de fuir avec 10 de vos pièces d'or...")
        input("Appuyez sur Entrer pour continuer")
        print()

start()