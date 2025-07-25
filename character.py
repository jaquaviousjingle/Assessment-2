#CHARACTER CLASS

class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

#Describe this character

    def describe(self):
        print(self.name + " is here")
        print(self.description)

#Set what this character will say when talked to

    def set_conversation(self, conversation):
        self.conversation = conversation

#Talk to this Character

    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " can't talk to you right now.")

#Fight with this Character

    def fight(self, combat_item):
        print(self.name + "doesn't want to fight with you.")
        return True

#ENEMY CLASS

class Enemy(Character):
    def __init__(self, char_name, char_description, health):
        super().__init__(char_name, char_description)
        self.health = health
        self.weakness = None
                
    def set_health(self, health):
        self.health = health

    def set_weakness(self, weakness):
        self.weakness = weakness
        
    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True

    def steal(self):
        print("You steal from " + self.name)

#FRIEND CLASS

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None
