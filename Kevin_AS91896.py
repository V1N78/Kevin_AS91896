# Adding backpack
backpack = []
MAX_CAPACITY = 12

# Backpack helper function
def add_to_backpack(item):
    if len(backpack) < MAX_CAPACITY:
        backpack.append(item)
        print("You added {} to your backpack.".format(item))
    else:
        print("Your backpack is full! You can't take {}.".format(item))

#introduction - the start of the story
print("--------------------------------------------------------------------------------------------------------------------------------------------------")
print("The year is 2087, in a post-apocalyptic nuclear world war, you are with your dog named Zuko. Together, you are scavenging, looking for supplies.")
print()
print("You stumbled upon an dark underground bunker, however, you also see an abandoned city with possible civilization in the distance.")
print("--------------------------------------------------------------------------------------------------------------------------------------------------")
print()
print("You have a choice to make: Do you want to search the dark underground bunker or the abandoned city?")
choice = input("Type 'bunker' to search the bunker or 'city' to search the city: ").lower()
while choice not in ["bunker", "city"]:
        print("Invalid choice. Please type 'bunker' or 'city'.")
        choice = input("Type 'bunker' to search the bunker or 'city' to search the city: ").lower()


#if they choose to explore the bunker1
if choice == "bunker":
    print("------------------------------------------------------------------------------------------------------------------------")
    print()
    print("You and Zuko cautiously enter the dark underground bunker. The air is stale, and the lights flicker ominously.")
    print()
    print("As you explore, you find some supplies...")
    add_to_backpack("flashlight")
    add_to_backpack("first aid kit")
    add_to_backpack("food")
    add_to_backpack("makeshift gun parts")
    add_to_backpack("bunker map")
    print()
    print("Suddenly, you hear a noise coming from deeper within the bunker.")
    print()
    print("Do you want to investigate the noise or leave quickly?")
    print()
    print("------------------------------------------------------------------------------------------------------------------------")
    choice = input("Type 'investigate' to check out the noise or 'leave' to exit the bunker: ").lower()
    while choice not in ["investigate", "leave"]:
        print("Invalid choice. Please type 'investigate' or 'leave'.")
        choice = input("Type 'investigate' to check out the noise or 'leave' to exit the bunker: ").lower()


#if they choose to explore the city2
if choice == "city":
    print("--------------------------------------------------------------------------------------------------------------------")
    print()
    print("You and Zuko cautiously approach the abandoned city. The buildings are crumbling, and the streets are eerily quiet.")
    print()
    print("As you explore, you find some supplies...")
    add_to_backpack("flashlight")
    add_to_backpack("first aid kit")
    add_to_backpack("gun without ammo")
    print()
    print("Suddenly, you hear a noise coming from one of the buildings.")
    print()
    print("Do you want to investigate the noise or leave quickly?")
    print()
    print("--------------------------------------------------------------------------------------------------------------------")
    choice = input("Type 'investigate' to check out the noise or 'leave' to exit the city: ").lower()
    while choice != "investigate" and choice != "leave":
        print("Invalid choice. Please type 'investigate' or 'leave'.")
        choice = input("Type 'investigate' to check out the noise or 'leave' to exit the city: ").lower()
        

# #if they choose to investigate the noise1 - problem on loop
# if choice == "investigate":
#         print("-----------------------------------------------------------------------------------------------------------------")
#         print()
#         print("You and Zuko move towards the source of the noise. You find a group of mutated creatures huddled around a fire.")
#         print()
#         print("They look at you with curiosity but do not attack. Do you want to try to communicate with them or leave quickly?")
#         print()
#         print("-----------------------------------------------------------------------------------------------------------------")
#         choice = input("Type 'communicate' to try talking to them or 'leave' to exit the bunker: ").lower()
# while choice not in ["communicate", "leave"]:
#         print("Invalid choice. Please type 'communicate' or 'leave'.")
#         choice = input("Type 'communicate' to try talking to them or 'leave' to exit the bunker: ").lower()


