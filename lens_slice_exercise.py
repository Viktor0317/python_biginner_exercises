# Len's Slice

# You work at Len’s Slice, a new pizza joint in the neighborhood.
# You are going to use your knowledge of Python lists to organize some of your sales data.

# ----------------------------------------------------------------------------------------

# Your code below:

toppings = ["pepperoni", "pinapple", "cheese", "sausage", "olives", "anchovies", "mashrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
# print(num_two_dollar_slices)

num_pizzas = len(toppings)
print("We sell", num_pizzas, "different kinds of pizza!")
pizza_and_prices = [[2, "pepperoni"], [6, "pinapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mashrooms"]]
# print(pizza_and_prices)

sorted_pizza_and_prices = sorted(pizza_and_prices)
# print(sorted_pizza_and_prices)

cheapest_pizza = sorted_pizza_and_prices[0]
# print(cheapest_pizza)

priciest_pizza = sorted_pizza_and_prices[6]
# print(priciest_pizza)

pizza_and_prices[5].pop()
pizza_and_prices[5].pop()
# print(pizza_and_prices)

pizza_and_prices.insert(6, [2.5, "peppers"])
# print(pizza_and_prices)

three_cheapest = sorted_pizza_and_prices[0:3]
print(three_cheapest)
