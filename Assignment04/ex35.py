from sys import exit
def gold_room():
    print("This room is full of gold. How much do you take?")
    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("man, learn to type a number")
    if how_much < 50:
        print("Nice, you aren't greedy, you win!")

        exit(0)
    else:
        dead("You greedy bastard!")
def bear_room():
    print("There is a bear")
    print("The bear has a bunch of honey")
    print("A fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can now go through")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means?" )

def cthulu_room():
        print("here you see cthulu")
        print("if he stares at you, you go insane")
        print("Do you flee or does he eat your head?")

        choice = input("> ")

        if "flee" in choice :
            start()
        elif "head" in choice:
            dead("well that was tasty!")
        else:
             cthulu_room()
def dead(why):
    print(why, "Good job!")
    exit(0)
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left")
    print("Which one do you take?")
    choice = input("> ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble arount the room and you starve")
start()
