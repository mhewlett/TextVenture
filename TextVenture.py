import random
exp_total = 0
dragon_hp = 200
player_hp = 100
attack = 8
dragon_attack = 12
dragon_fire = 25
gold = 0
loot = ["Sword", "Shield", "Training"]
inventory = []
name = input("Enter your name, hero: ")
print("\nWelcome " + name + ". I hope you are prepared for great adventure!")
print("The King has requested us to defeat a dragon.")
print()
print("Before you can take on the dragon you will need to acquire the following: ")
while "Shield" not in inventory:
    print()
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
    print()
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
        print()
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
    print()
    select = input("What would you like to acquire next? Choose option 1 or 2: ")
    print()
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
                gold = gold - 5
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
    loop = 'y'
    while loop.lower() == 'y':
        input("You walk around the area for a while to find the royal pests.")
        input("You look around the courtyard.")
        input("You smell something foul nearby.")
        input("You spot the shadow of a critter!")
        input("You give chase until you corner the poor bastard!")
        input("A rat appears!")
        rat_hp = 12
        rat_attack = 2
        list = ["1. Attack", "2. Potion", "3. Run"]
        pick = 0
        while True:
            if player_hp <= 0:
                print()
                print("*************************************")
                print("You have run out of HP. You are dead.")
                quit()
            if exp_total >= 21 and "4. Level-Up" not in inventory:
                if "4. Level-Up" not in list:
                    list.append("4. Level-Up")

            print("**************************")
            print(list)
            print(name + "'s HP " + str(player_hp) + " | Rat's HP " + str(rat_hp))
            print("**************************")
            pick = input("What do you want to do? ")
            if pick.isdigit():
                pick = int(pick)
                action = pick - 1
                if "4. Level-Up" not in list:
                    if pick < 1 or pick > 3:
                        print("Your selection is out of bounds.")
                        continue
                elif pick < 1 or pick > 4:
                    print("Your selection is out of bounds.")
                    continue
            else:
                print("You entered incorrectly")
                continue
            if rat_hp <= 0:
                rat_hp = 0
                print("The rat has died.")
                print("You've earned 1 gold.")
                gold = gold + 1
                print("You receive 3 exp.")
                exp_total = exp_total + 3
                print("You now have " + str(gold) + " gold.")
                break
            if pick == 4:
                inventory.append("4. Level-Up")
                attack = attack * 1.5
                player_hp = player_hp + 50
                list.pop(3)
                print("************************************")
                print("*    Your attack and HP increase!  *")
                print("************************************")
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
                    if "4. Level-Up" in inventory:
                        rat_hp = int(rat_hp - attack)
                        print("You struck the rat for 12 hp!")

                    else:
                        rat_hp = int(rat_hp - attack)
                        print("You struck the rat for 8 hp!")

                    if rat_hp < 0:
                        rat_hp = 0
                        continue
                    else:
                        continue

            elif action == 1:
                print("You've chosen to drink a potion.")
                input()
                if player_hp == 100 and "4. Level-Up" not in inventory:
                    print("You do not need to heal.")
                elif player_hp == 150:
                    print("You do not need to heal.")
                elif player_hp > 125 and player_hp < 150:
                    potion_partial = (150 - player_hp)
                    player_hp = player_hp + potion_partial
                    print("You have healed " + str(potion_partial) + "!")
                elif player_hp > 75 and player_hp < 100 and "4. Level-Up" not in inventory:
                    potion_partial = (100 - player_hp)
                    player_hp = player_hp + potion_partial
                    print("You have healed " + str(potion_partial) + " hp!")
                else:
                    player_hp = player_hp + 25
                    print("You have healed 25 hp!")
                    continue
        loop = input("\nFight again? ")
        print()
print("You are finally prepared to challenge the dragon!\n")
loot.append("Dragon")
while True:
    print(loot)
    print()
    select = input("Did you want to track down the dragon or keep training? 1 or 2: ")
    print()
    if select.isdigit():
        select = int(select)
        if select < 1 or select > 2:
            print("Your selection is out of bounds.")
            print()
            continue
    else:
        print("You only need to enter the number associated with the item.")
        print()
        continue
    choice = select - 1
    if choice == 0:
        loop = 'y'
        while loop.lower() == 'y':
            input("You walk around the area for a while to find the royal pests.")
            input("You look around the courtyard.")
            input("You smell something foul nearby.")
            input("You spot the shadow of a critter!")
            input("You give chase until you corner the poor bastard!")
            input("A rat appears!")
            rat_hp = 12
            rat_attack = 2
            list = ["1. Attack", "2. Potion", "3. Run"]
            pick = 0
            while True:
                if player_hp <= 0:
                    print()
                    print("*************************************")
                    print("You have run out of HP. You are dead.")
                    quit()
                if exp_total >= 21 and "4. Level-Up" not in inventory:
                    if "4. Level-Up" not in list:
                        list.append("4. Level-Up")

                print("**************************")
                print(list)
                print(name + "'s HP " + str(player_hp) + " | Rat's HP " + str(rat_hp))
                print("**************************")
                pick = input("What do you want to do? ")
                if pick.isdigit():
                    pick = int(pick)
                    action = pick - 1
                    if "4. Level-Up" not in list:
                        if pick < 1 or pick > 3:
                            print("Your selection is out of bounds.")
                            continue
                    elif pick < 1 or pick > 4:
                        print("Your selection is out of bounds.")
                        continue
                else:
                    print("You entered incorrectly")
                    continue
                if rat_hp <= 0:
                    rat_hp = 0
                    print("The rat has died.")
                    print("You've earned 1 gold.")
                    gold = gold + 1
                    print("You receive 3 exp.")
                    exp_total = exp_total + 3
                    print("You now have " + str(gold) + " gold.")
                    break
                if pick == 4:
                    inventory.append("4. Level-Up")
                    attack = attack * 1.5
                    player_hp = player_hp + 50
                    list.pop(3)
                    print("************************************")
                    print("*    Your attack and HP increase!  *")
                    print("************************************")
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
                        if "4. Level-Up" in inventory:
                            rat_hp = int(rat_hp - attack)
                            print("You struck the rat for 12 hp!")
                            continue
                        else:
                            rat_hp = int(rat_hp - attack)
                            print("You struck the rat for 8 hp!")
                            continue
                elif action == 1:
                    print("You've chosen to drink a potion.")
                    input()
                    if player_hp == 100 and "4. Level-Up" not in inventory:
                        print("You do not need to heal.")
                    elif player_hp == 150:
                        print("You do not need to heal.")
                    elif player_hp > 125 and player_hp < 150:
                        potion_partial = (150 - player_hp)
                        player_hp = player_hp + potion_partial
                        print("You have healed " + str(potion_partial) + "!")
                    elif player_hp > 75 and player_hp < 100 and "4. Level-Up" not in inventory:
                        potion_partial = (100 - player_hp)
                        player_hp = player_hp + potion_partial
                        print("You have healed " + str(potion_partial) + " hp!")
                    else:
                        player_hp = player_hp + 25
                        print("You have healed 25 hp!")
                        continue
            loop = input("\nFight again? ")
            print()
        continue

    else:
        print("Lets go hunt a dragon!")
        print(".")
        print(".")
        print(".")
        print("End of part one.")
        break



