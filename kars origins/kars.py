# -----imports-------#
import random
import time
import json
import threading



# ---- character / mechanics setup ------#

#human class

class character:  

    def __init__(self , name ,  health , damage , catchphrase):
        self.health = health
        self.damage = damage
        self.name = name
        self.catchphrase = catchphrase

    def is_alive(self):
       return self.health > 0

     # handles gore
    def attack(self , other):
        dmg = random.randint(self.damage , self.damage+20)
        other.health -= dmg

        attacks = [ f"{self.name} punches {other.name} as a tooth flys off.. damage took by {other.name} :- {dmg} " , f"{self.name} kicks {other.name} and he falls down with a thud ... damage took by {other.name} :- {dmg}" , f"{self.name} throws {other.name} and mashes his head for {dmg} damage points"]

        cprint(random.choice(attacks))
      
        
        if dmg > 20:
             cprint(f"{self.name} dealt a critical attack with {dmg} damage points to {other.name}")

    def taunt(self):
            cprint( f"{self.catchphrase}" )

    def block(self , other , incoming_dmg ):
         block_dmg  = random.randint(5 , 13)
         final_dmg =  max(incoming_dmg  - block_dmg , 0 )
         self.health -= final_dmg
         cprint(f"{self.name} blocked {other.name}'s attack and recived {final_dmg} damage  !")
         return True

    def parry(self , other ):
         chance = random.randint(1,100)
         if chance <= 60:
              dmg = random.randint(self.damage + 15  , self.damage + 20)
              other.health -= dmg           
              cprint(f"{self.name} goes through {other.name}'s attack and rips {other.name}'s ribs apart ... damage took by {other.name} :- {dmg}!")

              return True
         else:
              cprint(f"{other.name} dodges {self.name}'s attack and breaks {self.name}'s fingers and pokes it in the eye sockets , blood gets all over {other.name}'s face")
              return False
              

    def instinct(self , other ):
          chance = random.randint(1,100)
          if chance <= 80:
              dmg = random.randint(self.damage + 15  , self.damage + 20)
              other.health -= dmg           
              cprint(f"{self.name} cracks {other.name}'s bones as {other.name}'s marrow splatters everywhere... damage took by {other.name} :- {dmg}")

              return True
          else:
               cprint(f"{other.name} grabs {self.name}'s arms and mashes {self.name}'s ribs... , blood splatters everywhere , all instincts wasted")
               return False
              
          
         
         
     
    def critical(self , other):
          hit = random.randint(self.damage+ 5 , self.damage + 20)
          other.health -= hit

          cprint(f"{self.name} rips apart {other.name}'s jaw and smashes it into the skull till the facial structure deforms... damage took by {other.name} :- {hit}")
         
     
    def fatality(self , other):
         other.health = 0
         print(f"{self.name} ripps off {other.name}'s thigh muscle and breaks the femur as the bone flys off ,  {self.name} picks the bone and pierces it into the skull of {other.name}")

#item class
         
class armor:
     
     def __init__(self , protection , user , durability , name):
         self.protection = protection
         self.user = user 
         self.durability = durability
         self.name = name
         
     def protect(self , user):
          user_health = user.health
          total_health = user_health + self.protection
          user.health = total_health
          if self.durability <= 0:
               self.protection = 0
               cprint(f"{user.name}'s {self.name} got broken ! total health remaining :- {user.health - self.protection} ")
          
     def is_broken(self):
          if self.durability <= 0:
               return True


     
class healing:

     def __init__(self , player , power):
          self.power = power
          self.player = player
          self.power = power
     
     def heal(self , player):
          player.health = player.health + self.power
          print(f"{player.name} healed for {self.power} health points , player health :- {player.health}")


#enemy class
class animal:
     def __init__(self , name , attack_dmg , health , catchphrase):
          self.name = name
          self.attack_dmg = attack_dmg
          self.health = health
          self.catchphrase = catchphrase

     def rip(self , other ):
          dmg = random.randint(self.attack_dmg , self.attack_dmg + 10)
          other.health -= dmg
          print(f"{self.name} slashes his paws and rips {other.name}")

     def fire_breath(self, other):
          dmg = random.randint(self.attack_dmg + 10 , self.attack_dmg + 20)
          other.health -= dmg
          print(f"{self.name} breathes fire as {other.name} skin starts to peel off , exposing the red flesh beneath... damage took by {other.name} :- {dmg}")  

     def fatality(self , other):   
          other.health = 0
          print(f"{self.name} bites {other.name}'s head off and throws it against a rock , as the skull shatters into pieces , the beast munches on the innards...")

     def taunt(self):
          cprint( f"{self.catchphrase}" )

