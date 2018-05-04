
#This game is going to be called "PCR Perfection"
#The objective of the game is to do a really good PCR!
#Things to do:
#Figure out how to make an inventory system
#Figure out how to
import random

print(" _ _ _")
print("/ \\ / \\ | \\")
print("| | | | |")
print("|_/ | |_/")
print("| | | \\")
print("| \\_/ | \\")
print("Perfection")
print("By John Hadish")
print("")

Inventory = ["Labcoat", "Gloves"]
Bench = ["Pipette", "PCR tubes", ".5 mL tubes", "Protocol", ""]
#For testing: Bench = ["Pipette", "PCR tubes", ".5 mL tubes", "Protocol", "left primer", "right primer", "Taq", "DNA", "Buffer"]
Minus_20 = ["left primer", "right primer", "Taq", "Dead Fish"]
Fridge = ["DNA", "Buffer", "EtBr"]
PCR = [""]

#Start with False, True, False, True
EtBr_Poisoned = False
Like_Name = True
PI_Dissapointed = False
Alive = True

PI_Gender = "null"
First_Name = "null"
Last_Name = "null"
Fake_First = "null"
Fake_Last = "null"

First_Names = ["Jennifer", "Harold", "Moxie", "Cowboy", "Smith", "Hellen", "Madrid"]
Last_Names = ["the Destroyer", "Doudna", "Helsinki", "Caterday", "Smith", "Anderson"]

#Randomly assigns the players PI a gender. Their is a very small chance they will be
#Gender fluid/neutraL
def pI_gender():
global PI_Gender
y = random.random()
if y > 0.51:
PI_Gender = "he"
elif y < 0.49:
PI_Gender = "she"
else:
PI_Gender = "xe"

#If the player does not like their assigned name, the game will say it alot
def like_name(type):
if Like_Name == False and type == 1:
print(f"Also, your name is still {First_Name} {Last_Name}")
input("> ")
if Like_Name == False and type == 2:
print(f"{First_Name} {Last_Name}")
else:
pass

#Randomly picks a name for the player from a list, and them asks them if they like their name
def players_Name():
global Fake_First
Fake_First = random.choice(First_Names)
global Fake_Last
Fake_Last = random.choice(Last_Names)
global First_Name
First_Name = random.choice(First_Names)
global Last_Name
Last_Name = random.choice(Last_Names)
print(f"Your name is {First_Name} {Last_Name}")
good_name = input("Is this a good name? y/n > ")
print("")
if good_name == "y":
print("Thanks, I made it just for you =)")
input("> ")
elif good_name == "n":
print(f"Well, deal with it, it is what your parents named you,")
print(f"be thankful it wasn't '{Fake_First} {Fake_Last}")
input("> ")
print("Since you dont like your parent given name, I am going to say it alot to you")
input("> ")
global Like_Name
Like_Name = False
like_name(1)
else:
print(f"Yeah, I dont know what that means, so I assume you love your name '{First_Name} {Last_Name}'")
input("> ")


def start():
print("You are standing in an older lab in Johnson Hall")
input("> ")
print("A lab bench is before you, and on it is a pipette, and some test tubes")
input("> ")
print("You look around and see that there is a minus 20 Freezer,")
print("a deli fridge, and a PCR machine")
input("> ")
print("This can mean only one thing... you are going to do a PCR!")
input("> ")
print("If you can do a PCR, you automatically get your Ph.D! \nThis is what you have always wanted!")
input("> ")
print("### How to Play ###\nType only one thing at a time")
input("> ")
print("You interact with the lab by typing an 'action' \nyou then wait for the next prompt and then type a 'thing/place'")
input("> ")
help()
input("> ")
pI_gender()
players_Name()
bench()


def help():
print("Here are the 'actions' you can do:")
input("> ")
print("'move'")
print("'take'")
print("'place'")
print("'inventory'")
print("'help' (pulls up this list)")
print("q (quit)")
input("> ")
print("Remember to only type one thing at a time!")
print("For example, type 'take', wait for the next prompt,")
print("and then type what you want to take.")
input("> ")
print("You can only take things that are present in the area. Spelling counts!")

#The following areas are locations iin the lab

