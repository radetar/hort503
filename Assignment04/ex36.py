from sys import exit
def dark_forest():
    print("""You awake in a dark forest. On your left is a small hut with a cheerful fire. On your right is a path into creepy spider-filled woods. Which way do you go?""")
    choice = input("> ")
    if "hut" in choice:
        print("""You enter the hut. A creepy witch grabs you and cooks you with an apple in your mouth, then serves you to her book club.""")
        death()
    elif "path" in choice:
        print("""You start down the creepy path. The spiders catch you, make you into a protein smoothie, and drink you on the way to the gym""")
        death()
    else:
        print("""Way to think for yourself! You turn around see Dr. Ficklin, who leads you to Cat Village He is your fairy godparent for this journey. Fun fact, fairies love computer coding""")
        cat_village()
def cat_village():
    print("""You arrive in cat village. You see a bunch of racist elves bullying 5 kitty children. How many kitty children do you save?""")
    kitties_saved = int(input("> "))
    if kitties_saved == 5:
        print("You are a nice person! You win!!!")
    else:
        print("You are a sick bastard")
        death()
def death():
    print("You die. Good job.")
    exit()

dark_forest()
