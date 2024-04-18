#task1 
place = input("Where are you? (forest/cave) ")
if place == "forest":
    action = input("Do you want to climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("Invalid action!")
elif place == "cave":
    print("You find a hidden treasure!")
else:
    print("Invalid place!")

#task2
place = input("Where are you? (forest/cave) ")

if place == "forest":
    action = input("Do you want to climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("Invalid action!")

elif place == "cave":
    torch_decision = input("You are in a dark cave. Do you want to light a torch or proceed in the dark? (light a torch/proceed in the dark) ")
    if torch_decision == "light a torch":
        print("You light a torch and illuminate the cave. You find a hidden treasure!")
    elif torch_decision == "proceed in the dark":
        print("You proceed in the dark and stumble upon obstacles. Unfortunately, you trip and fall, ending your adventure.")
    else:
        print("Invalid decision!")

else:
    print("Invalid place!")

#task3
place = input("Where are you? (forest/cave) ")

if place == "forest":
    action = input("Do you want to climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("Invalid action!")

elif place == "cave":
    torch_decision = input("You are in a dark cave. Do you want to light a torch or proceed in the dark? (light a torch/proceed in the dark) ")
    if torch_decision == "light a torch":
        print("You light a torch and illuminate the cave. You find a hidden treasure!")
    elif torch_decision == "proceed in the dark":
        print("You proceed in the dark and stumble upon obstacles. Unfortunately, you trip and fall, ending your adventure.")
    else:
        pass
else:
    pass 