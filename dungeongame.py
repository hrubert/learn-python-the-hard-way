from sys import exit
from random import randint
from textwrap import dedent


class Character(object):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class Scene(object): 
    def __init__(self):
        pass
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

    def combat(self):
        pass


class Engine(object):
    pass


class Death(Scene):
    pass


class Floor1(Scene):
    def __init__(self):
        pass

    def enter(self):
        print(dedent("""
        You wake up with one hell of a headache. Your vision
        blurry, you examine your surroundings. The floor feels
        rough and sticky. It is dried blood, possibly your own.
        """))

        Char1 = Character(input("Try to remember your name. >"), 50)

        print(dedent("""
        You recall that your name was {Char1.name}. Any more
        than that is beyond you: Why you have been imprisoned,
        who put you here, if it is double points day at Jersey
        Mike's. Waiting around here is not going to bring your
        memories back.
        """))


class Floor2(Scene):
    pass


class Floor3(Scene):
    pass


class BossRoom(Scene):
    pass


class Sucess(Scene):
    pass


Floor1.enter()