import time
class Biome:

    def __init__(self, biome_name):
        self.name = biome_name
        self.description = None
        self.linked_biomes = {}
        self.character = None
        self.item = None

    def set_description(self, biome_description):
        self.description = biome_description

    def get_description(self):
        return self.description

    def set_name(self, name):
        self.biome_name = name
        return self.biome_name

    def get_name(self):
        return self.name

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character

    def describe(self):
        print(self.description)

    def link_biome(self, biome_to_link, direction):
        self.linked_biomes[direction] = biome_to_link

    def get_details(self):
        print(self.name)
        time.sleep(0.2)
        print("\n---------------------\n")
        time.sleep(0.2)
        print(self.description , "\n")
        time.sleep(0.2)
        for direction in self.linked_biomes:
            biome = self.linked_biomes[direction]
            print(biome.get_name() , "is to the" , direction,"\n")

    def move(self, direction):
        if direction in self.linked_biomes:
            return self.linked_biomes[direction]
        else:
            print("You can't go that way")
            return self

    def set_item(self, item_name):
        self.item = item_name

    def get_item(self):
        return self.item