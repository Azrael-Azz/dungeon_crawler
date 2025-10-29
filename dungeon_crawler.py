import time
import random

# decalring lists
shop_items = ["health potion           - Worth 50  G",
              "orichalcum armour       - Worth 500 G",
              "durandal,powerful sword - Worth 500 G",
              "Go back to Central Town"]

player_items = ["Dagger",
                "Steel Armour"]

locations = ["Shop: Preparation is must for an adventurer",
             "Inn: A place to rest",
             "Dungeon: Dark place where demon forces lie"]

player_offense_moves = ["You attack demon with all your might"]

player_defense_moves = ["You block the demon attack with your weapon"]

enemy_offense_moves = ["The demon charges at you with full force"]

enemy_defense_moves = ["Demon has a blocked your attack"]

player = ""
armour = "available"
durandal = "available"
gold = 500
player_health = 100
player_offense_min = 0
player_offense_max = 30
player_defense = 10
enemy_health = 100
enemy_offense_min = 0
enemy_offense_max = 0
enemy_defense = 0
dungeon_explore_count = 0
game_over = "deactivate"
player_status = ""
tomb_password = ""


# function to print messages with a 2 second delay
def print_pause(message):
    print(message)
    time.sleep(2)


# function to display the 'items in the list' with a serial number
def list_serial(list):
    for index in range(len(list)):
        print_pause(f"{index+1}. {list[index]}")
    print_pause("\n")
    return ""


# function to remove a specific item from a list
def remove_item(list, item):
    new_list = []
    for index in range(len(list)):
        if list[index] != item:
            new_list.append(list[index])
    list = new_list
    return list


# function to increase heal player's health within the limit of 100
def health_increase(num):
    global player_health
    if player_health < 100 and player_health > 0:
        player_health += num
        if player_health > 100:
            player_health = 100
        return player_health


# function to decrease player's health within the threshold of 0
def health_decrease(health, num):
    if health > 0:
        health += num
        if health < 0:
            health = 0
        return health
    else:
        health = 0
        return health


# function to display a message whenever the gold is insufficient
def low_gold_message():
    global gold
    global player
    print_pause(f"NOTE: You do not have enough cash {player}!")
    print_pause(f"Your Gold : {gold}")
    print_pause("NOTE: Defeat the demons to obtain gold.")


# main scenario
def dungeon_crawler():
    global player
    # input to ask for the player's name
    player = input("\nWitch: What is your name? Stranger\n")
    print_pause(f"\nWitch: Welcome to our world. {player}.")
    print_pause("\nWe have summoned you in hopes to defeat the Demon King."
                "Demon King is spreading chaos in this world.")
    print_pause("\nWill you please help us?")
    decision = input("\n1. Yes. I shall vanquish the demon lord?"
                     "\n2. No, I am busy. Send me back\n\n")
    if "yes" in decision:
        print_pause("\nWitch: Thank you, Hero."
                    " Here is 500 G, A Dagger and Steal Armour.")
        print_pause("\nPrepare for your journey. Go to Center Square"
                    "and to shop and buy armour or sword. ")
        print_pause("\nPlease save this world from chaos.")
        print_pause("\nI don't have much energy left after summoning ritual. "
                    "Good Luck, Hero")
        town()

    elif "no" in decision:
        print_pause("\nWitch: As sad as it is, We shall send you back to your world."
                    " It is our fight to begin with")
        lazyEnd()

    else:
        print_pause("Please enter yes or no")
        dungeon_crawler()


def town():
    if game_over == "activate":
        print_pause("\n\nGame over. Try again ........")
        exit()

    print_pause("\nWelcome to Central Town where all path are connected to.")
    print_pause("Where would you like to venture into:")
    # displays list of town locations in a serial list
    location_choice = input(list_serial(locations)).lower()
    # if player decides to enter into the shop
    if "shop" in location_choice:
        print_pause("\nYou have entered shop to prepare")
        shop()
    # if player decides to enter into the Inn
    elif "inn" in location_choice:
        print_pause("\nYou have checked into an Inn")
        inn()
    # if player decides to enter into the dungeon
    elif "dungeon" in location_choice:
        print_pause("\nYou have entered the dungeon. Be careful")
        dungeon()
    else:
        print_pause("The place you are looking for does"
                    "not exist in this world")
        town()


