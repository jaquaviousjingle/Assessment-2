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
no_mans_land.set_description("Trenches and pits surround you. Dead trees are the only signs of life in your peripheral, debris and rubble concealing the floor -  basically a vast blanket of nothingness")

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

sword = Item("sword")
sword.set_description("A robust and razor-sharp blade - able to defeat a certain enemy")
vegemite = Item("vegemite")
vegemite.set_description("Not tasty whatsoever but can be used to defeat a certain enemy")
hunting_rifle = Item("hunting rifle")
hunting_rifle.set_description("A trusty and rusty one-shot rifle used for eliminating any nearby enemy")

tundra.set_item(vegemite)
west_tundra.set_item(sword)
east_taiga.set_item(hunting_rifle)

harry = Enemy("Harry", "A smelly wumpus")
harry.set_conversation("Hangry...Hanggrry")
harry.set_weakness("vegemite") and harry.set_weakness("hunting rifle")
east_tundra.set_character(harry)

kratos = Enemy("Kratos", "An aggressive, frightening creature")
kratos.set_conversation("G'day, punk.")
kratos.set_weakness("sword") and kratos.set_weakness("hunting rifle")
west_taiga.set_character(kratos)

grizzly = Enemy("Rizzly Grizzly", "A huge, towering brown bear and a brute of nature")
grizzly.set_conversation("Rawr - Grrrrrrr")
grizzly.set_weakness("hunting rifle")
east_deciduous_forest.set_character(grizzly)

current_biome = tundra

bag = []

print("Welcome friend,")
time.sleep(1)
print("This is hopefully a journey you will remember.")
time.sleep(2)
print("All I can say is...")
time.sleep(1.5)
print("Good Luck.")
time.sleep(2)

while dead == False:
    
    print("\n")
    current_biome.get_details()
    item = current_biome.get_item()
    if item is not None:
        item.describe()
    inhabitant = current_biome.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    print("What shall you do, companion?")
    command = input("> ")
    command = command.lower()
    if command in ["north", "south", "east", "west"] and inhabitant is None:
        current_biome = current_biome.move(command)
    elif command in ["north", "south", "east", "west"] and inhabitant is not None:
        print("You can't go that way yet, there are enemies lurking nearby.")
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "fight":
            if inhabitant is not None and isinstance(inhabitant, Enemy):
                print("What will you fight with?")
                fight_with = input()
                fight_with = fight_with.lower()
                if fight_with in bag:
                    if inhabitant.fight(fight_with) == True:
                        print("Bravo, you won this battle!")
                        current_biome.set_character(None)
                        bag.remove(fight_with)
                    else:
                        print("Head home, you have lost this battle,")
                        print("This is the end of the road for you.")
                        dead = True
                else:
                    print("You don't have a " + fight_with)
            else:
                print("There is no one here to battle")
    elif command == "hi five":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.hifive()
        else:
            print("There is no one here to hi five :(")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your duffel bag")
            bag.append(item.get_name())
            print(bag)
            current_biome.set_item(None)