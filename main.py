
from biomes import Biome
from character import Character
from character import Enemy, Friend
from item import Item
import time
dead = False

tundra = Biome("Tundra")
tundra.set_description("The Tundra Biome, the treeless region found on the tops of the mountains, where the climate is cold and windy, and rainfall is scant. Tundra lands are covered with snow for much of the year, but summer brings bursts of wildflowers.")

west_tundra = Biome("West Tundra")
west_tundra.set_description("The Western side of the Tundra Biome, warm and dry but covered in orange grass and tumbleweeds.")

east_tundra = Biome("East Tundra")
east_tundra.set_description("The Eastern Tundra biome - somehow much colder and frostier than the Tundra biome, but possibly holding more useful assets underneath the snowy blanket.")

west_taiga = Biome("West Taiga")
west_taiga.set_description("A biome dominated by coniferous trees, like pine, spruce, and fir, adapted to the harsh climate.")

east_taiga = Biome("East Taiga")
east_taiga.set_description("A subarctic climate with long, severe winters and short, cool summers. Temperatures can range from very cold in the winter to mild in the summer - precipitation is moderate.")

west_deciduous_forest = Biome("West Deciduous Forest")
west_deciduous_forest.set_description("Moist summers and cold winters. Known for its biodiversity, including a variety of trees, shrubs, herbs, and animals")

east_deciduous_forest = Biome("East Deciduous Forest")
east_deciduous_forest.set_description("These woodlands include sugar maples in areas where lakes, rivers, and rugged terrain protect them from fire. At the prairie's edge, where fires are common, oaks dominate.")

area_51 = Biome("Area 51")
area_51.set_description("A highly classified Air Force facility, known for its secrecy and association with conspiracy theories about UFOs and alien technology")

no_mans_land = Biome("No Man's Land")
no_mans_land.set_description("Trenches and pits surround you. Dead trees are the only signs of life in your peripheral, debris and rubble concealing the floor -  basically a vast blanket of nothingness. There is nowhere to go except the final destination.")

the_entity = Biome("Final Destination - The Entity's Residence")
the_entity.set_description("The Entity is an ancient, enigmatic object that emits a powerful signal, drawing every droid across the globe to converge and seek out the remaining humans, with the purpose of uniting them to rebuild the world. There is no way out.")

tundra.link_biome(east_tundra, "east")
tundra.link_biome(west_tundra, "west")
west_tundra.link_biome(tundra, "east")
east_tundra.link_biome(tundra, "west")
west_tundra.link_biome(west_taiga, "north")
east_tundra.link_biome(east_taiga, "north")
west_taiga.link_biome(west_tundra, "south")
east_taiga.link_biome(east_tundra, "south")
west_taiga.link_biome(west_deciduous_forest, "north")
east_taiga.link_biome(east_deciduous_forest, "north")
west_deciduous_forest.link_biome(west_taiga, "south")
east_deciduous_forest.link_biome(east_taiga, "south")
west_deciduous_forest.link_biome(area_51, "east")
east_deciduous_forest.link_biome(area_51, "west")
area_51.link_biome(west_deciduous_forest, "west")
area_51.link_biome(east_deciduous_forest, "east")
area_51.link_biome(no_mans_land, "south")
no_mans_land.link_biome(area_51, "north")
no_mans_land.link_biome(the_entity, "south")

sword = Item("sword")
sword.set_description("A robust and razor-sharp blade - able to defeat a certain enemy")
lightstone = Item("lightstone")
lightstone.set_description("A translucent shard fallen from a star that casts light into the depths of shadows")
hunting_rifle = Item("hunting rifle")
hunting_rifle.set_description("A trusty and rusty one-shot rifle used for eliminating any nearby enemy")
key1 = Item("The First Key")
key1.set_description("One of the two keys needed to access The Entity's Residence")
key2 = Item("The Second Key")
key2.set_description("One of the two keys needed to access The Entity's Residence")

tundra.set_item(lightstone)
west_deciduous_forest.set_item(sword)
east_taiga.set_item(hunting_rifle)
east_deciduous_forest.set_item(key1)
west_taiga.set_item(key2)

sorcerer = Enemy("Astaroth", "The Shadow Sorcerer", 3)
sorcerer.set_conversation("The more you fight, the more you become part of me.")
sorcerer.set_weakness("lightstone")
east_tundra.set_character(sorcerer)

kratos = Enemy("Kratos", "An aggressive, frightening creature", 5)
kratos.set_conversation("G'day, punk.")
kratos.set_weakness("sword")
west_taiga.set_character(kratos)

