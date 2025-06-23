class Item:
    def __init__(self, item_name):
        self.item_name = item_name
        self.item_description = None
    
    def set_description(self, item_description):
        self.description = item_description

    def get_description(self):
        return self.description
    
    def set_name(self, item_name):
        self.item_name = item_name
        return self.item_name

    def get_name(self):
        return self.item_name
    
    def describe(self):
        print("The [" + self.item_name +"] is here - " + self.description)