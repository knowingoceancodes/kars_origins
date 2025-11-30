import random
import pyrpg


cprint = pyrpg.cprint

class character:

    def __init__ (self , name , dmg , health ):
        self.name = name 
        self.dmg = dmg
        self.health = health

    def damage(self , other):
        other.health -= self.dmg
        cprint(f"\n {self.name} : take that kid !")
    


class magician(character):

    def __init__(self, name, dmg, health , mp):
        super().__init__(name, dmg, health)
        self.mp = mp
    
    def special(self , other):

        tp = {"fire" : "burn" , "ice" : "freeze" , "wind" : "blow" , "rock" : "smash"}

        if self.mp in tp:
           cprint(f"\n {self.name} : gonna use {self.mp} and {tp[self.mp]} you !!!")

        other.health -= random.randint(5 , 10)

    



class buff(character):

    def __init__(self, name, dmg, health):
        super().__init__(name, dmg, health)


    def special(self , other):
        msp = random.randint(self.dmg , self.dmg+10)
        other.health -= msp
        cprint(f"\n {self.name} : MUSCLE POWER !!!! , YEAHHHHHHHHHH BABY !!!!!!")

        


def fight(hero , anti):

    uses = 3
    ouses = 3

    while hero.health > 0 and anti.health > 0:
        

        i = input(f'''\n FIGHT[1] , SPECIAL[2] ({uses} USES LEFT)
            [{hero.name} : {hero.health} , {anti.name} : {anti.health} ]
        
            ''')
        
        

        if i == "1":
            hero.damage(anti)

        elif uses > 0 and i == "2":
            uses = uses-1
            hero.special(anti)

        elif uses <= 0 and i == "2":
            cprint("\n DEV : you are out of your special skill , child")

        else:

            cprint("\nDEV : OUT OF YOUR MIND DEAR SIR ?")


        if hero.health > 0:
            anti.damage(hero)
            
        
            chance = random.randint(1 , 100)

            if chance > 70 :
                anti.special(hero)
                ouses -= 1

            elif chance > 70 and ouses <= 0 :
                cprint(f"\n{anti.name} : ahh , my magic went away lol")
    
    if hero.health == 0:
        cprint("\n u lose , lol")

    else :

        cprint("\n nice try diddy")


arno = buff("arno" , 10 , 100 )
yor = magician("yor" , 9 , 100 , "fire")

fight(arno , yor)
