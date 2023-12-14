class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.orders = []
        self.to_buy = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def add_new_order(self, customer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            self.to_buy[ingredient] += 1
            if self.to_buy[ingredient] > self.MINIMUM_INVENTORY[ingredient]:
                return False
        return self.orders.append([customer, order, day])

    def get_quantities_to_buy(self):
        return self.to_buy

    def get_available_dishes(self):
        orders_available = set()
        for dish in self.INGREDIENTS:
            multiply = 1
            for ingredient in self.INGREDIENTS[dish]:
                estoque = (self.MINIMUM_INVENTORY[ingredient] -
                           self.to_buy[ingredient])
                multiply = multiply * estoque
            if multiply:
                orders_available.add(dish)
        return orders_available