#if they choose to communicate with the creatures1 - Dead
if choice == "communicate":
    if "bunker map" in backpack:
        #hostile ending
        print("----------------------------------------------------------------------------------------------------------------------")
        print("You cautiously approach the creatures in attempt to communicate, however, they seem hostile and when you look closer, they were very hungry and were cooking wolves on the fire.")
        print()
        print("You quickly realize that they were not friendly so you and Zuko ran straight out of the bunker in attempt to escape.")
        print()
        print("But as you were about to escape, the creatures have already spotted you and Zuko, and rushed towards you.")
        print()
        print("You and Zuko fought bravely, but the odds were against you. You were outnumbered and outmatched.")
        print()
        print("You and Zuko died together harshly in this unforgiving world.")
        print("----------------------------------------------------------------------------------------------------------------------")
    else:
        # friendly creatures
        print("------------------------------------------------------------------------------------------------------------------")
        print("You cautiously approach the creatures and try to communicate. Surprisingly, they respond in a broken language.")
        print()
        print("They seem friendly and offer you supplies in exchange for food.")
        if "food" in backpack:
            backpack.remove("food")
            add_to_backpack("filtered water")
            add_to_backpack("ammo clip")
            print("You made new allies. Zuko seems to like them too. You feel a sense of hope in this desolate world.")
        else:
            print("You have no food to trade. They grow wary of you, and you decide to leave peacefully.")
        print("------------------------------------------------------------------------------------------------------------------")


#if they choose to leave the bunker1
elif choice == "leave":
        print("--------------------------------------------------------------------------------------------------------------------")
        print()
        print("You decide it's too dangerous to investigate further. You quickly exit the bunker with your supplies.")
        print()
        print("Outside, you see the abandoned city again, but now you're better prepared to face whatever lies ahead.")
        print()
        print("Zuko seems relieved, and you both head back to your makeshift camp to rest and plan your next move.")
        print()
        print("You feel a sense of accomplishment for surviving another day in this unforgiving world.")
        print()
        print("You woke up the next day, packed all your gathered supplies, and decided to head towards the abondoned city.")
        print()
        print("As you and Zuko approach the city, the once distant skyline looms closer—its shattered towers casting long shadows in the morning light.")
        print()
        print("The streets are eerily silent, save for the crunch of debris beneath your boots and the occasional gust of wind whistling through broken windows.")
        print()
        print("Zuko growls softly, his ears twitching. He's sensed something.")
        print()
        print("You pause, scanning your surroundings.")
        print()
        print("Graffiti lines the cracked walls, messages from survivors long gone: 'DON'T TRUST THEM', 'SAFE ZONE = LIE', and a crude map pointing deeper into the city.")
        print()
        print("Suddenly, you hear a metallic clatter from around the corner.")
        print()
        print("You motion for Zuko to stay low as you inch forward, gripping your makeshift weapon tightly.")
        print()
        print("Peering around the corner, you spot a drone—half-functional, sparking occasionally, scanning the area with a dim blue light.")
        print()
        print("You have a choice to make: try to disable the drone and see if it has any data, or avoid it entirely and head toward the location marked on the map.")
        print()
        print("Zuko looks to you, waiting for your decision.")
        print()
        print("--------------------------------------------------------------------------------------------------------------------")
        choice = input("Type 'disable' to disable the drone to see if it has any data or 'avoid' to head towards the location marked on the map: ").lower()
        while choice != "disable" and choice != "avoid":
                print("Invalid choice. Please type 'disable' or 'avoid'.")
                choice = input("Type 'disable' to disable the drone to see if it has any data or 'avoid' to head towards the location marked on the map: ").lower()

#if they choose to disable the drone
if choice == "disable":
    print("---------------------------------------------------------------------------------------------------------")
    print()
    print("You disable the drone successfully and extract a storage chip. Zuko barks softly as you work.")
    print()
    add_to_backpack("drone data")
    print()
    print("You slot the chip into your portable scanner. The screen flickers, then displays patrol routes, radiation zones, and a blinking dot labeled 'Safe House?'.")
    print()
    print("It’s several blocks northeast, deep in the red zone.")
    print()
    print("You mark the location on your map and pack up. Zuko growls—something's out there.")
    print()
    print("You now face another choice: head directly to the marked Safe House, or detour around the red zone to reduce risk.")
    print()
    print("---------------------------------------------------------------------------------------------------------")
    choice = input("Type 'direct' to go straight to the Safe House or 'detour' to take the longer, safer path: ").lower()
    while choice not in ["direct", "detour"]:
        print("Invalid choice. Please type 'direct' or 'detour'.")
        choice = input("Type 'direct' or 'detour': ").lower()