#Once player gets all of required stuff, they get to make the PCR.
def bench():
if all(x in Bench for x in ["PCR tubes", ".5 mL tubes", "left primer", "right primer", "Taq", "DNA", "Buffer"]) and "Pipette" in Inventory:
input("\nYou are ready to perform a PCR! > ")
input("You are mixing everything properly, great job pipetting! > ")
input("You are a natural! > ")
input("Good job, allmost done mixing! > ")
input("Heck yes, all done! > ")
input("You throw everything else that was on the bench besides the 'Prepared PCR Tubes' away!")
global Bench
Bench = ["Prepared PCR Tubes", "Protocol"]
bench()
else:
action(Bench, bench, "your Bench", "On", "What do you do?")

def minus_20():
action(Minus_20, minus_20, "the Minus 20", "In", "There is a message taped to the Minus 20 that says:\n'no gloves when opening or your PI will be mad!!!!'")

def fridge():
like_name(1)
action(Fridge, fridge, "the deli fridge", "In", "What do you do?")

def pCR_machine():
like_name(1)
if "Prepared PCR Tubes" in Inventory:
input("The moment of truth! > ")
input("You have been waiting for this all your life! > ")
input("If you can do this PCR, you get a Ph.D! > ")
#Maybe write some code to take out anything that is inside the PCR macnhine.
input("You put the prepared tubes in the PCR Machine > ")
input("You can almost taste that degree! > ")
button_press()
else:
action(PCR, pCR_machine, "the PCR machine", "In", "You are not ready to run a PCR Yet!\nWhat do you do?")


def button_press():
x = int(input("\nWhich button do you press? \n1) Start PCR \n2) Blow up Lab\n > "))
if x is 1:
input(f"You did it! You did a PCR and got your Ph.D! \n(Dont worry, Dr. {Fake_Last}'s next grad student will run the gel)")
end()
elif x is 2:
input("Ok, an unexpected decision this late in your Ph.D, but I respect your decisions. > ")
input("After all, grad school is about learning how to make decisions, even if they are the wrong ones > ")
input("You laugh as everything you worked for goes up in flames")
global Alive
Alive = False
end()
else:
print("It is either button '1' or '2'")
button_press()

#This is the end game session. It remembers what you did during the game.
def end():
print("\nWell, it looks like this is the end of the game!")
input("> ")
if Alive == True:
print("I am so proud of you for doing a PCR and getting your Ph.D!")
else:
print("Too bad you died in that tragic PCR accident! \nThey should really make those machines more safe!")

input("> ")
if PI_Dissapointed == False:
print(f"Your PI, Dr. {Fake_First} {Fake_Last}, is very proud of you for being safe \nby not touching the Minus 20 with your gloves on.")
input("> ")
if Alive == False:
print("Even though it was not safe when you blew up the lab")
else:
pass
else:
print(f"However, your PI, Dr.{Fake_First} {Fake_Last}, is very dissapointed in you for\ntouching the Minus 20 with your gloves on.")
input("> ")
print("That is bad lab etiquite, and you should be ashamed of yourself.")
input("> ")
print("You are a terrible human for that, I mean, there was a sign and everything!")

input("> ")
if Alive == True and PI_Dissapointed == False:
print(f"You walk across the stage to receive your diploma with Dr. {Fake_Last} cheering you on.")
elif Alive == True and PI_Dissapointed == True:
print(f"You walk across the stage to receive your diploma, but Dr. {Fake_Last}")
print("is nowhere to be seen in the crowd of cheering faces.")
input("> ")
print(f"{PI_gender} hates you for touching the damn Freezer with gloves on")
input("> ")
print("And will try to destroy your career as a scientist becasue of it")
elif Alive == False:
print(f"At your funeral, Dr. {Fake_Last} gives a touching eulogy:")
input("> ")
print("'Rot in science hell for destroying the lab, you piece of shit'")
input("> ")
if PI_Dissapointed == True:
print("I hate you for touching my Freezer with gloves on")
else:
print("'But at least you didn't touch the Freezer with gloves on!''")
else:
pass
input("> ")
print("The End!")
input("Thanks for playing!")
if EtBr_Poisoned == True and Alive == True:
input("Oh, and I almost forgot, since you touched the EtBr earlier without gloves, \nyou get cancer a few years later.")
input("Lucky for you, however, science has advanced to the point where we can cure that easy")
input("And you helped science get there, by doing a great PCR!")
exit()
else:
exit()
#This function happens if you take something out of the minus 20 with gloves on.
def madPI(area):
input("Oh shit, no you didn't! > ")
input("You took something out of the -20 with gloves on! > ")
input(f"You hear your PI, {Fake_First} {Fake_Last} coming! > ")
input(f"{PI_Gender} is pissed! >")
input(f"{PI_Gender} looks at you and nods in shame. > ")
input("You are a terrible graduate student! > ")
print("")
global PI_Dissapointed
PI_Dissapointed = True
area()



