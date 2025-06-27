# Adding backpack
backpack = []
# Maximum capacity of the backpack
MAX_CAPACITY = 7

#backpack helper function
def add_to_backpack(item):
    if len(backpack) < MAX_CAPACITY:
        backpack.append(item)
        print(f"You added {item} to your backpack.")
    else:
        print(f"Your backpack is full! You can't take {item}.")

# function to let players choose what items to pick up
def choose_items(items_found):
    for item in items_found:
        if len(backpack) >= MAX_CAPACITY:
            print("Your backpack is full! You can't carry any more items.")
            break
        choice = input(f"Do you want to take '{item}'? (yes/no): ").lower()
        while choice not in ["yes", "no"]:
            print("Please type 'yes' or 'no'.")
            choice = input(f"Do you want to take '{item}'? (yes/no): ").lower()
        if choice == "yes":
            add_to_backpack(item)

#function to remove an item from the backpack
def remove_item():
    if not backpack:
        print("Your backpack is empty. There's nothing to remove.")
        return
    print("Items in your backpack:")
    for i, item in enumerate(backpack, 1):
        print(f"{i}. {item}")
    choice = input("Which item do you want to remove? (type the item name): ")
    if choice in backpack:
        backpack.remove(choice)
        print(f"You removed {choice} from your backpack.")
    else:
        print(f"Your backpack is full! You can't take '{item}'.")
        choice = input("Do you want to remove something from your backpack to make space? (yes/no): ").lower()
        if choice == "yes":
            remove_item()
            # try adding again if space is made
            if len(backpack) < MAX_CAPACITY:
                backpack.append(item)
                print(f"You added {item} to your backpack.")
            else:
                print("Still no space. You left the item behind.")
        else:
            print("You left the item behind.")


# introduction - the start of the story
print("--------------------------------------------------------------------------------------------------------------------------------------------------")
print("\nThe year is 2077, in a post-apocalyptic nuclear world war, you are with your dog named Zuko.\n")
print("Together, you are scavenging, looking for supplies to fit a bag that is limited to only 7 items.")
print("\nYou stumbled upon an dark underground bunker, however, you also see an abandoned city with possible civilization in the distance.\n")
print("--------------------------------------------------------------------------------------------------------------------------------------------------")
print("\nYou have a choice to make: Do you want to search the dark underground bunker or the abandoned city?\n")
choice = input("Type 'bunker' to search the bunker or 'city' to search the city: ").lower()
while choice not in ["bunker", "city"]:
        print("Invalid choice. Please type 'bunker' or 'city'.")
        choice = input("Type 'bunker' to search the bunker or 'city' to search the city: ").lower()


#if they choose to explore the bunker1
if choice == "bunker":
    print("------------------------------------------------------------------------------------------------------------------------")
    print("\nYou and Zuko cautiously enter the dark underground bunker. The air is stale, and the lights flicker ominously.\n")
    print("As you explore, you find some supplies...")
    bunker_items = ["flashlight", "first aid kit", "food", "makeshift gun parts", "bunker map"]
    choose_items(bunker_items)
    # Allow player to manage backpack before continuing
    while True:
        action = input("Do you want to continue or manage your backpack? (continue/manage): ").lower()
        if action == "manage":
            remove_item()
        elif action == "continue":
            break
        else:
            print("Invalid choice. Please type 'continue' or 'manage'.")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("\nSuddenly, you hear a noise coming from deeper within the bunker.\n")
    print("Do you want to investigate the noise or leave quickly?\n")
    print("------------------------------------------------------------------------------------------------------------------------")
    
    choice = input("Type 'investigate' to check out the noise or 'leave' to exit the bunker: ").lower()
    while choice not in ["investigate", "exit"]:
        print("Invalid choice. Please type 'investigate' or 'exit'.")
        choice = input("Type 'investigate' to check out the noise or 'exit' to exit the bunker: ").lower()


