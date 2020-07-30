class Shoe:

    def __init__(self, shoe_color, shoe_size, shoe_style, shoe_price):
        self.color = shoe_color
        self.size = shoe_size
        self.style = shoe_style
        self.price = shoe_price

    def change_price(self, new_price):
        self.price = 0.81 * new_price

    def discount(self, discount):
        return self.price * (1 - discount)