#This is how you move to a new location
def move():
print("\nWhere do you want to move too?")
print("""Bench\nMinus20\nFridge\nPCR Machine""")
x = input("> ")
y = "\n\n"
if x == "Bench":
print(y)
bench()
elif x == "Minus20":
print(y)
minus_20()
elif x == "Fridge":
print(y)
fridge()
elif x == "PCR Machine":
print(y)
pCR_machine()
elif x == "q":
exit()
else:
print("I do not know where that is")
input("> ")
move()

#This is how you take an item. It should probably be made to look more like action
#so that it talks about the location and stuff
def take(area_list, area):
print("\nThese objects are present", area_list)
print("Which item do you want to take?")
x = input("> ")
if x in area_list:
Inventory.append(x)
area_list.remove(x)
input("Taken > ")
if x == "EtBr" and ("Gloves" not in Inventory):
global EtBr_Poisoned
EtBr_Poisoned = True
print("Dang, thats hard core picking up EtBr without gloves")
area()
elif area == minus_20 and "Gloves" in Inventory:
if PI_Dissapointed == False:
madPI(area)
else:
input("Since your PI alread knows you are a piece of crap, you can wear your gloves wherever!")
area()
elif x == "Dead Fish":
print(f"Gross, I dont know why your PI, {Fake_First} {Fake_Last} keeps that in here.")
print(f"Supossidly it used to be a pet that {PI_Gender} wants to revive with Science")
area()
elif x == "Protocol":
input("The Protocol says: > ")
input("To do a PCR, get the following things and put them on your bench > ")
input("*PCR tubes\n*.5 mL tubes\n*left primer\n*right primer\n*Taq\n*DNA\n*Buffer > ")
input("Once you have these on your bench, pick up your pipette (have Pipette in inventory) > ")
input("and you will mix everything together to get 'Prepared PCR Tubes'! > ")
input("Finally take the 'Prepared PCR tubes' and put them in the PCR Machine > ")
like_name(1)
print("")
input(f"You put the note back on your bench so you wont loose it and have to ask your PI, Dr. {Fake_Last}, for a new one")
Inventory.remove(x)
area_list.append(x)
area()
else:
area()

else:
input("\nThat item is not present > ")
area()

#This is how you place an objects
#Note that there is a special bit for Labcoat
def place(area_list, area):
print("You are holding", Inventory)
print("What do you want to place?")
x = input("> ")
if x in Inventory:
Inventory.remove(x)
area_list.append(x)
input("Placed > ")
if x == "Labcoat":
print("burrr, you are rather cold without your lab coat on")
print("(I forgot to mention it is winter and WSU cut the budget")
print("for heat to fund the football program)")
like_name(1)
input("> ")
area()
else:
area()
else:
input("\nThat item is not in your inventory > ")
like_name(1)
area()

#This is called at every location. It takes imputs specific to that location so
#that it is personalized.
def action(area_list, area, Name, InOn, Extra):
print("\n**********************************")
print(f"\nYou are at, {Name} > ")
print(f"{InOn} {Name} is \n {area_list} > ")
print(Extra)
input1(area_list, area, Name, InOn, Extra)
def input1(area_list, area, Name, InOn, Extra):
x = input("> ")
action2(area_list, area, Name, InOn, Extra, x)
def action2(area_list, area, Name, InOn, Extra, x):
if x == "take":
take(area_list, area)
elif x == "place":
place(area_list, area)
elif x == "move":
move()
elif x == "inventory":
input(f"You have {Inventory} in your posession (exit inventory)> ")
area()
elif x == "q":
exit()
elif x == "help":
help()
area()
else:
x = input("I don't know what that means. >")
action2(area_list, area, Name, InOn, Extra, x)



start()
