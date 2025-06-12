#introduction - the start of the story
print("The year is 2087, in a post-apocalyptic nuclear world war, you are with your dog named Zuko. Together, you are scavenging, looking for supplies.")
print("You stumbled upon an dark underground bunker, however, you also see an abandoned city with possible civilization in the distance.")
print("-------------------------------------------------------------------------------------------------------------------------------------------------")
print("You have a choice to make: Do you want to search the dark underground bunker or the abandoned city?")
choice = input("Type 'bunker' to search the bunker or 'city' to search the city: ").lower()

#if they choose to explore the bunker
if choice == "bunker":
    print("------------------------------------------------------------------------------------------------------------------------")
    print("You and Zuko cautiously enter the dark underground bunker. The air is stale, and the lights flicker ominously.")
    print("As you explore, you find some supplies: a flashlight, a first aid kit, and some canned food.")
    print("Suddenly, you hear a noise coming from deeper within the bunker. Do you want to investigate the noise or leave quickly?")
    print("------------------------------------------------------------------------------------------------------------------------")
    choice = input("Type 'investigate' to check out the noise or 'leave' to exit the bunker: ").lower()

#if they choose to investigate the noise
if choice == "investigate":
        print("-----------------------------------------------------------------------------------------------------------------")
        print("You and Zuko move towards the source of the noise. You find a group of mutated creatures huddled around a fire.")
        print("They look at you with curiosity but do not attack. Do you want to try to communicate with them or leave quickly?")
        print("-----------------------------------------------------------------------------------------------------------------")
        choice = input("Type 'communicate' to try talking to them or 'leave' to exit the bunker: ").lower()

#if they choose to communicate with the creatures
        if choice == "communicate":
            print("You cautiously approach the creatures and try to communicate. Surprisingly, they respond in a broken language.")
            print("They seem friendly and offer you some of their supplies in exchange for food. You accept and leave the bunker with new allies.")
            print("Zuko seems to like them too, and you feel a sense of hope in this desolate world.")

#if they choose to leave the bunker
elif choice == "leave":
        print("You decide it's too dangerous to investigate further. You quickly exit the bunker with your supplies.")
        print("Outside, you see the abandoned city again, but now you're better prepared to face whatever lies ahead.")

#if they choose to explore the city
elif choice == "city":
    print("--------------------------------------------------------------------------------------------------------------------")
    print("You and Zuko cautiously approach the abandoned city. The buildings are crumbling, and the streets are eerily quiet.")
    print("As you explore, you find some supplies: a flashlight, a first aid kit, and a gun with no bullets.")    
    print("Suddenly, you hear a noise coming from one of the buildings. Do you want to investigate the noise or leave quickly?")
    print("--------------------------------------------------------------------------------------------------------------------")
    choice = input("Type 'investigate' to check out the noise or 'leave' to exit the city: ").lower()