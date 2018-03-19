from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("This scene is not yet configured")
        print("Subclass it  and implement enter().")
        exit(1)
class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene= self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            #be sure to print out last scene
            current_scene.enter
class Death(Scene):
    quips = ["You died, you suck at this", "Another insult you died", "you died", "you died", "some insult"]
    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""Blah blah blah blah blah blah blah you are on an alien ship kill em' all."""))
        action = input("> ")
        if action == "shoot":
            print("bad choice")
            return 'death'
        elif action == "joke":
            print("good choice")
            return 'laser_weapon_armory'
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent(""" You get into the armory and need to put in a 3 digit code"""))
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0
        while guess != code and guesses < 10:
            print("WRONG. Try again")
            guesses += 1
            guess = input("[keypad]> ")
        if guess == code:
            print("you got it.")
            return 'the_bridge'
        else:
            print("you suck")
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print("You are on the bridge. There is an alien. What do you do?")

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("you die"))
            return 'death'
        elif action == "set bomb":
            print("good choice")
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE")
            return 'the_bridge'

class EscapePod(Scene):
    def enter(self):
        print("Ok you get the pods. Which pod you take?")
        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print("Bad choice")
            return 'death'
        else:
            print("You live")
            return 'finished'

class Finished(Scene):
    def enter(self):
        print("You won!")
        return 'finished'

class Map(object):
    scenes = {'central_corridor':CentralCorridor(), 'laser_weapon_armory':LaserWeaponArmory(), 'the_bridge':'TheBridge()', 'escape_pod':EscapePod(), 'death': Death(), 'finished':Finished()}
    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