#if they choose to explore the city2
if choice == "city":
    print("--------------------------------------------------------------------------------------------------------------------")
    print("\nYou and Zuko cautiously approach the abandoned city. The buildings are crumbling, and the streets are eerily quiet.\n")
    print("As you explore, you find some supplies...")
    city_items = ["flashlight", "first aid kit", "gun without ammo"]
    choose_items(city_items)
    while True:
        action = input("Do you want to continue or manage your backpack? (continue/manage): ").lower()
        if action == "manage":
            remove_item()
        elif action == "continue":
            break
        else:
            print("Invalid choice. Please type 'continue' or 'manage'.")
    print("\nSuddenly, you hear a noise coming from one of the buildings.\n")
    print("Do you want to check out the noise or leave quickly?\n")
    print("--------------------------------------------------------------------------------------------------------------------")
    choice = input("Type 'check out' to check out the noise or 'exit' to exit the city: ").lower()
    while choice != "check out" and choice != "exit":
        print("Invalid choice. Please type 'check out' or 'exit'.")
        choice = input("Type 'check out' to check out the noise or 'exit' to exit the city: ").lower()
        

# If they choose to investigate the noise1
if choice == "investigate":
    print("-----------------------------------------------------------------------------------------------------------------")
    print("\nYou and Zuko move towards the source of the noise. You find a group of mutated creatures huddled around a fire.\n")
    print("They look at you with curiosity but do not attack. Do you want to try to communicate with them or leave quickly?\n")
    print("-----------------------------------------------------------------------------------------------------------------")

    choice = input("Type 'talk' to try talking to them or 'exit' to exit: ").lower()
    while choice not in ["talk", "exit"]:
        print("Invalid choice. Please type 'talk' or 'exit'.")
        choice = input("Type 'talk' to try talking to them or 'exit' to exit: ").lower()

    if choice == "talk":
        if "bunker map" in backpack:
            # Hostile ending
            paragraph = """You cautiously approach the creatures in an attempt to communicate; however, they seem hostile, and when you look closer, they are very hungry and were cooking wolves on the fire.

You quickly realize that they are not friendly, so you and Zuko run straight out of the bunker in an attempt to escape.

But as you are about to flee, the creatures spot you and Zuko and rush toward you.

You and Zuko fight bravely, but the odds are against you. You are outnumbered and outmatched.

You and Zuko die together harshly in this unforgiving world."""
            print("----------------------------------------------------------------------------------------------------------------------")
            print(paragraph)
            print("----------------------------------------------------------------------------------------------------------------------")

        elif "food" in backpack:
            # Friendly creatures – food trade
            print("------------------------------------------------------------------------------------------------------------------")
            print("\nYou cautiously approach the creatures and try to communicate. Surprisingly, they respond in a broken language.\n")
            print("They seem friendly and offer you supplies in exchange for food.\n")
            backpack.remove("food")
            trade_items = ["filtered water", "ammo clip"]
            choose_items(trade_items)

            while True:
                action = input("Do you want to continue or manage your backpack? (continue/manage): ").lower()
                if action == "manage":
                    remove_item()
                elif action == "continue":
                    break
                else:
                    print("Invalid choice. Please type 'continue' or 'manage'.")

            print("\nYou made new allies. Zuko seems to like them too. You feel a sense of hope in this desolate world.")

        else:
            # No food to trade
            print("------------------------------------------------------------------------------------------------------------------")
            print("\nYou try to communicate, and they seem neutral at first.\n")
            print("However, you have no food to offer. The creatures grow wary of your presence.\n")
            print("Sensing the tension, you decide to leave peacefully with Zuko.\n")
            print("------------------------------------------------------------------------------------------------------------------")

    elif choice == "leave":
        print("\nYou decide not to take the risk. You and Zuko back away quietly and leave the area safely.\n")
        print("------------------------------------------------------------------------------------------------------------------")
    #bugged