#battle(human vs human model)

def battle(hero , enemy , amr , amr2):
 bheal = healing(hero , 50)
 strongheal = healing(hero , 80)
 ultraheal = healing(hero , 200)

 hchance = random.randint(1,100)
 
 if hchance <= 10:
     rheal = ultraheal
 elif hchance <= 20:
      rheal = strongheal
 elif hchance <= 90:
      rheal = bheal
 else:
      rheal = False


 heal = 0
 amr.protect(hero)
 amr2.protect(enemy)
 cprint("----- start fight ------")
  
 while hero.is_alive() and enemy.is_alive():  
    r = False       
    i = input(
            f"\n[1] Fight  |  [2] Block  |  [3] Parry  |  [4] Instinct\n"
            f"{enemy.name} HP: {enemy.health}  |  {hero.name} HP: {hero.health}\n:~: "
        )
   
    if i == "1":
         hero.attack(enemy) #normal attack
         amr2.durability -= 5
    elif i == "2":
         incoming = random.randint(enemy.damage , enemy.damage+20)
         r = hero.block(enemy , incoming)
    else:
         r = hero.parry(enemy)
         if r:
              amr2.durability -= 10

         if not r:
              enemy.attack(hero)
              amr.durability -= 5

    if hero.is_alive() and enemy.is_alive():
           if not r:
                echance = random.randint(1,100)

                if echance <= 30:
                    cprint("critical")
                    enemy.critical(hero)
                    amr.durability -= 10
                else:
                    enemy.attack(hero)
                    amr.durability -= 5
          
           elif r:
                
                echance = random.randint(1,100)

                if echance <= 30:
                    cprint(f"{enemy.name} skips a critical turn")
                else:
                    cprint(f"{enemy.name} skips turn")

                
         
    used = False
          
    if hero.health <= 40 and i == "4":
         hero.instinct(enemy)

         if echance <= 30:
              print(f"{enemy.name} is going to do a critical damage !")
         else:
              print(f"{enemy.name} is going to do a normal damage")
          
    used = True

    if enemy.health <= 30:
         f = input("\n enter 'f' to conduct FATALITY")

         if f == "f":
              hero.fatality(enemy)
         if f != "f":
              cprint("   qte MISSED !  ")
              enemy.fatality(hero)

 cprint("\n BATTLE ENDS HERE")

 if hero.is_alive():
     hero.taunt()
 else:
     enemy.taunt()

 if rheal and hero.is_alive() :
     heal = 1
     cprint(f"{hero.name} obtained {heal} healing , the strength of potion is {rheal.power} health points ! ")
     rheal.heal(hero)

 if not rheal:
      cprint(f"{enemy.name} had no drops")

    



#long pause
def lp():
     time.sleep(5)

#short pause
def sp():
     time.sleep(2)

     


# cinematic-print 
def cprint(text , duration=0.06):
     for t in text:
          print(t , end="" , flush=True)
          time.sleep(duration)
     print()
     
def ts(x):
     time.sleep(x)
          
def save(player_health , game_state_dialog):
     json.dump( { "player_health" : player_health , "game_state_dialog" : game_state_dialog} , open("savefile.json" , "w") )

def load():
     data = json.load( open("savefile.json" , "r") )
     return data["player_health"] , data["game_state_dialog"]

#-------game world --------#
hero = character("KARS" , 100 , 12 , "kars : I am worse than death" )
guard = character("GUARD" , 100 , 10 , "guard : Your blood will wash away your father's sins!")
guard2 = character("GUARD" , 100 , 8 , "guard : who mashes who's skull now ! ")

arm2 = armor(20 , guard , 50 ,  "bronze haze armour")
arm3 = armor(20 , guard2 , 50 ,  "bronze haze armour")



arm1 = armor(10 , hero , 50 , "golden dusk armour")

#----- story board chapter 1 ------#
try:
     load()
except:
     pass

cprint("a game developed by divyanshu...")
ts(2)

