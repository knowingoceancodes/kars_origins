import time 
import random

#this module is made by divyanshu panda and this has most of the things that one could need for a text based game

#available functions :
# 1. qte_call(context_text , iftext , elsetext , timer=3)
# 2. explorational_question(option1 , option2 , option3 , response1 , response2 , response3 , error_statement , else_statement)

__author__ = "Divyanshu Panda"
__version__ = "0.1.0"
__description__ = "A lightweight text-based game engine for Python developers."


#quick time event request 
def qte_call(context_text , iftext , elsetext , timer=3):

    def cprint(x):
        for i in x:
            print(i , end="" , flush=True)
            time.sleep(0.06)

    print("\n")

    
    dataset = ["w" , "a" , "s", "d"]

    randomchoice = random.choice(dataset)


    while True :

        cprint(context_text)

        print("\n")

     
        start = time.perf_counter()
        q = input(f"enter {randomchoice} :- ")
        print("\n")
        end = time.perf_counter()

        elapsed = end-start

        if q == randomchoice and elapsed <= timer:
             cprint("----| perfect |----")
             print("\n")
             cprint(iftext)
             break
        
        else:
              cprint("----| failed |----")
              print("\n")
              cprint(elsetext)
              print("\n")
             

#explorational interaction
def explorational_question(option1 , option2 , option3 , response1 , response2 , response3 , error_statement , else_statement):

    def cprint(x):
        for i in x:
            print(i , end="" , flush=True)
            time.sleep(0.06)
    
    def sp():
     time.sleep(2)


    partanswered1 = False
    partanswered2 = False
    partanswered3 = False

    all_answered = False

    while not all_answered :
        try: 
              u = int(input(f"\n  {option1}[1] , {option2}[2] , {option3}[3]"))
        
        except ValueError:
             cprint(f"\n kars : {error_statement}")
             continue
        
        if u == 1:
             
             if not partanswered1:
                   cprint(f"{response1}")
                   sp()
                   partanswered1 = True

             else:
                  cprint(f"\n kars : {else_statement}")
                  sp()

        if u == 2:

            if not partanswered2:
                   cprint(f"{response2}")
                   sp()
                   partanswered2 = True

            else:
                  
                  cprint(f"\nkars :{else_statement}")
                  sp()
             
             
                  
        if u == 3:
             
             if not partanswered3:
                  cprint(f"{response3}")
                  sp()
                  partanswered3 = True

             else: 
                  cprint(f"kars : {else_statement}")
                  sp()

        if sum([partanswered1,partanswered2,partanswered3]) == 3:
             all_answered = True
             break
        
        else:
             cprint("kars : *bashes his head for he was out of his mind* ")
             sp()

# cheeky print or cprint
def cprint(Text , duration=0.06):
     for ch in Text:
          print(ch , end="" , flush=True)
          time.sleep(duration)

def sp(Time=2):
     time.sleep(Time)
    
def lp(Time-5)
    time.sleep(Time)

if __name__ == "__main__":

    print(f"this module is made by {__author__} , version:- {__version__}")
