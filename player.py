class Player:
    def __init__(self, player_name):
        self.name = player_name
        self.health = 20
        self.damage = 10
        self.temp_damage = 0
        self.parade = False

    def stat(self):
        message = f"Nom : {self.name} \nPoint de vie : {self.health}\nPoint d'attaque : {self.damage}"
        return message