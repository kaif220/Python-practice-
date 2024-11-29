# Question: Create a class ShoppingCart with private attributes _items (a list) and _total_price.

class shoping_cart:
    def __init__ (self):
        self._items= []
        self._total_price = 0

    def add_item(self,item,price):
        self._items.append(item)
        self._total_price += price  
    
    def remove_item(self,item,price):
        if item in self._items:
            self._items.remove(item)
            self._total_price -= price
        
    def get_total_price(self):
        return self._total_price
cart = shoping_cart()
cart.add_item("apple", 1.5)
cart.add_item("banana", 2)
cart.remove_item("apple", 1.5)
print(cart.get_total_price()) 