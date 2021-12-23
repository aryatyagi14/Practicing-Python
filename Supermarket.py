class Supermarket:
    def __init__(self, name, openT, inventory):
        self.name = name
        self.openT = openT
        self.inventory = inventory

    def purchase(self, item):
        self.item = item
        if( self.item not in self.inventory):
            print("This store doesnt have that item")
        else:
            print("Item Bought for ", self.inventory[item], "dollars")
            self.inventory[item] = self.inventory[item] -1
        print(self.inventory)

    def returnI(self, item):
        self.item = item
        if( self.item == "dairy"):
            print("You can't return a dairy product")
        elif(self.item in self.inventory):
            print("This item has been returned")
            self.inventory[item] = self.inventory[item] +1
        print(self.inventory)

walmart = Supermarket("walmart", 9, {"dairy": 5, "pencil": 1 })
walmart.purchase("pencil")
walmart.returnI("pencil")