#if they choose to leave the bunker
if choice == "exit":
    paragraph = """You decide it's too dangerous to investigate further. You quickly exit the bunker with your supplies.

Outside, you see the abandoned city again, but now you're better prepared to face whatever lies ahead.

Zuko seems relieved, and you both head back to your makeshift camp to rest and plan your next move.

You feel a sense of accomplishment for surviving another day in this unforgiving world.

You woke up the next day, packed all your gathered supplies, and decided to head towards the abandoned city.

As you and Zuko approach the city, the once distant skyline looms closer—its shattered towers casting long shadows in the morning light.

The streets are eerily silent, save for the crunch of debris beneath your boots and the occasional gust of wind whistling through broken windows.

Zuko growls softly, his ears twitching. He's sensed something.

You pause, scanning your surroundings.

Graffiti lines the cracked walls, messages from survivors long gone: "DON'T TRUST THEM", "SAFE ZONE = LIE", and a crude map pointing deeper into the city.

Suddenly, you hear a metallic clatter from around the corner.

You motion for Zuko to stay low as you inch forward, gripping your makeshift weapon tightly.

Peering around the corner, you spot a drone—half-functional, sparking occasionally, scanning the area with a dim blue light.


Zuko looks to you, waiting for your decision."""
    print("--------------------------------------------------------------------------------------------------------------------")
    print(paragraph)
    print("--------------------------------------------------------------------------------------------------------------------")
    choice = input("Type 'disable' to disable the drone to see if it has any data or 'avoid' to head towards the location marked on the map: ").lower()
    while choice != "disable" and choice != "avoid":
        print("Invalid choice. Please type 'disable' or 'avoid'.")
        choice = input("Type 'disable' to disable the drone to see if it has any data or 'avoid' to head towards the location marked on the map: ").lower()

#if they choose to disable the drone
if choice == "disable":
    paragraph = """You disable the drone successfully and extract a storage chip. Zuko barks softly as you work.

After slipping the chip into your portable scanner, the screen flickers to life, revealing detailed patrol routes, radiation zones, 

and a blinking dot labeled *“Safe House?”*—several blocks northeast, buried deep in the red zone.

You quickly mark the location on your map and pack up your gear. Just then, Zuko growls low—there’s something moving in the shadows.

With tension building, you’re left with a critical decision: 

take the direct path to the Safe House through the hazardous red zone, or detour around it to avoid whatever danger might be lurking ahead."""
    print("---------------------------------------------------------------------------------------------------------")
    print(paragraph)
    drone_items = ["drone data"]
    choose_items(drone_items)
    add_to_backpack("drone data")
    print("---------------------------------------------------------------------------------------------------------")
    choice = input("Type 'direct' to go straight to the Safe House or 'detour' to take the longer, safer path: ").lower()
    while choice not in ["direct", "detour"]:
        print("Invalid choice. Please type 'direct' or 'detour'.")
        choice = input("Type 'direct' or 'detour': ").lower()

# if they choose to go directly to the Safe House
    if choice == "direct":
        print("---------------------------------------------------------------------------------------------------------")
        print("\nYou press forward through the red zone. The air is thick, and the buildings creak with every step.\n")
        print("Zuko sticks close. Suddenly, gunfire echoes nearby. Raiders.\n")
        if "ammo clip" in backpack and "gun without ammo" in backpack:
            print("\nYou quickly reload your gun using the ammo clip from earlier. With Zuko’s help, you fend off the ambush.\n")
            print("You survive—but barely. Zuko is injured, and you use your first aid kit to treat him.\n")
            backpack.remove("first aid kit")
            print("\nBloodied but alive, you arrive at the Safe House. The reinforced door slides open after scanning the drone chip.\n")
            print("Inside, clean water, medical supplies, and a working radio greet you. You’ve found sanctuary... for now.\n")
            print("---------------------------------------------------------------------------------------------------------")
        #no gun/Dead
        else:
            print("---------------------------------------------------------------------------------------------------------")
            print("\nUnarmed, you try to hide—but the raiders spot you. You and Zuko put up a fight, but it’s no use.\n")
            print("You both fall in the firefight. Your journey ends here.\n")
            print("---------------------------------------------------------------------------------------------------------")