# if they choose to go directly to the Safe House
    if choice == "direct":
        print("---------------------------------------------------------------------------------------------------------")
        print()
        print("You press forward through the red zone. The air is thick, and the buildings creak with every step.")
        print()
        print("Zuko sticks close. Suddenly, gunfire echoes nearby. Raiders.")
        if "ammo clip" in backpack and "gun without ammo" in backpack:
            print()
            print("You quickly reload your gun using the ammo clip from earlier. With Zuko’s help, you fend off the ambush.")
            print()
            print("You survive—but barely. Zuko is injured, and you use your first aid kit to treat him.")
            print()
            backpack.remove("first aid kit")
            print()
            print("Bloodied but alive, you arrive at the Safe House. The reinforced door slides open after scanning the drone chip.")
            print()
            print("Inside, clean water, medical supplies, and a working radio greet you. You’ve found sanctuary... for now.")
            print()
            print("---------------------------------------------------------------------------------------------------------")
        #no gun/Dead
        else:
            print()
            print("Unarmed, you try to hide—but the raiders spot you. You and Zuko put up a fight, but it’s no use.")
            print()
            print("You both fall in the firefight. Your journey ends here.")
            print()
            print("---------------------------------------------------------------------------------------------------------")

# if they choose to detour around the red zone
    elif choice == "detour":
        print("---------------------------------------------------------------------------------------------------------")
        print()
        print("You circle around the red zone, navigating alleys and collapsing tunnels.")
        print()
        print("It takes longer, and you're forced to ration your food.")
        print()
        if "food" in backpack:
            print("-------------------------------------------------------")
            print()
            print("You eat just enough to keep moving, sharing with Zuko.")
            print()
            print("----------------------------------------------------------------------------------------------------------")
            backpack.remove("food")
        else:
            print("----------------------------------------------------------------------------------------------------------")
            print()
            print("Without food, you both grow weak. Zuko stumbles, but you press on.")
            print()
            print("At last, you reach the Safe House. The drone chip grants you access.")
            print()
            print("It’s quiet. Safe. You made the right call.")
            print()
            print("---------------------------------------------------------------------------------------------------------")

# if they choose to avoid the drone
elif choice == "avoid":
    print("---------------------------------------------------------------------------------------------------------")
    print()
    print("You decide not to risk the drone. You and Zuko follow the map painted on the wall deeper into the city.")
    print()
    print("The path takes you underground—into the subway system. It’s dark, damp, and claustrophobic.")
    print()
    print("You can hear the distant sound of water dripping.")
    print()
    print("Graffiti becomes more frequent, and signs of life appear: torches, food wrappers, paw prints.")
    print()
    print("You arrive at an old maintenance station, converted into a shelter. A man in a gas mask emerges from the shadows.")
    print()
    print("'You're not with the Eastern Raiders, are you?' he asks gruffly. Zuko doesn’t growl—he senses no threat.")
    print()
    print("You shake your head. The man lowers his weapon.")
    print()
    print("'Then you're welcome here. But you'll need to earn your stay. There's something we need help with...'")
    print()
    print("You and Zuko exchange a look. This journey is far from over.")
    print()
    print("---------------------------------------------------------------------------------------------------------")

#if they choose to investigate the noise2
if choice == "investigate":
        print("-----------------------------------------------------------------------------------------------------------------")
        print()
        print("You and Zuko move towards the source of the noise. You find a group of mutated creatures huddled around a fire.")
        print()
        print("They look at you with curiosity but do not attack. Do you want to try to communicate with them or leave quickly?")
        print()
        print("-----------------------------------------------------------------------------------------------------------------")
        choice = input("Type 'communicate' to try talking to them or 'leave' to exit the city: ").lower()
while choice not in ["communicate", "leave"]:
        print("Invalid choice. Please type 'communicate' or 'leave'.")
        choice = input("Type 'communicate' to try talking to them or 'leave' to exit the city: ").lower()

