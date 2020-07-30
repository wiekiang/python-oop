from shoe import Shoe

shoe_one = Shoe('brown', '7.5', 'sneaker', 110)
shoe_two = Shoe('white', '4.5', 'flip-flop', 80)

print(shoe_one.color)
print(shoe_one.price)

shoe_two.change_price(90)
print(shoe_two.price)

shoe_one.color = 'blue'
shoe_one.size = 5.0
shoe_one.price = 78