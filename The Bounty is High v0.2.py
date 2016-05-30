from sys import exit
import random
import time

character_name  = raw_input("What is your character name?")
character_race = raw_input("What is your character\'s race?              Human (a), Elf (b), Dwarf (c)")
character_race_elf_plural = "Elves"
character_name = character_name.title()

def character_creation():
    global character_name, character_race, character_race_elf_plural
    
    if character_race == 'a':
        character_race = "Human"
        print "Your character",character_name,"belongs to the race of",character_race,"s"
    elif character_race == 'b':
        character_race ="Elf"
        print "Your character",character_name,"belongs to the race of",character_race_elf_plural
    elif character_race == 'c':
        character_race = "Dwarf"
        print "Your character",character_name,"belongs to the race of",character_race,"s"
    else:
        print "This is not valid"
        while character_race != 'a' or 'b' or 'c':
            break
character_creation()
inventory = {
    'gold' : 500,
    'backpack': ['sleep roll', 'food','tent','map', 'water'] ,
    'weapons' : ['sword'],
    }
    
print "Your inventory contains:",inventory

time.sleep(5) 

min = 1
max = 6

def dice():
    global min,max, dice_roll,dice_number
    dice_roll = raw_input("Roll the dice?, (y)")
    if dice_roll == "yes" or "y":
        print "Rolling the dices..."
        time.sleep(2)
        dice_number = random.randint(min,max)
        print "It\'s a ", dice_number

print character_name,",begins in a small village,named Harkenwold.Everything flows naturally...You see people walking around, hear loud voices of people selling their products"
what_now = raw_input("What do you do? You enter a tavern (a),   Look around for a job (b)")
if what_now == "a":
    print "You enter a tavern called The Hungry Hunter,you walk towards the tavern owner."  
    time.sleep(2) 
    print "Ay!What can i get you?"
    print "You realize there is a poster just right behind him and you ask about it." 
    print "You need to throw a diplomacy roll in order to convince him to tell you what this is about."
    dice()
    if dice_number >= 3:
        print "He decides to tell you." 
        print "Ok this man is a murderer in our city,and of what i know, he is hiding in the woods southwest of here."
    elif dice_number < 3 :
        print "He decides not to tell you."    
        print "Luckily when you walk outside the tavern, you see the same poster and you ask citizens about it.They tell you that this man is a murderer in their city,and of what they know, he is hiding in the woods southwest of here."
    
elif what_now == "b":
    print "You see a poster of a murderer, he is hiding southwest from there.You decide to search for him."
hp = 8
    
what_now2 = raw_input("What do you want to do now?          Visit an armory and buy new equipment,then head for the forest. (a), Sleep and relax, then head for the forest. (b)")
if what_now2 == 'a':
    buy_equipment = raw_input("You enter an armory.The shop owner asks you what you want to buy.       New sword (-80 gold) (a), new shield (-50 gold) (b), new bow (-80 gold) (c)")
    if buy_equipment == 'a':
        print "You got a new longsword!"
        inventory['gold'] = 500 - 80
        inventory['weapons'].remove('sword')
        inventory['weapons'] = ['Longsword']
        time.sleep(3)
        print "Now you head for the woods..."
    elif buy_equipment == 'b':
        print "You got a new Stronger shield!"
        inventory['gold'] = 500 - 50
        inventory['weapons'] = ['Strong Shield','sword']
        time.sleep(3)
        print "Now you head for the woods..."
    elif buy_equipment == 'c':
        print "You got a new Elven Bow!"
        inventory['gold'] = 500 - 80
        inventory['weapons'] = ['Elven bow']
        time.sleep(3)
        print "Now you head for the woods..."
elif what_now2 == 'b':
    print "You rest, and head out for the woods.You also restore 2 hp."
    hp = 8 + 2
    print "HP = ",hp
if what_now2 == 'a':
    player_damage = 4 
elif what_now2 == 'b':
    player_damage = 2        

print "You walk in the forest for days and days,and in the 6th day after consuming all your food, you hear a strange sound and walk up to the location of it"
inventory['backpack'].remove('food')
time.sleep(3)
print "All of a sudden, he jumps in front of you, a wild man who hasn't been taken care of for days and says to you..."
print "How could you be so stupid, to think you can defeat me, Larse Altheron!"
time.sleep(2)  
print "You decide to attack him with",hp, "hp"
print "You pull out your weapon, which deals", player_damage,"damage."

hp_enemy = 10
dice()
if dice_number >= 2:
    print "You deal",player_damage, "damage!"
    hp_enemy = hp_enemy - player_damage
elif dice_number < 2:
    print "You miss!"
    
print "Now the enemy attacks"
time.sleep(2)
print "He deals 2 damage"
hp = hp - 2
print "Now it\'s your turn!"
dice()
if dice_number >= 2:
    print "You deal",player_damage, "damage!"
    hp_enemy = hp_enemy - player_damage
elif dice_number < 2:
    print "You miss!"

time.sleep(3)
print "As he sees your strength and dexterity, he decides to flee, but as he turns around to flee, you stab him in the FUCKING back."
print "You find some food in his bag, you cut his head, and head back for the village."
time.sleep(4)
print "Villagers are grateful, and you are given 1000000 gold"
inventory['gold'] = 100000000000000000000000000
print "Thanks for playing!            version 0.2(alpha)"
time.sleep(3)








    
       
    