# funtion to trigger shop sequence in the game
def shop():
    global gold
    global shop_items
    global player_items
    global player
    global player_status
    global player_offense_min
    global player_offense_max
    global player_defense
    global player_health
    global armour
    global durandal

    print_pause("Shopkeeper: Welcome to the shop.")
    print_pause("We have a large collection from far lands ")
    print_pause("Feel free to browse through them.")
    print_pause("What do you want to purchase? Name it.")
    # Displays shops items in a serial list and take desired input from player
    shop_choice = input(list_serial(shop_items)).lower()
    # if player wants to buy health potion in the shop
    if "health" in shop_choice:
        if gold >= 50 and player_health < 100:
            print_pause("Shopkeeper: One must stock up on health or "
                        "face death")
            print_pause(f"Gold: {gold}, -50")
            gold -= 50
            print_pause(f"Your Gold: {gold}")
            health_increase(25)
            print_pause("Your health increased +25, feel healthier now ?")
            print_pause(f"Your Health: {player_health}")
        elif player_health == 100:
            print_pause("SHOPKEEPER: You already have full health")
        elif gold < 50:
            low_gold_message()

    elif "armour" in shop_choice and armour == "available":
        if gold >= 500:
            print_pause("SHOPKEEPER: Made from the rarest metal."
                        "\nSaid to protect you even from Demon Lord")
            print_pause(
                "Note: Now you have 'Orichalcum Armour' in your possession")
            shop_items = remove_item(shop_items,
                                     "Orichalcum Armour       - Worth 500 G")
            player_defense = 30
            print_pause(
                "Your defense has increased to 30. You now feel sturdy")
            armour = "not available"
            print_pause(f"Gold: {gold}, -500")
            gold -= 500
            print_pause(f"Your Gold: {gold}")
        else:
            low_gold_message()

    # if player wants to buy 'durandal' in the shop
    # player cannot buy this item, if the item is already sold out
    elif "durandal" in shop_choice and durandal == "available":
        if gold >= 500 and "Excaliber" not in player_items:
            print_pause("SHOPKEEPER: A great sword for the true warrior")
            print_pause("SHOPKEEPER: It is said to bring out the inner "
                        "strenth of the warrior from the depths of volcano")
            print_pause("NOTE: You now possess the 'Durandal', a mighty sword")
            player_offense_min = 30
            player_offense_max = 50
            print_pause(
                f"NOTE: Your offense has increased to: {player_offense_max}")
            print_pause("NOTE: You are more stronger now and")
            print_pause("      ready to fight stronger enemies.")
            shop_items = remove_item(shop_items,
                                     "Durandal,a mighty sword - Worth 500 G")
            player_items.append("Durandal")
            durandal = "not available"
            print_pause(f"Gold: {gold}, -500")
            gold -= 500
            print_pause(f"Your Gold: {gold}")
        elif "Excaliber" in player_items:
            print_pause("SHOPKEEPER: You already possess a more "
                        "powerful sword")
            print_pause("SHOPKEEPER: These is no need to buy this sword")
        elif gold < 500:
            low_gold_message()

    # if player wants to get back to the town
    elif "go back" in shop_choice:
        print_pause("You head back to the town")
        town()
    # if player gives an unrecognized input
    else:
        print_pause("SHOPKEEPER: I don't understand, "
                    "Specify the name of the item clearly")
        shop()
    # After trading, player has to get back to town
    print_pause("\nYou took care of the business in shop, as of now "
                "and head back to the Central Town")
    town()


# a function to run 'inn' sequence
def inn():
    print_pause("This is a place to rest & refresh your body and soul")
    inner_inn()


