import pyrpg
cprint = pyrpg.cprint


class character:

    def __init__(self ,name , health , dmg):
        self.name = name
        self.health = health
        self.dmg = dmg

    def attack(self , other):
        other.health -= self.dmg
        print(f"{other.name} was attacked for {self.dmg} damage points by {self.name}")

    def is_alive(self):
        return self.health > 0

    
def battle(hero , opponent):
    cprint("\n ----- battle start -----")

    while hero.is_alive() or opponent.is_alive():
        b = input(f"choose your stance : attack[1] , skip[2] , block[3] " 
                 f"{opponent.name} HP: {opponent.health}  |  {hero.name} HP: {hero.health}:|~|:-"
                 )

        if b == "1":
            hero.attack(opponent)
        elif b == "2":
            cprint(f"\n {hero.name} skips turn ")
        elif b == "3":
            opponent.attack(hero)


        