# if they choose to detour around the red zone
    elif choice == "detour":
        print("---------------------------------------------------------------------------------------------------------")
        print("\nYou circle around the red zone, navigating alleys and collapsing tunnels.\n")
        print("It takes longer, and you're forced to ration your food.\n")
        print("----------------------------------------------------------------------------------------------------------")
        if "food" in backpack:
            print("-------------------------------------------------------")
            print("\nYou eat just enough to keep moving, sharing with Zuko.\n")
            print("-------------------------------------------------------")
            backpack.remove("food")
        else:
            print("----------------------------------------------------------------------------------------------------------")
            print("\nWithout food, you both grow weak. Zuko stumbles, but you press on.")
            print("At last, you reach the Safe House. The drone chip grants you access.\n")
            print("It’s quiet. Safe. You made the right call.\n")
            print("---------------------------------------------------------------------------------------------------------")

# if they choose to avoid the drone
if choice == "avoid":
    paragraph = """You decide not to risk the drone. You and Zuko follow the map painted on the wall deeper into the city.

The path takes you underground—into the subway system. It’s dark, damp, and claustrophobic.

You can hear the distant sound of water dripping.

Graffiti becomes more frequent, and signs of life appear: torches, food wrappers, paw prints.

You arrive at an old maintenance station, converted into a shelter. A man in a gas mask emerges from the shadows.

"You're not with the Eastern Raiders, are you?" he asks gruffly. Zuko doesn’t growl—he senses no threat.

You shake your head. The man lowers his weapon.

"Then you're welcome here. But you'll need to earn your stay. There's something we need help with..."

You and Zuko exchange a look. This journey is far from over."""
    print("---------------------------------------------------------------------------------------------------------\n")
    print(paragraph)
    print("\n---------------------------------------------------------------------------------------------------------")

#if they choose to check out the noise2/city - fixed loop
if choice == "check out":
    print("-----------------------------------------------------------------------------------------------------------------")
    print("\nYou and Zuko move towards the source of the noise. You find a group of mutated creatures huddled around a fire.\n")
    print("They look at you with curiosity but do not attack. Do you want to try to communicate with them or leave quickly?\n")
    print("-----------------------------------------------------------------------------------------------------------------")
    
    choice = input("Type 'communicate' to try talking to them or 'leave' to exit the city: ").lower()

    while choice != "communicate" and choice != "leave":
        print("Invalid choice. Please type 'communicate' or 'leave'.")
        choice = input("Type 'communicate' to try talking to them or 'leave' to exit the city: ").lower()


#if they choose to communicate with the creatures2
if choice == "communicate":
    print("------------------------------------------------------------------------------------------------------------------")
    print("\nThe creatures—humanoid but deformed from radiation—gesture for you to sit. Their fire crackles softly.\n")
    print("One, who calls himself 'Grak', explains they were once human. Survivors of a failed government experiment.\n")

    if "food" in backpack:
        print("They offer you supplies in exchange for food. You trade willingly, and they hand over clean water and a pouch of used medicine pouch.\n")
        backpack.remove("food")
        city_items = ["clean water", "used medicine pouch"]
        choose_items(city_items)

        while True:
            action = input("Do you want to continue or manage your backpack? (continue/manage): ").lower()
            if action == "manage":
                remove_item()
            elif action == "continue":
                break
            else:
                print("Invalid choice. Please type 'continue' or 'manage'.")

        print("-------------------------------------------------------------------------------------------------------------")
        print("\nZuko warms up to them. You eat, rest, and learn from them.\n")
        print("Grak tells you about the dangers of the city, the raiders, and the radiation storms that sweep through.\n")
        print("He also mentions a place called 'The Core'—a rumored safe haven where technology still works.\n")
        print("-------------------------------------------------------------------------------------------------------------")

    #if they do not have food to trade
    elif "food" not in backpack:
        paragraph = """But you have no food to trade. They still let you stay the night, offering water for your honesty.

You add clean water to your backpack.

Grak marks a location on your map: an old subway entrance that leads toward what they call *“The Core”—*

a place where technology still runs and maybe, just maybe, humanity is trying to rebuild.

You and Zuko rest and leave at dawn, guided by the map.

You now have a new objective: Reach The Core.

But the way won’t be easy. Raiders roam the surface. Radiation storms sweep the ruins. And there’s something worse underground.

You reach the subway entrance. Rusted gates creak open as you descend. Zuko sniffs the air—alert.

Dim emergency lights flicker to life as you make your way into the tunnels. Your flashlight catches movement ahead.

You pause. You hear footsteps and low growls. Not from a creature. From humans.

Do you want to hide and wait for them to pass or call out and try to talk?"""
    print("-------------------------------------------------------------------------------------------------------------\n")
    print(paragraph)
    print("\n------------------------------------------------------------------------------------------------------------------")
    choice = input("Type 'hide' to avoid them or 'talk' to call out and try to communicate: ").lower()
    while choice not in ["hide", "talk"]:
        print("Invalid choice. Please type 'hide' or 'talk'.")
        choice = input("Type 'hide' or 'talk': ").lower()

