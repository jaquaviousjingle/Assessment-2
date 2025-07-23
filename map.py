from colours import Colours
class Map:
    def __init__(self):
        self.all_biomes = ["Area 51", "West Deciduous Forest", "East Deciduous Forest", "West Taiga", "East Taiga", "West Tundra", "East Tundra", "Tundra", "The Entity", "No Man's Land"]
        self.visited = []

    def mark(self, biome_name):
        if biome_name in self.visited:
            return f"{biome_name:20}"
        else:
            return f"{'X':12}"


    def show_map(self):
        print("\n========== MAP ==========")
        print("          " + self.mark("Area 51"))
        print("    /          \\")
        print(self.mark("West Deciduous Forest") + "      " + self.mark("East Deciduous Forest"))
        print("|                 |")
        print(self.mark("West Taiga") + "      " + self.mark("East Taiga"))
        print("|                 |")
        print(self.mark("West Tundra") + "     " + self.mark("East Tundra"))
        print("    \\          /")
        print("       " + self.mark("Tundra"))
        print("=========================\n")
        print(Colours.RED + "No Man's Land & The Entity's Residence can't be found on the map." + Colours.RESET)
