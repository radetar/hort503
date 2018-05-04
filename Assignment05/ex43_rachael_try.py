class Scene(object):

        def enter(self):
            pass

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        scene_map.opening_scene()


class Death(Scene):

    def enter(self):
        print("You died, good job!")

class CentralCorridor(Scene):

    def enter(self):
        print("You are standing in a long corridor. A large Gothon blocks your path. It is well known that a Gothon's weakness is laughter. What do you do?")
        response = input("> ")
        if "joke" in response:
            print("The gothon doubles over in laughter, and passes out")
            a_map.next_scene(LaserWeaponArmory)
        elif "laugh" in response:
            print("The gothon doubles over in laughter, and passes out")
            a_map.next_scene(LaserWeaponArmory)
        else:
            print("The Gothon shoots you.")
            a_map.next_scene(Death)



class LaserWeaponArmory(Scene):

    def enter(self):
        print("You come upon the door for the armory. It has a keypad to get in. You get three trys to guess the 5 digit code before you are lasered to death. ")
        trys = 0
        while trys < 3:
            guess = input("> ")
            if "12345" in guess:
                print("Wow these guys don't get password security at all. You get into the armory and steal a snuggle bomb.")
                a_map.next_scene(TheBridge)
            else:
                trys =+ 1
        a_map.next_scene(Death)



class TheBridge(Scene):

    def enter(self):
        print("You are on the bridge and see another gothon. You need to plant the bomb. It is known that gothons are tickleish. What do you do first?")
        response <- input("> ")
        if 'tickle' in response:
            print("Gothon squeals and runs away. You plant the snuggle bomb to ensure pacification of your enemy")
            a_map.next_scene(Escape_Pod)
        else:
            print("The Gothon shoots you")
            a_map.next_scene(Death)


class Escape_Pod(Scene):
    def enter(self):
        print("Finally you get to the escape pod. Only one works. Which one do you pick?")
        response = input("> ")
        if '32' in response :
            print("Yay, you did it! The snuggle bomb explodes in a very politically correct flurry of rainbows and love.You've saved the universe. Good job.")
        else:
            print("Wrong choice")
            a_map.next_scene(Death)



class Map(object):

    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        self.scene_name = scene_name
        self.scene_name.enter()
    def opening_scene(self):
        self.enter()


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
