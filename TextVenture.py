import random
dragon_hp = 200
player_hp = 100
rat_attack = 2
dragon_attack = 12
dragon_fire = 25
gold = 0
loot = ["Sword", "Shield", "Training"]
inventory = []
name = input("Enter your name, hero: ")
print("Welcome " + name + ". I hope you are prepared for great adventure!")
print("The King has requested us to defeat a dragon.")
print()
print("Before you can take on the dragon you will need to acquire the following: ")
while "Shield" not in inventory:
    print(loot)
    select = input("\nWhat would you like to acquire first? Choose option 1, 2, or 3: ")
    if select.isdigit():
        select = int(select)
        if select < 1 or select > 3:
            print("Your selection is out of bounds.")
            continue
    else:
        print("You only need to enter the number associated with the item.")
        continue
    choice = select - 1
    print("You have selected to acquire the " + loot[choice].lower() + "! ")
    if select == 1:
        print()
        print("The sword is located in the armory.")
        print("You enter the armory and see the sword mounted to the wall.")
        input("Press enter to grab the sword from the mount.\n")
        print("As you approach it, you feel great power emanating from it.")
        print("You reach up and pull the sword fixed to the mount.\n")
        print("************************************")
        print("*   You have acquired the sword!   *")
        print("************************************")
        loot.pop(int(choice))
        inventory.append("Sword")
        break
    elif select == 2:
        print()
        print("The shield is located in the shop.")
        print("You enter the shop and find the price of the shield to be 5 gold.")
        print("Uh oh...")
        input("")
        print("You do not have enough gold to buy the shield at this time.")
        print("You will need to return when you have more gold.")
        continue
    else:
        print()
        print("You decide to speak with the nearby guard about training.")
        print("The guard looks you up and down and scoffs at you.")
        print("'Did you think that you could train without the proper gear?'")
        print("'You will at least need to equip yourself with a sword first!'")
        print("'Come back once you've found a sword.'")
        print()
        continue
while True:
    print(loot)
    input()
    select = input("\nWhat would you like to acquire next? Choose option 1 or 2: ")
    if select.isdigit():
        select = int(select)
        if select < 1 or select > 2:
            print("Your selection is out of bounds.")
            continue
    else:
        print("You only need to enter the number associated with the item.")
        continue
    choice = select - 1
    print("You have selected to acquire the " + loot[choice].lower() + "! ")
    if select == 1:
        print()
        print("The shield is located in the shop.")
        print("You enter the shop and find the price of the shield to be 5 gold.")
        if gold >= 5:
            buy_shield = input("Would you like to purchase the shield for 5 gold? (Y or N) ")
            if buy_shield.lower() == 'y':
                print()
                print("************************************")
                print("*   You have acquired the shield!  *")
                print("************************************")
                print()
                loot.pop(int(choice))
                break
            else:
                print("You decided not to purchase the shield.")
                print("You have left the shop.")
                continue
        else:
            print("Uh oh...")
            input("")
            print("You do not have enough gold to buy the shield at this time.")
            print("You will need to return when you have more gold.")
            continue
    print()
    print("You decide to speak with the nearby guard about training.")
    if "Sword" in inventory:
        print("The guard looks you up and down.")
        print("'I see that you have a sword. Let's practice using it!'")
        print("'See those rats over there? I'll give you 1 gold for every rat you slay.'")
    else:
        print("The guard looks you up and down and scoffs at you.")
        print("'Did you think that you could train without the proper gear?'")
        print("'You will at least need to equip yourself with a sword first!'")
        print("'Come back once you've found a sword.'")
        print()
        continue
    print("Lets go fight some rats!")
    input()
    import random
    loop = 'y'
    while loop.lower() == 'y':
        input("You walk around the area for a while to find the royals pests.")
        input("You look around the courtyard.")
        input("You smell something foul nearby.")
        input("You spot the shadow of a critter!")
        input("You give chase until you corner the poor bastard!")
        input("A rat appears!")

        rat_hp = 16
        attack = 8
        rat_attack = 2

        list = ["1. Attack", "2. Potion", "3. Run"]
        while True:
            print("**************************")
            print(list)
            print(name + "'s HP " + str(player_hp) + " | Rat's HP " + str(rat_hp))
            print("**************************")
            pick = input("What do you want to do? ")
            if pick.isdigit():
                pick = int(pick)
                action = pick - 1
                if pick < 1 or pick > 3:
                    print("Your selection is out of bounds.")
                    continue
            else:
                print("You entered incorrectly")
                continue
            if rat_hp <= 0:
                print("The rat has died.")
                print("You've earned 1 gold.")
                gold = gold + 1
                print("You now have " + str(gold) + " gold.")
                break
            else:
                acc = random.randint(1, 2)
                print("The rat attacks!")
                input()
                if acc != pick:
                    print("The attack missed!")
                else:
                    player_hp = player_hp - rat_attack
                    print("You took damage!")
            print("**************************")
            if action == 2:
                print("You've chosen to run.")
                input()
                run = random.randint(1, 3)
                if run != action:
                    print("You were unable to get away!")
                    continue
                else:
                    print("You got away safely.")
                    break
            elif action == 0:
                print("You try to attack the rat.")
                input()
                acc = random.randint(1, 2)
                if acc != pick:
                    print("Your attack missed!")
                    continue
                else:
                    rat_hp = rat_hp - attack
                    print("You struck the rat for 8 hp!")
                    continue
            elif action == 1:
                print("You've chosen to drink a potion.")
                input()
                player_hp = player_hp + 25
                print("You have healed 25 hp!")
                continue
        loop = input("\nFight again?")
        print()

print("You are finally prepared to challenge the dragon!")