grizzly = Enemy("Rizzly Grizzly", "A huge, towering brown bear and a brute of nature", 5)
grizzly.set_conversation("Rawr - Grrrrrrr")
grizzly.set_weakness("hunting rifle")
east_deciduous_forest.set_character(grizzly)

helper = Character("Mysterious Being", "I don't recommend you head North, soldier\nyour death might be certain.")
helper.set_conversation("There is nothing more for me to say.")
west_tundra.set_character(helper)

the_assistant = Character("Master Kawhi Leonard", "He might have something to tell you that might help you on your quest.")
the_assistant.set_conversation("Greetings,\nTo get to The Entity's Residence,\nIt is required that you have the two keys.\nIf you do, you shall pass.\nIf not, search for them.")
no_mans_land.set_character(the_assistant)

current_biome = tundra

energy = 28
#heavy = 5
#light = 3
#take = 1

bag = []
valid_directions = ("'north', 'east', 'south' or 'west'")
valid_commands = ["north", "south", "east", "west", "fight", "take", "bag", "energy", "talk"]
help = ("To remember:\n'take' - takes an item from a biome to be used further in your journey\n'fight' - if there is an enemy in the biome, you can battle\n'bag' - shows what you have in your bag\n'energy' - shows you much energy / stamina you have remaining to keep going\n Valid directions that you enter such as " + valid_directions + " will be the direction you travel")
print(help)
print("-----------------------------------------------------------------------")
time.sleep(4)
print("Welcome friend,")
time.sleep(2)
print("This is hopefully a journey you will remember.")
time.sleep(2)
print("All I can say is...")
time.sleep(1)
print("The Entity's Residence is your final destination - make use of the energy you have left to reach it in time")
time.sleep(1.5)
print("Good Luck.")
time.sleep(2)
print("-----------------------------------------------------------------------")

while not dead or energy > 0:
    print("\n")
    current_biome.get_details()
    time.sleep(0.2)
    item = current_biome.get_item()
    time.sleep(0.2)
    if item is not None:
        item.describe()
    time.sleep(0.2)
    inhabitant = current_biome.get_character()
    time.sleep(0.1)
    if inhabitant is not None:
        inhabitant.describe()
    time.sleep(0.1)
    print("What shall you do, companion?")
    command = input("> ")
    command = command.lower()
    if command not in valid_commands:
        print("That is an invalid command, please enter a valid command such as one of the following:")
        print(valid_commands)
    elif command in ["north", "south", "east", "west"] and isinstance(inhabitant, Enemy) == False:
        if current_biome == no_mans_land:
            if key1 not in bag or key2 not in bag:
                print("The Entity's Guardian is here")
                print("[The Guardian says]: You cannot pass without both keys, continue your quest and return when you hold the First and Second Key")
            else:
                current_biome = current_biome.move(command)
        else:
            current_biome = current_biome.move(command)
        
    elif command in ["north", "south", "east", "west"] and isinstance(inhabitant, Enemy) == True:
        print("You can't go that way yet, there are enemies lurking nearby.")
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "fight":
            if inhabitant is not None and isinstance(inhabitant, Enemy) ==  True:
                print("What will you fight with?")
                fight_with = input()
                fight_with = fight_with.lower()
                if fight_with in bag:
                    attack = input("Heavy or Light attack?\n")
                    if inhabitant.fight(fight_with) == True:
                        if attack == "heavy":
                            energy -= 5
                            inhabitant.health -= 5
                        elif attack == "light":
                            energy -= 3
                            inhabitant.health -= 3
                        if inhabitant.health <= 0:
                            print("Bravo, you won this battle!")
                            current_biome.set_character(None)
                            bag.remove(fight_with)
                        else:
                            print("Head home, you have lost this battle - the enemy overpowered you")
                            print("This is the end of the road for you.")
                            dead = True
                    else:
                        print("Head home, you have lost this battle - you couldn't find the enemy's weakness")
                        print("This is the end of the road for you.")
                        dead = True
                else:
                    print("You don't have a " + fight_with)
                    print("This is the end of the road for you\nIt was fun while it lasted.")
                    dead = True
            else:
                print("There is no one here to battle")
            
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your duffel bag")
            bag.append(item.get_name())
            current_biome.set_item(None)
            energy -= 1
    elif command == "bag":
        print(bag)

    elif command == "energy":
        print("You have",energy,"energy remaining")
        print(f"You have used {28 - energy} energy")
    
    if current_biome == the_entity:
        print("Welcome,")
        time.sleep(0.2)
        print("I assume you have travelled far to reach me, and I have also waited through summers and winters.")
        time.sleep(0.2)
        ("And now - I need you to restore the entirety of the world's human race.")
        time(1)