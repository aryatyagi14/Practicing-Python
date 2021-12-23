
class ShoppingCart:
    def __init__(self, name, cart):
        self.name = name
        self.cart = cart

    def addToCart(self, item, quantity):
        self.item = item
        self.quantity = quantity
        self.cart[item] = quantity

    def removeFromCart(self, item, q):
        self.item = item
        self.q = q
        if( self.cart[item] - self.q <= 0):
            self.cart.pop(item)
        elif(self.quantity - self.q > 0):
            self.cart[item] = self.quantity - self.q
        

    def displayinfo(self):
        print(self.name)
        print(self.cart)

arya = ShoppingCart("walmart", {"milk":2} )
arya.displayinfo()
arya.addToCart("pencils", 20)
arya.displayinfo()
arya.removeFromCart("pencils", 10)
arya.displayinfo()