cprint("game intended for mature audiences , includes :- self harm , injury detail , violence , mild language ")
ts(2)

print("\n")

cprint("??? : KARS !")
ts(1.5)
cprint("??? : look what they have done !")
ts(2)
cprint("??? : you are my hope KARS !")
ts(2)
cprint("\n you see a world painted red with bloods of millions ,  with a figure standing on the bodies of the dead")
ts(2)
cprint("\n you watch him as he gets stabbed from behind")

cprint("\n ??? : KILL THEM ALL KARS !")
ts(2)

cprint("\n --kars : chapter-1 : the origins--")

ts(2)

cprint("\n you wake up in taverna , men gamble over nucklebones , and women sing as the wine spills everywhere...")
ts(2)
cprint("\n kars : *grunts* ")
ts(1.5)
cprint("\n a guard enters the place , with golden boots and bronze armour , he stomps his boots as he starts to speak...")
ts(2)
cprint("\n guard : By decree of Olympus, all gatherings must remain silent.")
ts(2)
cprint("guard : Anyone found questioning the gods will BURN ")
ts(1)

s1d1 = input("\n ask about the decree [1] , speak up [2]")

save(hero.health , s1d1)

if s1d1 == "1" :
     cprint("\n guard : Look who crawled in. The whelp of the traitor. Thought you could drink among men?")
     ts(2)
     cprint("guard : Your father dug too deep, peered where no mortal should. Now his soul rots where it belongs — beneath Olympus's boot-")
     ts(2)
elif s1d1 == "2":
     cprint("\n guard : You don't deserve to speak up ")
     ts(1)
     cprint("guard : Your father was a traitor to our land , our gods ! , you shall burn in the underworld as he did")
     ts(2)
     cprint("guard : You were spared , just because of your innocence but , you share the same blo-")
     ts(2)
else:
     cprint("--choosing canon choice--")
     ts(1)
     cprint("\n guard : You don't deserve to speak up ")
     ts(1)
     cprint("guard : Your father was a traitor to our land , our gods ! , you shall burn in the underworld as he did")
     ts(2)
     cprint("guard : You were spared , just because of your innocence but , you share the same blo-")
     ts(2)



cprint("\n rage filled your soul as you held the guard up his throat.")
ts(1)
cprint("\n kars : you dont deserve to speak up against MY FATHER !")
ts(2)
cprint("guard : you have done a grave mistake you drunk bastard !")
ts(2)

cprint("\nThe taverna goes silent. The smell of wine and sweat is replaced by iron and blood...")
ts(2)
s1d2 = cprint("The guard draws his blade. The crowd watches, waiting for one to fall.")
s1d2
ts(2)
save(hero.health , s1d2)


battle(hero , guard , arm1 , arm2)

if hero.is_alive():
     cprint(f"{hero.name} emerged victorious!")
else:
     cprint("---restarting from checkpoint---")
     hero.health = 100
     guard.health = 100
     
     ts(2)

 
     battle(hero , guard , arm1 , arm2)

cprint("another guard approaches ")

cprint("kars : *shouts with rage* ")
cprint("kars : i will mash your skull till you beg your own death !")

cprint("\n")

battle(hero , guard2 , arm1 , arm3)

if hero.is_alive():
     cprint(f"{hero.name} emerged victorious!")
else:
     cprint("---restarting from checkpoint---")
     hero.health = 100
     guard.health = 100
     
     ts(2)

 
     battle(hero , guard , arm1 , arm2)


#director's cut
cprint("'\n the whole taverna goes silent as you mashed the brains out of the guard.. ")
ts(2)
cprint(" MERCY ! MERCY ! - they shout , but the monster within you knew your destiny. ")
cprint("the guards lied lifeless , the floor drank the blood of your enemies.. ")

cprint("\n you walked outside , your hands soaked with blood , heart filled with hatred and a mind enraged.. ")
cprint(" you lie against the wall , feeling the cool stone against your back as you catch your breath.")

cprint("\n you look at the sky , the stars shine bright , you feel a presence , a power within you.. ")
cprint("the guards were alerted of your actions , they will come for you...")

cprint("live or die , the choice is yours...")

cprint("\n --chapter 1 : world of the dead-- ")
ts(2)

cprint("\n guard : He is there , leaning against the walls ")
cprint("\n guard : Get him !")
ts(2)

