# Project : Len's Slice
# Date    : Thu 04 Jun 2020 08:23:03 PM IST

# All kinds of pizzas
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

# Cost of each pizza slice
prices   = [2, 6, 1, 3, 2, 7, 2]

# Length of toppings
num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# Comine toppings and prices
pizzas = list(zip(prices, toppings))

print(pizzas)

# Sort pizzas with lowest prices
pizzas.sort()

# Cheapest Pizza
cheapest_pizza = pizzas[0]

# Priciest Pizza
priciest_pizza = pizzas[-1]

# First three lowest cost pizzas
three_cheapest = pizzas[:3]

print(three_cheapest)

# Number of $2 pizzas
num_two_dollar_slices = prices.count(2)

print(num_two_dollar_slices)
