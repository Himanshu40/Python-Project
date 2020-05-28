# Challenge 1 : Create a function named large_power() that takes two parameters named base and exponent.
#              If base raised to the exponent is greater than 5000, return True, otherwise return False
# Date        : Thu 28 May 2020 06:51:58 AM IST

def large_power(base, exponent):
    if (base ** exponent) > 5000:
        return True
    else:
        return False

print(large_power(2, 13))
print(large_power(2, 12))
