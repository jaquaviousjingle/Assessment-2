from character import Enemy

harry = Enemy("Harry", "A smelly wumpus")

harry.describe()

#Add some conversation for Harry when he is talked to

harry.set_conversation("Come closer, I can't see you!")

#Trigger a conversation with Harry

harry.talk()

harry.set_weakness("vegemite")

print("What will you fight with?")
fight_with = input()
harry.fight(fight_with)
