# Project : Sal's Shipping
# Date    : Thu 28 May 2020 07:57:42 AM IST

def ground_shipping(weight):
    if weight <= 2.00:
        return (weight * 1.50 + 20.00)
    elif (weight > 2.00) and (weight <= 6.00):
        return (weight * 3.00 + 20.00)
    elif (weight > 6.00) and (weight <= 10.00):
        return (weight * 4.00 + 20.00)
    elif weight > 10.00:
        return (weight * 4.75 + 20.00)

def drone_shipping(weight):
    if weight <= 2.00:
        return (weight * 4.50 + 0.00)
    elif (weight > 2.00) and (weight <= 6.00):
        return (weight * 9.00 + 0.00)
    elif (weight > 6.00) and (weight <= 10.00):
        return (weight * 12.00 + 0.00)
    elif weight > 10.00:
        return (weight * 14.25 + 0.00)

premium_ground_shipping = 125.00

def cheapest_cost(weight):
    ground_shipping_cost = ground_shipping(weight)
    drone_shipping_cost = drone_shipping(weight)

    if (ground_shipping_cost < drone_shipping_cost) and (ground_shipping_cost < premium_ground_shipping):
        print("Ground Shipping is cheapest than Drone Shipping")
        print("Cost for " + str(weight) + " is " + str(ground_shipping_cost) + "\n")
    elif (drone_shipping_cost < ground_shipping_cost) and (drone_shipping_cost < premium_ground_shipping):
        print("Drone Shipping is cheapest than Ground Shipping")
        print("Cost for " + str(weight) + " is " + str(drone_shipping_cost) + "\n")
    else:
        print("Premium Ground Shipping is cheapest than Ground shipping and Drone shipping")
        print("Cost for " + str(weight) + " is " + str(premium_ground_shipping) + "\n")

cheapest_cost(4.8)
cheapest_cost(41.5)

