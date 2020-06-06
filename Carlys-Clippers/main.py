# Project : Carly's Clippers
# Date    : Sat 06 Jun 2020 08:19:30 PM IST

# the names of the cuts offered at Carly’s Clippers
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# the price of each hairstyle in the hairstyles list
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# the number of each hairstyle in hairstyles that was purchased last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# to sum up all the prices of haircuts
total_price = 0

for price in prices:
    total_price += price

average_price = total_price / len(prices)

print("Average haircut Price: " + str(average_price))

new_prices = [price - 5 for price in prices]

print(new_prices)

total_revenue = 0

for i in range(len(hairstyles)):
    total_revenue += prices[i] + last_week[i]

print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue / 7

print("Average Daily Revenue: " + str(average_daily_revenue))

cuts_under_30 = [cost for cost in new_prices if cost < 30]

print("Hair Cuts under $30: " + str(cuts_under_30))
