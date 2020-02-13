# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items

    def fetchItem(self, itemlist, qty=[]):
        for item in self.items:
            if itemlist.name not in [item.name]:
                self.items.append(item(itemlist.name, itemlist.description, qty))
        else: 
            for item in self.items:
                if item.name == itemlist.name:
                    item.qty += qty