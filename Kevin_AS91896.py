#introduction - the start of the story
print("--------------------------------------------------------------------------------------------------------------------------------------------------")
print("The year is 2087, in a post-apocalyptic nuclear world war, you are with your dog named Zuko. Together, you are scavenging, looking for supplies.")
print()
print("You stumbled upon an dark underground bunker, however, you also see an abandoned city with possible civilization in the distance.")
print("-------------------------------------------------------------------------------------------------------------------------------------------------")
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
    print("As you explore, you find some supplies: a flashlight, a first aid kit, some food, and some parts with missing pieces to make a makeshift gun.")
    print()
    print("You also find a map that shows the layout of the bunker and some notes left by previous survivors.")
    print()
    print("Suddenly, you hear a noise coming from deeper within the bunker. Do you want to investigate the noise or leave quickly?")
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
    print("As you explore, you find some supplies: a flashlight, a first aid kit, and a gun with missing ammo.")    
    print()
    print("Suddenly, you hear a noise coming from one of the buildings. Do you want to investigate the noise or leave quickly?")
    print()
    print("--------------------------------------------------------------------------------------------------------------------")
    choice = input("Type 'investigate' to check out the noise or 'leave' to exit the city: ").lower() 
    while choice not in ["investigate", "leave"]:
        print("Invalid choice. Please type 'investigate' or 'leave'.")
        choice = input("Type 'investigate' to check out the noise or 'leave' to exit the city: ").lower()
        

#if they choose to investigate the noise1
if choice == "investigate":
        print("-----------------------------------------------------------------------------------------------------------------")
        print()
        print("You and Zuko move towards the source of the noise. You find a group of mutated creatures huddled around a fire.")
        print()
        print("They look at you with curiosity but do not attack. Do you want to try to communicate with them or leave quickly?")
        print()
        print("-----------------------------------------------------------------------------------------------------------------")
        choice = input("Type 'communicate' to try talking to them or 'leave' to exit the bunker: ").lower()
while choice not in ["communicate", "leave"]:
        print("Invalid choice. Please type 'communicate' or 'leave'.")
        choice = input("Type 'communicate' to try talking to them or 'leave' to exit the bunker: ").lower()


#if they choose to communicate with the creatures1 - Dead
if choice == "communicate":
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
       #end/game over


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
        choice = input("Type 'disable' to disbale the drone to see if it has any data or 'avoid' to head towards the location marked on the map: ").lower()
while choice not in ["avoid", "disable"]:
        print("Invalid choice. Please type 'disable' or 'avoid'.")
        choice = input("Type 'disable' to disbale the drone to see if it has any data or 'avoid' to head towards the location marked on the map: ").lower()





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
if choice == "communicate":
        print("------------------------------------------------------------------------------------------------------------------")
        print("You cautiously approach the creatures and try to communicate. Surprisingly, they respond in a broken language.")
        print()
        print("They seem friendly and offer you some of their supplies in exchange for food. You accept and leave the bunker with new allies.")
        print()
        print("Zuko seems to like them too, and you feel a sense of hope in this desolate world.")
        print()
        print("")
        print("------------------------------------------------------------------------------------------------------------------")
        #continue of story




#if they choose to leave2 - Dead
elif choice == "leave":
        print("-----------------------------------------------------------------------------------------------------------------")
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
        print("--------------------------------------------------------------")
        #end/game over