cprint("\n  you get hit hard by a guard's shield , everything goes black...")

ts(5)

cprint("\n ??? : K-KA-KARS ! ")
ts(1)
cprint(" ??? : WAKE UP ! ")
ts(2)
cprint("your eyes snap open... ")
sp()
cprint("The sky , it was not blue , the clouds were not gay , the sun was no more , hidden behind the bloodsoaked sky")
sp()
cprint("this was not the world YOU knew...")
sp()
cprint("the ground , it was red , soaked with the blood of the fallen. ")
sp()

ch2 = input(" explore[1] , shout[2] , pretend its a dream[3] ")

#choice 2:
key = False
key2 = False
#canon choice
if ch2 == "1":
     cprint("\n you stand up , your legs shaking beneath you.")
     lp()
     cprint("the world was a living nightmare")
     sp()
     cprint("the land was covered with bodies...")
     sp()
     cprint("you walk forward , your feet sinking in the blood soaked ground")
     sp()
     key = False

#branched choice
elif ch2 == "2":
     cprint("\n KARS : H- HELP ME!")
     sp()
     cprint("KARS : SOMEONE HELP ME !")
     sp()
     cprint("KARS : PLEASE !")
     sp()

     cprint(".  .  . silence .  .  .")
     lp()
     cprint("no one answers your cries for help")
     sp()

     cprint(" ??? : kars... why do you cry ?")
     time.sleep(3)
     cprint("??? : you have you destiny here , YOU ARE THE CHOSEN ONE !")
     sp()
     cprint("??? : embrace your destiny KARS , and rise above the rest !")
     sp()
     cprint("??? : you are the hope of our people , the one who will bring us salvation !")
     sp()
     cprint("??? : rise above the rest KARS , embrace your roots !")
     sp()

     cprint("...")
     key = True


     #skips a fight with a slender monster

#diverts to canon choice

elif ch2 == "3":
     cprint("\n you close your eyes , trying to convince yourself that this is a dream")
     cprint("but the stench of death and decay was too real")
     cprint("you open your eyes , only to see the same horrifying sight")
     cprint("you stand up , your legs shaking beneath you.")
     cprint("the world was a living nightmare")
     cprint("the land was covered with bodies...")
     cprint("you walk forward , your feet sinking in the blood soaked ground")

     key = False

else:
     cprint("\n --choosing canon choice--")
     cprint("\n you stand up , your legs shaking beneath you.")
     cprint("the world was a living nightmare")   
     cprint("the land was covered with bodies...")
     cprint("you walk forward , your feet sinking in the blood soaked ground")

     key = False


beast_faught = False
     

if not key: # if player chose canon choice
     cprint("\n the cobblestone road , it was , it couldn't be... ")
     cprint("it , it was the taverna ! , but how ? ")
     cprint("the taverna was destroyed , the bodies of the dead lied everywhere , the smell of blood and the oozing innards filled the space")

     cprint("you walk inside , the place was deserted , the tables were overturned , the walls were splattered with blood")
     cprint("\n *stomp* *stomp* *stomp* ")
     cprint("you hear the sound of boots , the heavy ones , they were coming from BEHIND you !")
     
     cprint("you turn around , and see a figure in the distance , its hard to make out any details")
     cprint("the figure was tall" )
     cprint("it was slender and had long arms")

     cprint("it wasn't a beast , it was not human , it was a creature , A MONSTER !")

     #quick time events

     limit = 3
     cprint("THE SLENDER CREATURE APPROACHES , HIS BODY RIPS TO EXPOSE HIS HOLLOW CHEST WANTING TO ABSORB YOU")

     start = time.time()
     key = input("press A :- ").lower()
     end = time.time()

     elapsed = end - start

     if key == "a" and elapsed <= 3:
          cprint("you throw your legs down the groud pushing your body forward... the beast was unable to catch you")
     else:
          cprint("your bones get squished as the creature absorbs you , the creature feasts on you ")
          cprint("...restating from checkpoint...")

     
     print(" THE BEAST GROWLS AS HE APPROACHES YOU !")


     # the snippet is under development


   


     if hero.is_alive():
          beast_faught = True #technically impossible to live in the fight
          cprint("??? : that power ... it can't be... ")
          cprint("??? : you are the chosen one , the one who will bring us salvation !")
          cprint("??? : rise above the rest KARS , embrace your destiny !")

          cprint("??? : embrace your roots kars , you are my son , the son of alexios")
          cprint("??? : rise above the rest")

          cprint("alexios : the hive mind had taken over you")
          cprint("alexios : we were betrayed by the gods , they took everything from us")
          cprint("alexios : now we will massacre everyone on the mortal plane")

     

          cprint("alexios : together we will bring down the gods , and rule the world as we see fit")

          cprint("a game developed by divyanshu...")
          cprint("ending :- impossible ending")

          cprint("divyanshu : ayo man ! you made it to the impossible ending ! that was technically impossible to do :_) , good luck tampering codes")

     else:
          key = True
          beast_faught = True


     # the game hypothetically ends here if you some how defeat the beast lol         