# A branch sequence to the funtion 'inn'
def inner_inn():
    # player's choice
    print_pause("\nWhat would you like to do:")
    inn_choice = input("1. Rent a Room"
                       "\n2. go back to town\n").lower()
    # if player chooses to enter the room
    if "room" in inn_choice:
        room()
    # if player chooses to enter the town
    elif "go back" in inn_choice:
        town()
    # condition to deal with unrecognized input
    else:
        print_pause("Enter a valid choice: room? or town?")
        inner_inn()


# A branch sequence to the funtion 'inner_inn'
def room():
    global gold
    print_pause("\nYou enterd the room all tired and depraved of sleep")
    print_pause("You were charged 20 gold for the room")
    print_pause(f"Gold: {gold}, -20")
    gold -= 20
    print_pause(f"Your Gold: {gold}")
    room_sequense()


# A branch sequence to the funtion 'room'
def room_sequense():
    global player_items
    print_pause("\nWhat would yo do now?")
    room_action = input("1. Sleep"
                        "\n2. Examine the room\n").lower()
    # if player wants to sleep on bed
    if "sleep" in room_action:
        print_pause("\nIt is time to rest your body")
        room_choice()
    # if player wants to examine the room
    elif "examine" in room_action:
        print_pause("\nYou examine the room throughly for any "
                    "possible anamoly")
        print_pause("You find an old article eating dust behind the "
                    "closet")
        print_pause("You read it, out of curiosity")
        print_pause("\nThe book tells you about Excaliber a sword weilded by A Mighty King,"
                    "\nand a line that is written in bold (all for the peace)")
        print_pause("\nIt is time to rest your body")
        room_choice()
    # condition to deal with unrecognized input
    else:
        print_pause("Enter a valid action in words")
        room_sequense()


def room_choice():
    print_pause("Your health increased by 50")
    print_pause(f"Health : {player_health}, +50")
    health_increase(50)
    print_pause(f"Your Health: {player_health}")
    print_pause("\nYou head back to the Inn entrance")
    inn()

# A branch sequence to the funtion


def fight_sequence(enemy_offense_min, enemy_offense_max, enemy_defense):
    global player_health
    global player_offense_min
    global player_offense_max
    global player_defense
    global enemy_health
    global player_offense_moves
    global player_defense_moves
    global enemy_offense_moves
    global enemy_defense_moves
    global game_over
    global gold

    # a loop to let player and enemy deal random damage in each turn
    for turn in range(40):
        # if trun is even number and player is alive
        if turn % 2 == 0 and player_health > 0:
            print_pause("You Attack the Demon")
            print_pause(random.choice(player_offense_moves))
            print_pause(random.choice(enemy_defense_moves))
            # assign random number with in the range to player's offence
            player_offense = random.randint(player_offense_min,
                                            player_offense_max)
            enemy_damage = enemy_defense - player_offense
            # as damage decreases the health, it cannot be a positive number
            if enemy_damage > 0:
                enemy_damage = 0
            print_pause(f"Enemy damage : {enemy_damage}")
            # decrement enemy health based on damage
            enemy_health = health_decrease(enemy_health, enemy_damage)
            # display both player's and enemy's health
            print_pause(f"Player_health: {player_health}")
            print_pause(f"Enemy_health : {enemy_health}\n")
        # if trun is odd number and enemy is alive
        elif turn % 2 == 1 and enemy_health > 0:
            print_pause(f"Demon Attacks....//")
            print_pause(random.choice(enemy_offense_moves))
            # print random message from the list 'player_defense_moves'
            print_pause(random.choice(player_defense_moves))
            # assign random number with in the range to enemy's offence
            enemy_offense = random.randint(enemy_offense_min,
                                           enemy_offense_max)
            player_damage = player_defense - enemy_offense
            # as damage decreases the health, it cannot be a positive number
            if player_damage > 0:
                player_damage = 0
            print_pause(f"Player damage: {player_damage}")
            # decrement player's health based on damage
            player_health = health_decrease(player_health, player_damage)
            # display both player's and enemy's health
            print_pause(f"Player_health: {player_health}")
            print_pause(f"Enemy_health : {enemy_health}\n")
        # if enemy loses the battle
        if player_health > 0 and enemy_health <= 0:
            print_pause(f"You have successfully slain the demon")
            print_pause("You emerge victorious !!")
            print_pause("The enemy dropped gold")
            gold += 50
            print_pause(f"Gold: {gold}, -500")
            return "player wins"
        # if player loses the battle
        elif player_health <= 0 and enemy_health > 0:
            print_pause("You lost this battle....")
            print_pause("You are dead.")
            game_over = "activate"
            town()


