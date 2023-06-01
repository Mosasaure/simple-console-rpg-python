class Player:
    def __init__(self, player_name = "User") -> None:
        self.name = player_name    # nom du joueur (str)
        self.health = 20    # point de vie du joueur (int)
        self.damage = 10    # point d'attaque du joueur (int)
        self.temp_damage = self.damage    # point d'attaque temporaire du joueur (int)
        self.parade = False    # défini si oui ou non le joueur parade la prochaine attaqsue de son adversaire (bool)
        self.inventory = [
            {
                "life_potion": 0, 
                "strenght_potion": 0, 
                "mystery_potion": 0
            }, 
            {
                "monney": 0
            }
        ]    # inventaire du joueur (list)

    def stat(self) -> str:
        """renvoie les statistique du joueur (nom, PV, PA, nombre de potion)"""
        message = f"Nom : {self.name} \nPoint de vie : {self.health}\nPoint d'attaque : {self.damage}\nDans votre sac à dos vous avez {self.inventory['potion']} potion(s)"
        return message
    
class Ennemi:
    def __init__(self, name = "Ennemi") -> None:
        self.name = name
        self.health = 15    # point de vie de l'ennemi (int)
        self.damage = 5    # point d'attaque de l'ennemi (int)
        self.temp_damage = self.damage    # point d'attaque temporaire de l'ennemi (int)
        self.parade = False    # défini si oui ou non le joueur parade la prochaine attaqsue de son adversaire (bool)