#if they choose to communicate with the creatures2
        print("------------------------------------------------------------------------------------------------------------------")
        print()
        print("The creatures—humanoid but deformed from radiation—gesture for you to sit. Their fire crackles softly.")
        print()
        print("One, who calls himself 'Grak', explains they were once human. Survivors of a failed government experiment.")
        print()
        print("They offer you supplies in exchange for food. You trade willingly, and they hand over clean water and a pouch of used medicine.")
        if "food" in backpack:
            backpack.remove("food")
            add_to_backpack("clean water")
            add_to_backpack("used medicine pouch")
            print("-------------------------------------------------------------------------------------------------------------")
            print()
            print("Zuko warms up to them. You eat, rest, and learn from them.")
            print()
            print("Grak tells you about the dangers of the city, the raiders, and the radiation storms that sweep through.")
            print()
            print("He also mentions a place called 'The Core'—a rumored safe haven where technology still works.")
            print()
            print("You now know of a hidden underground tunnel network they use to move safely through the city.")
            print()
            print("--------------------------------------------------------------------------------------------------------------")
        else:
        print()
        print("But you have no food to trade. They still let you stay the night, offering water for your honesty.")
        add_to_backpack("clean water")
        print()
        print("Grak marks a location on your map: an old subway entrance that leads toward what they call 'The Core'—")
        print()
        print("a place where technology still runs and maybe, just maybe, humanity is trying to rebuild.")
        print()
        print("You and Zuko rest and leave at dawn, guided by the map.")
        print()
        print("You now have a new objective: Reach The Core.")
        print()
        print("But the way won’t be easy. Raiders roam the surface. Radiation storms sweep the ruins. And there’s something worse underground.")
        print()
        print("You reach the subway entrance. Rusted gates creak open as you descend. Zuko sniffs the air—alert.")
        print()
        print("Dim emergency lights flicker to life as you make your way into the tunnels. Your flashlight catches movement ahead.")
        print()
        print("You pause. You hear footsteps and low growls. Not from a creature. From humans.")
        print()
        print("Do you want to hide and wait for them to pass or call out and try to talk?")
        print()
        print("------------------------------------------------------------------------------------------------------------------")
        choice = input("Type 'hide' to avoid them or 'talk' to call out and try to communicate: ").lower()
        while choice not in ["hide", "talk"]:
            print("Invalid choice. Please type 'hide' or 'talk'.")
            choice = input("Type 'hide' or 'talk': ").lower()

#if they choose to hide
        if choice == "hide":
            print("------------------------------------------------------------------------------------------------------------")
            print()
            print("You pull Zuko into the shadows. The figures pass by—armed scavengers wearing makeshift armor.")
            print()
            print("You wait silently as they disappear into the dark. That was close.")
            print()
            print("You continue deeper into the tunnels, following the markings from Grak's map.")
            print()
            print("You eventually find a sealed metal door with a biometric scanner, half-powered.")
            #if they have drone data from previous choice
            if "drone data" in backpack:
                print("-------------------------------------------------------------------------------------------------------------")
                print()
                print("You insert the drone data chip. The door unlocks with a hiss.")
                print()
                print("Inside, you're greeted by lights, humming machines, and a voice on a speaker: 'Welcome to The \"Core\".'")
                print()
                print("--------------------------------------------------------------------------------------------------------------")

            #if no drone data - makes noise to alert the guards/DEAD
            else:
                print("-------------------------------------------------------------------------------------------------------------")
                print()
                print("The scanner denies you entry. You’ll need technology to bypass this. As you took a step back, the anti-theft alarm blares deafeningly, alerting all the guards in proximity.")
                print()
                print("As you turn to run, the guards spot you. You and Zuko make a break for it, but you were outnumbered.")
                print()
                print("You and Zuko died together harshly in this unforgiving world.")
                print()
            print("------------------------------------------------------------------------------------------------------------")

#if they choose to talk
        elif choice == "talk":
            print("------------------------------------------------------------------------------------------------------------")
            print()
            print("You call out. The footsteps stop. Moments later, three humans approach, guns raised.")
            print()
            print("'You're not one of them?' one asks.")
            print()
            print("You explain yourself. After a tense moment, they lower their weapons. They're scouts from a survivor faction called Haven.")
            print()
            print("They’ve also heard of The Core but believe it’s guarded by AI defenses gone rogue.")
            print()
            print("They offer to escort you part of the way in exchange for help carrying some salvaged tech.")
            print()
            print("You accept. The road ahead may be dangerous, but you're no longer alone.")
            print()
            print("------------------------------------------------------------------------------------------------------------")

#if they choose to leave2 - Dead
if choice == "leave":
        print("-----------------------------------------------------------------------------------------------------------------")
        print()
        print("You decide it's too dangerous to investigate further. You quickly exit the city with your supplies.")
        print()
        print("Outside, you stumbled across upon a group of hungry group mutated bears in the distance.")
        print()
        print("Suddenly, they turned their heads into you and ran in the direction you currently standing. You quickly hide behind a car.")
        print()
        print("The bers sniff around, but they don't seem to notice you. You hold your breath, hoping they will leave. After a tense moment, they began to leave")
        print()
        print("As they began to leave, Zuko started barrking at them, gaining their attention.")
        print()
        print("They began rushing towards you, and you quickly try to run away, but it's too late.")
        print()
        print("The bears catch up to you and Zuko, and you realize this is the end. You fought bravely, but the odds were against you.")
        print()
        print("You and Zuko died together harshly in this unforgiving world.")
        print()
        print("-------------------------------------------------------------------------------------------------------------")

#at the end of the game to show backpack contents
print("\nYour final backpack contents: {}".format(backpack))