# funtion to trigger the location 'dungeon'
def dungeon():
    print_pause("You venture to kill demons in dungeon")
    print_pause("The dungeon is vast and dark")
    dungeon_choice()


# A branch sequence to the funtion 'dungeon'
def dungeon_choice():
    print_pause("\nWhat action will you take?")
    dungeon_action = input("\n1. Explore"
                           "\n2. Go back to central town\n")
    if dungeon_action == "explore":
        print_pause("NOTE: The dungeon is complex")
        dungeon_explore()
    # if player chooses to return to the town
    elif dungeon_action == "2":
        print_pause("You head back to the town")
        town()
    # condition to deal unrecognized input
    else:
        print_pause("Enter a valid number")
        dungeon_choice()


# A branch sequence to the funtion 'dungeon_choice'
def dungeon_explore():
    global player_items
    global dungeon_explore_count

    enemy_attack = random.choice(["no", "yes", "no", "no"])

    if enemy_attack == "yes":
        print_pause("You have been ambushed by enemy")
        fight_result = fight_sequence(0, 30, 5)

        # if player wins
        if fight_result == "player wins":
            print_pause("You resume your search")
        # if player loses, the sequence is executed in 'fight_sequence'
    dungeon_explore_count += 1
    # if exlpore input/count is given more than 2 times,
    if dungeon_explore_count > 2:
        print_pause("You found the 'Lost Tomb of King Authur'")
        print_pause("The tomb is sealed off and require a keyword password")
        tomb()

    # condition to loop back to explore option
    else:
        print_pause("Please choose explore or go back")
        dungeon_explore()
    dungeon_explore()


# A branch sequence to the funtion 'dungeon_explore'
def tomb():
    global player_items
    global player_offense_min
    global player_offense_max

    tomb_keyword = input("Enter the keyword: ")
    # if the keyword input is correct
    if tomb_keyword == "all for peace":
        print_pause("\nThe Authur's Tomb gates open with crackling sound")
        print_pause("You enter thr tomb cautiously")
        print_pause("You find the legendary"
                    " sword: The Excaliber next to a tomb")
        print_pause("You have accquired the Legendary sword: Excaliber")
        player_items.append("Excaliber")
        # player stats will be increased
        player_offense_min = 50
        player_offense_max = 80
        print_pause("\nNOTE: Your offense has increased "
                    f"to: {player_offense_max}")
        print_pause("NOTE: You are stronger than ever")
        print_pause("As you take the Excaliber. You send your prayers "
                    "observing tomb where letters were engraved")
        print_pause(
            "You read the engravings that says a famous propeht once said "
            "the demon king lies within the king but a hero will come,"
            " take the sword and "
            "save the world.")
        print_pause(
            "You decide to trust the engravings and think weather to challenge the king")
        challenge_king()
    # if the keyword input is not matched
    else:
        print_pause(
            "NOTE: Wrong password, try again? Maybe you will find something at inn")
        room_action = input("1. Try again."
                            "\n2.go back to town\n").lower()
    if "try" in room_action:
        tomb()
    # if player wants to examine the room
    elif "go back" in room_action:
        town()