if key:
     lp()
     cprint(".  .  .  .  .  .  .  .  .  .  .")

     lp()

     cprint("--the light stabs through your eyes as you wake up--")
     sp()
     cprint("*voice* : wake up you shit")
     sp()

     cprint("*voice* : *fade noise")
     sp()

     cprint("--your eyes snap open , you jump off the floor and crawl under the bed inside your cell-- ")
     lp()

     cprint("guard : acting all cocky , huh ? ")
     sp()
     cprint("guard : we should have slit your throat open... you were lucky .. the gods spared you")
     sp()

     cprint("guard : you will rot in this cell till you die... and your 'acting dead' wont save you")
     sp()

     cprint("kars : i wasn't acting dead... , i was... no .. i was somewhere else !")
     sp()

     cprint("guard : kill yourself if you are done with your blabber , you bastard")
     sp()


     
     #arguments for situation
     partanswered1 = False
     partanswered2 = False
     partanswered3 = False

    #integrating chapter 2 transition key
     ch1_climax = False

     #fix bug
     while not ch1_climax:
        try: 
              u = int(input("\n  ask who brought you here[1] , ask what happens to you [2] , look around the cell [3]"))
        
        except ValueError:
             cprint("\n kars : i should ask the guard properly , it seems like he is hiding something from me")
             continue
        
        if u == 1:
             
             if not partanswered1:
                   cprint("\nguard: *sips a mug full of wine...*")
                   sp()
                   cprint("\nguard: You were knocked out, Sthenelos picked you up and threw you into the cart")
                   sp()
                   cprint("\n--the guard looks at you disgusted--")
                   sp()
                   partanswered1 = True

             else:
                  cprint("\nkars : i had to ask the guard about what lies next")
                  sp()

        if u == 2:
             
             if not partanswered2:
                  ch1_climax = True

             else:                             
                  None
                  
        if u == 3:
             
             if not partanswered3:
                  cprint("You look around")
                  sp()
                  cprint("The place is arid with just a single window, beyond reach")
                  sp()
                  cprint("The only bed is made up of hay but comfortable")
                  sp()
                  partanswered3 = True

             else: 
                  cprint("kars : i couldn't waste anymore time , i had to talk to the guard about what's next")
                  sp()

        if u == 0 or u < 3 or u > 0:
             cprint("kars : *bashes his head for he was out of his mind* ")
             sp()