#if they choose to hide
if choice == "hide":
            print("------------------------------------------------------------------------------------------------------------")
            print("\nYou pull Zuko into the shadows. The figures pass by—armed scavengers wearing makeshift armor.\n")
            print("You wait silently as they disappear into the dark. That was close.\n")
            print("You continue deeper into the tunnels, following the markings from Grak's map.\n")
            print("You eventually find a sealed metal door with a biometric scanner, half-powered.\n")
            #if they have drone data from previous choice
            if "drone data" in backpack:
                print("-------------------------------------------------------------------------------------------------------------")
                print("\nYou insert the drone data chip. The door unlocks with a hiss.\n")
                print("Inside, you're greeted by lights, humming machines, and a voice on a speaker: 'Welcome to The \"Core\", traveler.'\n")
                print("It is like they knew you were coming.\n")
                print("As you took a step, the door seals behind you, and the voice continues, 'We have been expecting you. Please, make yourself at home.'\n")
                print("Then, a small group of survivors who have managed to keep the place running approaches you and greets you warmly, giving you and Zuko food to eat.\n")
                print("--------------------------------------------------------------------------------------------------------------")

            #if no drone data - makes noise to alert the guards/DEAD
            else:
                print("------------------------------------------------------------------------------------------------------------")
                print("\nThe scanner denies you entry. You’ll need technology to bypass this. As you took a step back, the anti-theft alarm blares deafeningly, alerting all the guards in proximity.\n")
                print("As you turn to run, the guards spot you. You and Zuko make a break for it, but you were outnumbered.\n")
                print("You and Zuko died together harshly in this unforgiving world.\n")
                print("------------------------------------------------------------------------------------------------------------")

#if they choose to talk
if choice == "call out":
            paragraph = """You call out. The footsteps stop. Moments later, three humans approach, guns raised.

"You're not one of them?" one asks.

You explain yourself. After a tense moment, they lower their weapons. They're scouts from a survivor faction called Haven.

They’ve also heard of The Core but believe it’s guarded by AI defenses gone rogue.

They offer to escort you part of the way in exchange for help carrying some salvaged tech.

You accept. The road ahead may be dangerous, but you're no longer alone."""
            print("------------------------------------------------------------------------------------------------------------\n")
            print(paragraph)
            print("\n------------------------------------------------------------------------------------------------------------")



#if they choose to leave2 - Dead
if choice == "leave":
        paragraph = """You decide it's too dangerous to investigate further. You quickly exit the city with your supplies.

Outside, you stumble upon a group of hungry, mutated bears in the distance.

Suddenly, they turn their heads toward you and charge in your direction. You quickly hide behind a rusted car.

The bears sniff around, but they don’t seem to notice you. You hold your breath, praying they move on. After a tense moment, they begin to leave.

But just then, Zuko starts barking, drawing their attention.

They turn and rush toward you. You try to run, but it's too late.

The bears catch up to you and Zuko, and you realize this is the end. You fought bravely, but the odds were against you.

You and Zuko die together, harshly, in this unforgiving world."""
        print("-------------------------------------------------------------------------------------------------------------\n")
        print(paragraph)
        print("\n-------------------------------------------------------------------------------------------------------------")

#at the end of the game to show backpack contents
print("\nYour final backpack contents: {}".format(backpack))
print("\nRemember, in this world, survival is never guaranteed. Every choice matters, and every item counts.\n")
print("Thank you for playing!\n")
#ending