def challenge_king():
    # player's choice
    print_pause("\nWould you challenge the king to a battle ?")
    challenge = input("1. yes, challenge the king"
                      "\n2. No, not yet\n").lower()
    # if player chooses to fight the king
    if "yes" in challenge:
        print_pause("\nYou challenge the king to single combat")
        print_pause("The king did not hesitate to accept the challenge\n")
        fight_result = fight_sequence("King", 50, 70, 50)
        # if player wins
        if fight_result == "player wins":
            print_pause("The king is on his final breath")
            print_pause("You approach him with your sword drawn")
            kings_fate_scenario()
    # if player chooses not to fight the king
    elif "no" in challenge:
        print_pause("\nYou were not ready yet")
        print_pause("You decided to wait for the right time")
        print_pause("You head back to the central town")
        town()
    # condition to deal with unrecognized input
    else:
        print_pause("\nNOTE: Enter the correct words\n")
        challenge_king()


def kings_fate_scenario():
    # player's choice
    print_pause("\nEnter the number of your choice :")
    kings_fate = input("1. Kill the king and finish once and for all"
                       "\n2. Somethings not right, spare his life\n")
    # if player decides to kill the king
    if kings_fate == "1":
        print_pause("\nYou deliver a powerful blow to the king ")
        print_pause("The king took the final blow with out any "
                    "resistance")
        print_pause("almost as if he wanted you to slay him !!")
        print_pause("You have slain the monster, but something feels unsettled"
                    " to you.")
        print_pause("You were branded as king's slayer and abolished "
                    "from the kingdom")
        print_pause(".")
        print_pause(".")
        print_pause(".")
        print_pause(".")
        badEnd()

    # if player decides not to kill the king
    elif kings_fate == "2":
        print_pause("\nYou take a leap of faith, to spare the king's life")
        print_pause("You gave the king a chance to explain his actions")
        print_pause("The king is in no condition to talk to you,")
        print_pause("He appears to be be possessed")
        print_pause("\nYou sense a dark presence lurking in the shadows !!")
        print_pause("It appears to be the monster, manipulating the king all"
                    " along")
        print_pause("The king is nothing but a puppet,\n a victim to monster's"
                    " vicious nature")
        print_pause("You leap towards the monster at full throttle")
        print_pause("The monster was caught off gaurd and wonded badly")
        print_pause("\nThe monster actually is the demon lord"
                    "\ndisguised itself as a human !!\n")
        print_pause("The monster is both wounded and drain from "
                    "manipulating king")
        print_pause("This is the perfect chance to end this once "
                    "and for all..\n")
        fight_result = fight_sequence("Monster", 40, 60, 40)
        if fight_result == "player wins":
            print_pause("The monster is finally slain")
            print_pause("You rescued the king and the world from the "
                        "monster's evil plan")
            print_pause("You were rewarded with gold and title in the "
                        "kingdom\n")
            print_pause("------------------ GAME ENDED -------------------")
            goodEnd()
    # condition to deal with unrecognized input
    else:
        print_pause("\nEnter the number of your choice to decide king's fate")
        kings_fate_scenario()


# Endings
def goodEnd():
    global player
    print_pause("Triggered Good Ending")
    print_pause(
        "\n\n Thank you for saving this world. We are grateful to you." + player + " .")
    exit()


def badEnd():
    print_pause("Triggered Bad Ending")
    print_pause("After 4 weeks of the incident")
    print_pause("You were drinking in an Inn in the neighbouring"
                " town")
    print_pause("You enquire the BARTENDER for the info as a daily"
                " routine")
    print_pause("According to the information,")
    print_pause("The princess was kidnapped by the monster and "
                "never returned !!")
    print_pause("As suspected, the monster was not the king !!")
    print_pause("There is something behind the scenes playing the king")
    print_pause("Time to return....//\n")


def lazyEnd():
    print_pause("\nTriggered Lazy End:\nYou were sent back to your world and lived your repetitive boring life peacefully. "
                "\nUnbenounced to you a world had fallen into chaos due to your laziness.")


dungeon_crawler()