# kar's awakening arc [ch1-2] transition...
if ch1_climax:
    cprint("\n guard : the word is..")
    sp()
    cprint("guard : *holds the mug up high *")
    sp()
    cprint("guard : you are going to be tried tomorrow at the kings court ")
    sp()
    cprint("guard : *laughs as he gulps a mouthfull of wine* ")
    sp()
    cprint("guard : with your acts , you are going to drop DEAD...")
    lp()

    cprint("\nfear held you the most")
    sp()

    if beast_faught == True:
      cprint("\nyou couldn't die twice")
      sp()
      cprint("\nyou check your chest for the mark by the magestic beast")
      sp()
      cprint("\nthere it lies , the mark of the beast , blood oozes from the wound")
      sp()
      cprint("\nit wasn't bleeding , it was BURNING")
      sp()

    cprint("\n??? : why do you fear death KARS ?")
    sp()
    cprint("??? : you were never alive to begin with")
    sp()
    cprint("??? : EMBRACE DEATH")
    lp()

    cprint("\n the sky darkens as the moon rises high")
    sp()
    cprint(" the world around you starts to fade away")
    sp()

    cprint("\nguard : whats your last wish ?")
    sp()
    cprint("guard : *gulps the last of his wine*")
    sp()
    cprint("guard : *chuckles* you are going to die tomorrow , so why bother ?")
    sp()
    cprint("\n xander : name's xander... thought you should know")
    sp()


    cprint("\n you close your eyes as the world fades away...")
    lp()

    cprint("\n the guards rush in to your cell , they drag you out of the cell ...")
    sp()
    cprint("\n the hopeful sun's rays darken as they shine upon you")
    sp()
    cprint("\n the guards beat you till you were lifeless , breathless , motionless and emotionless..")
    sp()
    cprint("\nfighting back would make things even worse..")

    
    cprint("\n armed guard : put the fuck down , shove him up the cart")  
    sp()  
    cprint("\nyour bones crack as your lifeless body get shoved into the cart")
    sp()
    cprint("\narmed guard : he should die for what he has caused to our brother")
    sp()
    cprint("\nguards spit at you for your actions , they have lost someone dearest to them... you were heartless to understand them enough...")
    sp()
    cprint("\narmed guard 2 : he is the traitor's son , the corrupt blood runs through his veins")
    sp()

    cprint("\nyour blood burns as your vision blurs ")
    sp()
    cprint("your pupils stare at the blue sky , though lifeless ")
    lp()
    
    cprint("\nthe light tears through your eyes as you open them")
    sp()

    cprint("\n kars : *scream in agony* ")
    sp()


    cprint("\n you stood tied to the ground")
    sp()

    cprint("\n chains rattle as you try to break free...")
    sp()
    cprint("\n the chains were soaked in blood")
    sp()

    cprint("\nkars : WHAT IS THIS PLACE ! ")
    sp()

    cprint("\nyou scream as you look above , where stood the king's throne")
    sp()

    cprint("\nking asterion : KARS ! what a pleasure... ")
    sp()

    cprint("king asterion : i see you have awakened from your slumber , your fists crave blood , dont they ?")
    sp()

    cprint("\n ??? : 'your fists crave blood' ")
    lp()

    cprint("\n you look around the colosseum , people surround the place with the king watching.")
    sp()
    cprint("the atmosphere is tense , the crowd murmurs in anticipation.")
    lp()

    cprint("\nking asterion : your fist will feast on blood or the soil gets watered by your blood")
    sp()
    cprint("\nking asterion : this is your fate")
    sp()

    cprint("\n the crowd roars in excitement as the battle is about to begin")
    lp()

    cprint("\n 'traitor' , 'traitor' , 'traitor' , 'traitor' , 'traitor' , 'traitor' , 'traitor' ---chants the crowd--- ")
    sp()

    cprint("\n king asterion : LET THE GAMES BEGIN ! ")
    sp()

    cprint("\n the gates open , the bars lift up , the smell of blood and sweat fills the air...")
    sp()
    cprint("you could see 2 figures rushing towards you")
    sp()

    cprint("\n 2 lions leap towards you as the crowd goes wild...")
    sp()

    cprint("\n the beasts were upon you , their claws raked your flesh , their teeth sank into your skin... ")
    sp()

    cprint("\n BUT THEY WERE NOT YET READY FOR THE BEAST WITHIN YOU...")
    lp()





cprint("\n --end of chapter 1---")
sp()

cprint(''' \n


          |-----------------------------||-------------------------------------|
          |                         kars: origins                              |
          |                                                                    |
          |                   programmer:- knowingocean831 
                              |       
          |                   storyboard:- knowingocean831 
                              |
          |                                                                    |
          |                   gametester:- G-DIVYESH                           |
          |                   gametester:- Trilokesh                           |
          |                   story writing :- swayam prakash barik            |
          |                   story writing :- G-DIVYESH                       |
          |____________________________________________________________________|                                                              
          

          
          








''')
sp()

cprint("\nchapter 2 : the land of the dead")
lp()
cprint("TO BE CONTINUED")
lp()

if beast_faught:
     cprint("\n-YOUR BLOOD BURNS THE SHAKLES INTO ASHES-")
     sp()
     cprint("\nKARS : Incinerate !")
     lp()


cprint("-end-")
ts(5)



# ---credits---- #

#playtester :- divyeshgundala08@gmail.com
#developer :- divyanshu
#storyboard :- divyanshu
#project management :- divyanshu
#creative direction :- divyanshu   

