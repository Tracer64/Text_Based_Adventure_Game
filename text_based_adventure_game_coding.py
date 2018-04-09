class Character:
    """ This is the beginning for a lonely Character """

    def __init__(self, name):
        self.name = name


class Adventurer(Character):
    """ Adventurer inherits from Character """
    def speak(self, voice="Hello"):
        self.voice = voice
        return self.voice

class Health(Adventurer):
    """ Health inherits from Adventurer """

class Damsel(Character):
    """ Damsel inherits from Character """
    def speak(self, voice="Help!"):
        self.voice = voice
        return self.voice

x = Adventurer('I Jones')
print(x.speak())


d = Damsel('Damsel in Distress')
print(d.speak())

#Player may say "quit" at any point in time to end the game

Run = True

while Run:
    print("hello")

    ans = input("what do you have to say for yourself?\n>>>")
    if ans == "quit":
        run = False
    input("you said: " + ans + "\n>>> ")
